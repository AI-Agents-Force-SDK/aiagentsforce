from typing import List

from aiagentsforce_core.callbacks import CallbackManagerForRetrieverRun
from aiagentsforce_core.documents import Document
from aiagentsforce_core.retrievers import BaseRetriever

from aiagentsforce_community.utilities.pubmed import PubMedAPIWrapper


class PubMedRetriever(BaseRetriever, PubMedAPIWrapper):
    """`PubMed API` retriever.

    It wraps load() to get_relevant_documents().
    It uses all PubMedAPIWrapper arguments without any change.
    """

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        return self.load_docs(query=query)
