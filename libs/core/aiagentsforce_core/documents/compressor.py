from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Optional

from pydantic import BaseModel

from aiagentsforce_core.callbacks import Callbacks
from aiagentsforce_core.documents import Document
from aiagentsforce_core.runnables import run_in_executor


class BaseDocumentCompressor(BaseModel, ABC):
    """Base class for document compressors.

    This abstraction is primarily used for
    post-processing of retrieved documents.

    Documents matching a given query are first retrieved.
    Then the list of documents can be further processed.

    For example, one could re-rank the retrieved documents
    using an LLM.

    **Note** users should favor using a RunnableLambda
    instead of sub-classing from this interface.
    """

    @abstractmethod
    def compress_documents(
        self,
        documents: Sequence[Document],
        query: str,
        callbacks: Optional[Callbacks] = None,
    ) -> Sequence[Document]:
        """Compress retrieved documents given the query context.

        Args:
            documents: The retrieved documents.
            query: The query context.
            callbacks: Optional callbacks to run during compression.

        Returns:
            The compressed documents.
        """

    async def acompress_documents(
        self,
        documents: Sequence[Document],
        query: str,
        callbacks: Optional[Callbacks] = None,
    ) -> Sequence[Document]:
        """Async compress retrieved documents given the query context.

        Args:
            documents: The retrieved documents.
            query: The query context.
            callbacks: Optional callbacks to run during compression.

        Returns:
            The compressed documents.
        """
        return await run_in_executor(
            None, self.compress_documents, documents, query, callbacks
        )
