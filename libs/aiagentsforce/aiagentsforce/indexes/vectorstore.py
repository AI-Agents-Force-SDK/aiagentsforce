from typing import Any, Dict, List, Optional, Type

from aiagentsforce_core.document_loaders import BaseLoader
from aiagentsforce_core.documents import Document
from aiagentsforce_core.embeddings import Embeddings
from aiagentsforce_core.language_models import BaseLanguageModel
from aiagentsforce_core.vectorstores import VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter
from pydantic import BaseModel, ConfigDict, Field

from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain.chains.retrieval_qa.base import RetrievalQA


def _get_default_text_splitter() -> TextSplitter:
    return RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)


class VectorStoreIndexWrapper(BaseModel):
    """Wrapper around a vectorstore for easy access."""

    vectorstore: VectorStore

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="forbid",
    )

    def query(
        self,
        question: str,
        llm: Optional[BaseLanguageModel] = None,
        retriever_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> str:
        """Query the vectorstore."""
        if llm is None:
            raise NotImplementedError(
                "This API has been changed to require an LLM. "
                "Please provide an llm to use for querying the vectorstore.\n"
                "For example,\n"
                "from langchain_openai import OpenAI\n"
                "llm = OpenAI(temperature=0)"
            )
        retriever_kwargs = retriever_kwargs or {}
        chain = RetrievalQA.from_chain_type(
            llm, retriever=self.vectorstore.as_retriever(**retriever_kwargs), **kwargs
        )
        return chain.invoke({chain.input_key: question})[chain.output_key]

    async def aquery(
        self,
        question: str,
        llm: Optional[BaseLanguageModel] = None,
        retriever_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> str:
        """Query the vectorstore."""
        if llm is None:
            raise NotImplementedError(
                "This API has been changed to require an LLM. "
                "Please provide an llm to use for querying the vectorstore.\n"
                "For example,\n"
                "from langchain_openai import OpenAI\n"
                "llm = OpenAI(temperature=0)"
            )
        retriever_kwargs = retriever_kwargs or {}
        chain = RetrievalQA.from_chain_type(
            llm, retriever=self.vectorstore.as_retriever(**retriever_kwargs), **kwargs
        )
        return (await chain.ainvoke({chain.input_key: question}))[chain.output_key]

    def query_with_sources(
        self,
        question: str,
        llm: Optional[BaseLanguageModel] = None,
        retriever_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> dict:
        """Query the vectorstore and get back sources."""
        if llm is None:
            raise NotImplementedError(
                "This API has been changed to require an LLM. "
                "Please provide an llm to use for querying the vectorstore.\n"
                "For example,\n"
                "from langchain_openai import OpenAI\n"
                "llm = OpenAI(temperature=0)"
            )
        retriever_kwargs = retriever_kwargs or {}
        chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm, retriever=self.vectorstore.as_retriever(**retriever_kwargs), **kwargs
        )
        return chain.invoke({chain.question_key: question})

    async def aquery_with_sources(
        self,
        question: str,
        llm: Optional[BaseLanguageModel] = None,
        retriever_kwargs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> dict:
        """Query the vectorstore and get back sources."""
        if llm is None:
            raise NotImplementedError(
                "This API has been changed to require an LLM. "
                "Please provide an llm to use for querying the vectorstore.\n"
                "For example,\n"
                "from langchain_openai import OpenAI\n"
                "llm = OpenAI(temperature=0)"
            )
        retriever_kwargs = retriever_kwargs or {}
        chain = RetrievalQAWithSourcesChain.from_chain_type(
            llm, retriever=self.vectorstore.as_retriever(**retriever_kwargs), **kwargs
        )
        return await chain.ainvoke({chain.question_key: question})


def _get_in_memory_vectorstore() -> Type[VectorStore]:
    """Get the InMemoryVectorStore."""
    import warnings

    try:
        from aiagentsforce_community.vectorstores.inmemory import InMemoryVectorStore
    except ImportError:
        raise ImportError(
            "Please install langchain-community to use the InMemoryVectorStore."
        )
    warnings.warn(
        "Using InMemoryVectorStore as the default vectorstore."
        "This memory store won't persist data. You should explicitly"
        "specify a vectorstore when using VectorstoreIndexCreator"
    )
    return InMemoryVectorStore


class VectorstoreIndexCreator(BaseModel):
    """Logic for creating indexes."""

    vectorstore_cls: Type[VectorStore] = Field(
        default_factory=_get_in_memory_vectorstore
    )
    embedding: Embeddings
    text_splitter: TextSplitter = Field(default_factory=_get_default_text_splitter)
    vectorstore_kwargs: dict = Field(default_factory=dict)

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="forbid",
    )

    def from_loaders(self, loaders: List[BaseLoader]) -> VectorStoreIndexWrapper:
        """Create a vectorstore index from loaders."""
        docs = []
        for loader in loaders:
            docs.extend(loader.load())
        return self.from_documents(docs)

    async def afrom_loaders(self, loaders: List[BaseLoader]) -> VectorStoreIndexWrapper:
        """Create a vectorstore index from loaders."""
        docs = []
        for loader in loaders:
            async for doc in loader.alazy_load():
                docs.append(doc)
        return await self.afrom_documents(docs)

    def from_documents(self, documents: List[Document]) -> VectorStoreIndexWrapper:
        """Create a vectorstore index from documents."""
        sub_docs = self.text_splitter.split_documents(documents)
        vectorstore = self.vectorstore_cls.from_documents(
            sub_docs, self.embedding, **self.vectorstore_kwargs
        )
        return VectorStoreIndexWrapper(vectorstore=vectorstore)

    async def afrom_documents(
        self, documents: List[Document]
    ) -> VectorStoreIndexWrapper:
        """Create a vectorstore index from documents."""
        sub_docs = self.text_splitter.split_documents(documents)
        vectorstore = await self.vectorstore_cls.afrom_documents(
            sub_docs, self.embedding, **self.vectorstore_kwargs
        )
        return VectorStoreIndexWrapper(vectorstore=vectorstore)
