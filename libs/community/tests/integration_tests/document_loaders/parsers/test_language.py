from pathlib import Path

import pytest

from aiagentsforce_community.document_loaders.concurrent import ConcurrentLoader
from aiagentsforce_community.document_loaders.generic import GenericLoader
from aiagentsforce_community.document_loaders.parsers import LanguageParser


def test_language_loader_for_python() -> None:
    """Test Python loader with parser enabled."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = GenericLoader.from_filesystem(
        file_path, glob="hello_world.py", parser=LanguageParser(parser_threshold=5)
    )
    docs = loader.load()

    assert len(docs) == 2

    metadata = docs[0].metadata
    assert metadata["source"] == str(file_path / "hello_world.py")
    assert metadata["content_type"] == "functions_classes"
    assert metadata["language"] == "python"
    metadata = docs[1].metadata
    assert metadata["source"] == str(file_path / "hello_world.py")
    assert metadata["content_type"] == "simplified_code"
    assert metadata["language"] == "python"

    assert (
        docs[0].page_content
        == """def main():
    print("Hello World!")  # noqa: T201

    return 0"""
    )
    assert (
        docs[1].page_content
        == """#!/usr/bin/env python3

import sys


# Code for: def main():


if __name__ == "__main__":
    sys.exit(main())"""
    )


def test_language_loader_for_python_with_parser_threshold() -> None:
    """Test Python loader with parser enabled and below threshold."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = GenericLoader.from_filesystem(
        file_path,
        glob="hello_world.py",
        parser=LanguageParser(language="python", parser_threshold=1000),
    )
    docs = loader.load()

    assert len(docs) == 1


def esprima_installed() -> bool:
    try:
        import esprima  # noqa: F401

        return True
    except Exception as e:
        print(f"esprima not installed, skipping test {e}")  # noqa: T201
        return False


@pytest.mark.skipif(not esprima_installed(), reason="requires esprima package")
def test_language_loader_for_javascript() -> None:
    """Test JavaScript loader with parser enabled."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = GenericLoader.from_filesystem(
        file_path, glob="hello_world.js", parser=LanguageParser(parser_threshold=5)
    )
    docs = loader.load()

    assert len(docs) == 3

    metadata = docs[0].metadata
    assert metadata["source"] == str(file_path / "hello_world.js")
    assert metadata["content_type"] == "functions_classes"
    assert metadata["language"] == "js"
    metadata = docs[1].metadata
    assert metadata["source"] == str(file_path / "hello_world.js")
    assert metadata["content_type"] == "functions_classes"
    assert metadata["language"] == "js"
    metadata = docs[2].metadata
    assert metadata["source"] == str(file_path / "hello_world.js")
    assert metadata["content_type"] == "simplified_code"
    assert metadata["language"] == "js"

    assert (
        docs[0].page_content
        == """class HelloWorld {
  sayHello() {
    console.log("Hello World!");
  }
}"""
    )
    assert (
        docs[1].page_content
        == """function main() {
  const hello = new HelloWorld();
  hello.sayHello();
}"""
    )
    assert (
        docs[2].page_content
        == """// Code for: class HelloWorld {

// Code for: function main() {

main();"""
    )


def test_language_loader_for_javascript_with_parser_threshold() -> None:
    """Test JavaScript loader with parser enabled and below threshold."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = GenericLoader.from_filesystem(
        file_path,
        glob="hello_world.js",
        parser=LanguageParser(language="js", parser_threshold=1000),
    )
    docs = loader.load()

    assert len(docs) == 1


def test_concurrent_language_loader_for_javascript_with_parser_threshold() -> None:
    """Test JavaScript ConcurrentLoader with parser enabled and below threshold."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = ConcurrentLoader.from_filesystem(
        file_path,
        glob="hello_world.js",
        parser=LanguageParser(language="js", parser_threshold=1000),
    )
    docs = loader.load()

    assert len(docs) == 1


def test_concurrent_language_loader_for_python_with_parser_threshold() -> None:
    """Test Python ConcurrentLoader with parser enabled and below threshold."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = ConcurrentLoader.from_filesystem(
        file_path,
        glob="hello_world.py",
        parser=LanguageParser(language="python", parser_threshold=1000),
    )
    docs = loader.load()

    assert len(docs) == 1


@pytest.mark.skipif(not esprima_installed(), reason="requires esprima package")
def test_concurrent_language_loader_for_javascript() -> None:
    """Test JavaScript ConcurrentLoader with parser enabled."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = ConcurrentLoader.from_filesystem(
        file_path, glob="hello_world.js", parser=LanguageParser(parser_threshold=5)
    )
    docs = loader.load()

    assert len(docs) == 3


def test_concurrent_language_loader_for_python() -> None:
    """Test Python ConcurrentLoader with parser enabled."""
    file_path = Path(__file__).parent.parent.parent / "examples"
    loader = ConcurrentLoader.from_filesystem(
        file_path, glob="hello_world.py", parser=LanguageParser(parser_threshold=5)
    )
    docs = loader.load()

    assert len(docs) == 2
