"""Test manifest integration."""

from aiagentsforce_community.llms.manifest import ManifestWrapper


def test_manifest_wrapper() -> None:
    """Test manifest wrapper."""
    from manifest import Manifest

    manifest = Manifest(client_name="openai")
    llm = ManifestWrapper(client=manifest, llm_kwargs={"temperature": 0})
    output = llm.invoke("The capital of New York is:")
    assert output == "Albany"
