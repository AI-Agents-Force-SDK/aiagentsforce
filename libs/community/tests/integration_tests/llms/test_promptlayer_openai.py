"""Test PromptLayer OpenAI API wrapper."""

from pathlib import Path
from typing import Generator

import pytest

from aiagentsforce_community.llms.loading import load_llm
from aiagentsforce_community.llms.promptlayer_openai import PromptLayerOpenAI


def test_promptlayer_openai_call() -> None:
    """Test valid call to promptlayer openai."""
    llm = PromptLayerOpenAI(max_tokens=10)  # type: ignore[call-arg]
    output = llm.invoke("Say foo:")
    assert isinstance(output, str)


def test_promptlayer_openai_extra_kwargs() -> None:
    """Test extra kwargs to promptlayer openai."""
    # Check that foo is saved in extra_kwargs.
    llm = PromptLayerOpenAI(foo=3, max_tokens=10)  # type: ignore[call-arg]
    assert llm.max_tokens == 10
    assert llm.model_kwargs == {"foo": 3}

    # Test that if extra_kwargs are provided, they are added to it.
    llm = PromptLayerOpenAI(foo=3, model_kwargs={"bar": 2})  # type: ignore[call-arg]
    assert llm.model_kwargs == {"foo": 3, "bar": 2}

    # Test that if provided twice it errors
    with pytest.raises(ValueError):
        PromptLayerOpenAI(foo=3, model_kwargs={"foo": 2})  # type: ignore[call-arg]


def test_promptlayer_openai_stop_valid() -> None:
    """Test promptlayer openai stop logic on valid configuration."""
    query = "write an ordered list of five items"
    first_llm = PromptLayerOpenAI(stop="3", temperature=0)  # type: ignore[call-arg]
    first_output = first_llm.invoke(query)
    second_llm = PromptLayerOpenAI(temperature=0)  # type: ignore[call-arg]
    second_output = second_llm.invoke(query, stop=["3"])
    # Because it stops on new lines, shouldn't return anything
    assert first_output == second_output


def test_promptlayer_openai_stop_error() -> None:
    """Test promptlayer openai stop logic on bad configuration."""
    llm = PromptLayerOpenAI(stop="3", temperature=0)  # type: ignore[call-arg]
    with pytest.raises(ValueError):
        llm.invoke("write an ordered list of five items", stop=["\n"])


def test_saving_loading_llm(tmp_path: Path) -> None:
    """Test saving/loading an promptlayer OpenAPI LLM."""
    llm = PromptLayerOpenAI(max_tokens=10)  # type: ignore[call-arg]
    llm.save(file_path=tmp_path / "openai.yaml")
    loaded_llm = load_llm(tmp_path / "openai.yaml")
    assert loaded_llm == llm


def test_promptlayer_openai_streaming() -> None:
    """Test streaming tokens from promptalyer OpenAI."""
    llm = PromptLayerOpenAI(max_tokens=10)  # type: ignore[call-arg]
    generator = llm.stream("I'm Pickle Rick")

    assert isinstance(generator, Generator)

    for token in generator:
        assert isinstance(token["choices"][0]["text"], str)
