"""Test Google PaLM Chat API wrapper.

Note: This test must be run with the GOOGLE_API_KEY environment variable set to a
      valid API key.
"""

from aiagentsforce_core.messages import BaseMessage, HumanMessage, SystemMessage
from aiagentsforce_core.outputs import ChatGeneration, ChatResult, LLMResult

from aiagentsforce_community.chat_models import ChatGooglePalm


def test_chat_google_palm() -> None:
    """Test Google PaLM Chat API wrapper."""
    chat = ChatGooglePalm()  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = chat.invoke([message])
    assert isinstance(response, BaseMessage)
    assert isinstance(response.content, str)


def test_chat_google_palm_system_message() -> None:
    """Test Google PaLM Chat API wrapper with system message."""
    chat = ChatGooglePalm()  # type: ignore[call-arg]
    system_message = SystemMessage(content="You are to chat with the user.")
    human_message = HumanMessage(content="Hello")
    response = chat.invoke([system_message, human_message])
    assert isinstance(response, BaseMessage)
    assert isinstance(response.content, str)


def test_chat_google_palm_generate() -> None:
    """Test Google PaLM Chat API wrapper with generate."""
    chat = ChatGooglePalm(n=2, temperature=1.0)  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = chat.generate([[message], [message]])
    assert isinstance(response, LLMResult)
    assert len(response.generations) == 2
    for generations in response.generations:
        assert len(generations) == 2
        for generation in generations:
            assert isinstance(generation, ChatGeneration)
            assert isinstance(generation.text, str)
            assert generation.text == generation.message.content


def test_chat_google_palm_multiple_completions() -> None:
    """Test Google PaLM Chat API wrapper with multiple completions."""
    # The API de-dupes duplicate responses, so set temperature higher. This
    # could be a flakey test though...
    chat = ChatGooglePalm(n=5, temperature=1.0)  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = chat._generate([message])
    assert isinstance(response, ChatResult)
    assert len(response.generations) == 5
    for generation in response.generations:
        assert isinstance(generation.message, BaseMessage)
        assert isinstance(generation.message.content, str)


async def test_async_chat_google_palm() -> None:
    """Test async generation."""
    chat = ChatGooglePalm(n=2, temperature=1.0)  # type: ignore[call-arg]
    message = HumanMessage(content="Hello")
    response = await chat.agenerate([[message], [message]])
    assert isinstance(response, LLMResult)
    assert len(response.generations) == 2
    for generations in response.generations:
        assert len(generations) == 2
        for generation in generations:
            assert isinstance(generation, ChatGeneration)
            assert isinstance(generation.text, str)
            assert generation.text == generation.message.content
