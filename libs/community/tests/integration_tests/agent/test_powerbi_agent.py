import pytest
from aiagentsforce_core.utils import get_from_env

from aiagentsforce_community.agent_toolkits import PowerBIToolkit, create_pbi_agent
from aiagentsforce_community.chat_models import ChatOpenAI
from aiagentsforce_community.utilities.powerbi import PowerBIDataset


def azure_installed() -> bool:
    try:
        from azure.core.credentials import TokenCredential  # noqa: F401
        from azure.identity import DefaultAzureCredential  # noqa: F401

        return True
    except Exception as e:
        print(f"azure not installed, skipping test {e}")  # noqa: T201
        return False


@pytest.mark.skipif(not azure_installed(), reason="requires azure package")
def test_daxquery() -> None:
    from azure.identity import DefaultAzureCredential

    DATASET_ID = get_from_env("", "POWERBI_DATASET_ID")
    TABLE_NAME = get_from_env("", "POWERBI_TABLE_NAME")
    NUM_ROWS = get_from_env("", "POWERBI_NUMROWS")

    fast_llm = ChatOpenAI(
        temperature=0.5, max_tokens=1000, model_name="gpt-3.5-turbo", verbose=True
    )  # type: ignore[call-arg]
    smart_llm = ChatOpenAI(
        temperature=0, max_tokens=100, model_name="gpt-4", verbose=True
    )  # type: ignore[call-arg]

    toolkit = PowerBIToolkit(
        powerbi=PowerBIDataset(
            dataset_id=DATASET_ID,
            table_names=[TABLE_NAME],
            credential=DefaultAzureCredential(),
        ),
        llm=smart_llm,
    )

    agent_executor = create_pbi_agent(llm=fast_llm, toolkit=toolkit, verbose=True)

    output = agent_executor.run(f"How many rows are in the table, {TABLE_NAME}")
    assert NUM_ROWS in output
