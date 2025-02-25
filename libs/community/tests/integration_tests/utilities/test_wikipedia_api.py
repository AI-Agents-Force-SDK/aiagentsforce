"""Integration test for Wikipedia API Wrapper."""

from typing import List

import pytest
from aiagentsforce_core.documents import Document

from aiagentsforce_community.utilities import WikipediaAPIWrapper


@pytest.fixture
def api_client() -> WikipediaAPIWrapper:
    return WikipediaAPIWrapper()  # type: ignore[call-arg]


def test_run_success(api_client: WikipediaAPIWrapper) -> None:
    output = api_client.run("HUNTER X HUNTER")
    assert "Yoshihiro Togashi" in output


def test_run_no_result(api_client: WikipediaAPIWrapper) -> None:
    output = api_client.run(
        "NORESULTCALL_NORESULTCALL_NORESULTCALL_NORESULTCALL_NORESULTCALL_NORESULTCALL"
    )
    assert "No good Wikipedia Search Result was found" == output


def assert_docs(docs: List[Document], all_meta: bool = False) -> None:
    for doc in docs:
        assert doc.page_content
        assert doc.metadata
        main_meta = {"title", "summary", "source"}
        assert set(doc.metadata).issuperset(main_meta)
        if all_meta:
            assert len(set(doc.metadata)) > len(main_meta)
        else:
            assert len(set(doc.metadata)) == len(main_meta)


def test_load_success(api_client: WikipediaAPIWrapper) -> None:
    docs = api_client.load("HUNTER X HUNTER")
    assert len(docs) > 1
    assert len(docs) <= 3
    assert_docs(docs, all_meta=False)


def test_load_success_all_meta(api_client: WikipediaAPIWrapper) -> None:
    api_client.load_all_available_meta = True
    docs = api_client.load("HUNTER X HUNTER")
    assert len(docs) > 1
    assert len(docs) <= 3
    assert_docs(docs, all_meta=True)


def test_load_more_docs_success(api_client: WikipediaAPIWrapper) -> None:
    top_k_results = 20
    api_client = WikipediaAPIWrapper(top_k_results=top_k_results)  # type: ignore[call-arg]
    docs = api_client.load("HUNTER X HUNTER")
    assert len(docs) > 10
    assert len(docs) <= top_k_results
    assert_docs(docs, all_meta=False)


def test_load_no_result(api_client: WikipediaAPIWrapper) -> None:
    docs = api_client.load(
        "NORESULTCALL_NORESULTCALL_NORESULTCALL_NORESULTCALL_NORESULTCALL_NORESULTCALL"
    )
    assert not docs
