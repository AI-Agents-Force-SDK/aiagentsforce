"""Utilities for testing purposes."""

import hashlib
from datetime import datetime
from typing import Any, Dict, List, Mapping, Optional, cast

from couchbase.cluster import Cluster
from couchbase.options import GetOptions
from aiagentsforce_core.callbacks import CallbackManagerForLLMRun
from aiagentsforce_core.embeddings import Embeddings
from aiagentsforce_core.language_models.llms import LLM


class FakeEmbeddings(Embeddings):
    """Fake embeddings functionality for testing."""

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Return simple embeddings.
        Embeddings encode each text as its index."""
        return [[float(1.0)] * 9 + [float(i)] for i in range(len(texts))]

    async def aembed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embed_documents(texts)

    def embed_query(self, text: str) -> List[float]:
        """Return constant query embeddings.
        Embeddings are identical to embed_documents(texts)[0].
        Distance to each text will be that text's index,
        as it was passed to embed_documents."""
        return [float(1.0)] * 9 + [float(0.0)]

    async def aembed_query(self, text: str) -> List[float]:
        return self.embed_query(text)


class ConsistentFakeEmbeddings(FakeEmbeddings):
    """Fake embeddings which remember all the texts seen so far to return consistent
    vectors for the same texts."""

    def __init__(self, dimensionality: int = 10) -> None:
        self.known_texts: List[str] = []
        self.dimensionality = dimensionality

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Return consistent embeddings for each text seen so far."""
        out_vectors = []
        for text in texts:
            if text not in self.known_texts:
                self.known_texts.append(text)
            vector = [float(1.0)] * (self.dimensionality - 1) + [
                float(self.known_texts.index(text))
            ]
            out_vectors.append(vector)
        return out_vectors

    def embed_query(self, text: str) -> List[float]:
        """Return consistent embeddings for the text, if seen before, or a constant
        one if the text is unknown."""
        return self.embed_documents([text])[0]


class FakeLLM(LLM):
    """Fake LLM wrapper for testing purposes."""

    queries: Optional[Mapping] = None
    sequential_responses: Optional[bool] = False
    response_index: int = 0

    def get_num_tokens(self, text: str) -> int:
        """Return number of tokens."""
        return len(text.split())

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "fake"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if self.sequential_responses:
            return self._get_next_response_in_sequence
        if self.queries is not None:
            return self.queries[prompt]
        if stop is None:
            return "foo"
        else:
            return "bar"

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        return {}

    @property
    def _get_next_response_in_sequence(self) -> str:
        queries = cast(Mapping, self.queries)
        response = queries[list(queries.keys())[self.response_index]]
        self.response_index = self.response_index + 1
        return response


def cache_key_hash_function(_input: str) -> str:
    """Use a deterministic hashing approach."""
    return hashlib.md5(_input.encode()).hexdigest()


def fetch_document_expiry_time(
    cluster: Cluster,
    bucket_name: str,
    scope_name: str,
    collection_name: str,
    document_key: str,
) -> datetime:
    """Fetch the document's expiry time from the database."""
    collection = (
        cluster.bucket(bucket_name).scope(scope_name).collection(collection_name)
    )
    result = collection.get(document_key, GetOptions(with_expiry=True))

    return result.expiryTime


def get_document_keys(
    cluster: Cluster, bucket_name: str, scope_name: str, query: str
) -> List[str]:
    """Get the document key from the database based on the query using meta().id."""
    scope = cluster.bucket(bucket_name).scope(scope_name)

    result = scope.query(query).execute()

    document_keys = [row["id"] for row in result]
    return document_keys
