"""Test Minimax API wrapper."""

from aiagentsforce_community.llms.minimax import Minimax


def test_minimax_call() -> None:
    """Test valid call to minimax."""
    llm = Minimax(max_tokens=10)  # type: ignore[call-arg]
    output = llm.invoke("Hello world!")
    assert isinstance(output, str)


def test_minimax_call_successful() -> None:
    """Test valid call to minimax."""
    llm = Minimax()  # type: ignore[call-arg]
    output = llm.invoke(
        "A chain is a serial assembly of connected pieces, called links, \
        typically made of metal, with an overall character similar to that\
        of a rope in that it is flexible and curved in compression but \
        linear, rigid, and load-bearing in tension. A chain may consist\
        of two or more links."
    )
    assert isinstance(output, str)
