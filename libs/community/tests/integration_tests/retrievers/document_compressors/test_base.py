"""Integration test for compression pipelines."""

from langchain.retrievers.document_compressors import (
    DocumentCompressorPipeline,
    EmbeddingsFilter,
)
from aiagentsforce_core.documents import Document
from langchain_text_splitters.character import CharacterTextSplitter

from aiagentsforce_community.document_transformers import EmbeddingsRedundantFilter
from aiagentsforce_community.embeddings import OpenAIEmbeddings


def test_document_compressor_pipeline() -> None:
    embeddings = OpenAIEmbeddings()
    splitter = CharacterTextSplitter(chunk_size=20, chunk_overlap=0, separator=". ")
    redundant_filter = EmbeddingsRedundantFilter(embeddings=embeddings)
    relevant_filter = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.8)
    pipeline_filter = DocumentCompressorPipeline(
        transformers=[splitter, redundant_filter, relevant_filter]
    )
    texts = [
        "This sentence is about cows",
        "This sentence was about cows",
        "foo bar baz",
    ]
    docs = [Document(page_content=". ".join(texts))]
    actual = pipeline_filter.compress_documents(docs, "Tell me about farm animals")
    assert len(actual) == 1
    assert actual[0].page_content in texts[:2]


async def test_adocument_compressor_pipeline() -> None:
    embeddings = OpenAIEmbeddings()
    splitter = CharacterTextSplitter(chunk_size=20, chunk_overlap=0, separator=". ")
    redundant_filter = EmbeddingsRedundantFilter(embeddings=embeddings)
    relevant_filter = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.8)
    pipeline_filter = DocumentCompressorPipeline(
        transformers=[splitter, redundant_filter, relevant_filter]
    )
    texts = [
        "This sentence is about cows",
        "This sentence was about cows",
        "foo bar baz",
    ]
    docs = [Document(page_content=". ".join(texts))]
    actual = await pipeline_filter.acompress_documents(
        docs, "Tell me about farm animals"
    )
    assert len(actual) == 1
    assert actual[0].page_content in texts[:2]
