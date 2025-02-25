"""
This file contains a mapping between the lc_namespace path for a given
subclass that implements from Serializable to the namespace
where that class is actually located.

This mapping helps maintain the ability to serialize and deserialize
well-known AI Agents Force objects even if they are moved around in the codebase
across different AI Agents Force versions.

For example,

The code for AIMessage class is located in aiagentsforce_core.messages.ai.AIMessage,
This message is associated with the lc_namespace
["langchain", "schema", "messages", "AIMessage"],
because this code was originally in langchain.schema.messages.AIMessage.

The mapping allows us to deserialize an AIMessage created with an older
version of AI Agents Force where the code was in a different location.
"""

# First value is the value that it is serialized as
# Second value is the path to load it from
SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain", "schema", "messages", "AIMessage"): (
        "aiagentsforce_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "messages", "AIMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("langchain", "schema", "messages", "BaseMessage"): (
        "aiagentsforce_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("langchain", "schema", "messages", "BaseMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessage"): (
        "aiagentsforce_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "messages", "FunctionMessage"): (
        "aiagentsforce_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "messages", "HumanMessage"): (
        "aiagentsforce_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "messages", "SystemMessage"): (
        "aiagentsforce_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "messages", "ToolMessage"): (
        "aiagentsforce_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("langchain", "schema", "messages", "RemoveMessage"): (
        "aiagentsforce_core",
        "messages",
        "modifier",
        "RemoveMessage",
    ),
    ("langchain", "schema", "agent", "AgentAction"): (
        "aiagentsforce_core",
        "agents",
        "AgentAction",
    ),
    ("langchain", "schema", "agent", "AgentFinish"): (
        "aiagentsforce_core",
        "agents",
        "AgentFinish",
    ),
    ("langchain", "schema", "prompt_template", "BasePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "base",
        "BasePromptTemplate",
    ),
    ("langchain", "chains", "llm", "LLMChain"): (
        "langchain",
        "chains",
        "llm",
        "LLMChain",
    ),
    ("langchain", "prompts", "prompt", "PromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("langchain", "prompts", "chat", "MessagesPlaceholder"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "MessagesPlaceholder",
    ),
    ("langchain", "llms", "openai", "OpenAI"): (
        "langchain_openai",
        "llms",
        "base",
        "OpenAI",
    ),
    ("langchain", "prompts", "chat", "ChatPromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("langchain", "prompts", "image", "ImagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "schema", "agent", "AgentActionMessageLog"): (
        "aiagentsforce_core",
        "agents",
        "AgentActionMessageLog",
    ),
    ("langchain", "schema", "agent", "ToolAgentAction"): (
        "langchain",
        "agents",
        "output_parsers",
        "tools",
        "ToolAgentAction",
    ),
    ("langchain", "prompts", "chat", "BaseMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("langchain", "schema", "output", "ChatGeneration"): (
        "aiagentsforce_core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("langchain", "schema", "output", "Generation"): (
        "aiagentsforce_core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("langchain", "schema", "document", "Document"): (
        "aiagentsforce_core",
        "documents",
        "base",
        "Document",
    ),
    ("langchain", "output_parsers", "fix", "OutputFixingParser"): (
        "langchain",
        "output_parsers",
        "fix",
        "OutputFixingParser",
    ),
    ("langchain", "prompts", "chat", "AIMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "AIMessagePromptTemplate",
    ),
    ("langchain", "output_parsers", "regex", "RegexParser"): (
        "langchain",
        "output_parsers",
        "regex",
        "RegexParser",
    ),
    ("langchain", "schema", "runnable", "DynamicRunnable"): (
        "aiagentsforce_core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("langchain", "schema", "prompt", "PromptValue"): (
        "aiagentsforce_core",
        "prompt_values",
        "PromptValue",
    ),
    ("langchain", "schema", "runnable", "RunnableBinding"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("langchain", "schema", "runnable", "RunnableBranch"): (
        "aiagentsforce_core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("langchain", "schema", "runnable", "RunnableWithFallbacks"): (
        "aiagentsforce_core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("langchain", "schema", "output_parser", "StrOutputParser"): (
        "aiagentsforce_core",
        "output_parsers",
        "string",
        "StrOutputParser",
    ),
    ("langchain", "chat_models", "openai", "ChatOpenAI"): (
        "langchain_openai",
        "chat_models",
        "base",
        "ChatOpenAI",
    ),
    ("langchain", "output_parsers", "list", "CommaSeparatedListOutputParser"): (
        "aiagentsforce_core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    ("langchain", "schema", "runnable", "RunnableParallel"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableParallel",
    ),
    ("langchain", "chat_models", "azure_openai", "AzureChatOpenAI"): (
        "langchain_openai",
        "chat_models",
        "azure",
        "AzureChatOpenAI",
    ),
    ("langchain", "chat_models", "bedrock", "BedrockChat"): (
        "langchain_aws",
        "chat_models",
        "bedrock",
        "ChatBedrock",
    ),
    ("langchain", "chat_models", "anthropic", "ChatAnthropic"): (
        "langchain_anthropic",
        "chat_models",
        "ChatAnthropic",
    ),
    ("langchain_groq", "chat_models", "ChatGroq"): (
        "langchain_groq",
        "chat_models",
        "ChatGroq",
    ),
    ("langchain", "chat_models", "fireworks", "ChatFireworks"): (
        "langchain_fireworks",
        "chat_models",
        "ChatFireworks",
    ),
    ("langchain", "chat_models", "google_palm", "ChatGooglePalm"): (
        "langchain",
        "chat_models",
        "google_palm",
        "ChatGooglePalm",
    ),
    ("langchain", "chat_models", "vertexai", "ChatVertexAI"): (
        "langchain_google_vertexai",
        "chat_models",
        "ChatVertexAI",
    ),
    ("langchain", "chat_models", "mistralai", "ChatMistralAI"): (
        "langchain_mistralai",
        "chat_models",
        "ChatMistralAI",
    ),
    ("langchain", "chat_models", "bedrock", "ChatBedrock"): (
        "langchain_aws",
        "chat_models",
        "bedrock",
        "ChatBedrock",
    ),
    ("langchain_google_genai", "chat_models", "ChatGoogleGenerativeAI"): (
        "langchain_google_genai",
        "chat_models",
        "ChatGoogleGenerativeAI",
    ),
    ("langchain", "schema", "output", "ChatGenerationChunk"): (
        "aiagentsforce_core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("langchain", "schema", "messages", "ChatMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("langchain", "schema", "messages", "HumanMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("langchain", "schema", "messages", "FunctionMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("langchain", "schema", "messages", "SystemMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("langchain", "schema", "messages", "ToolMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("langchain", "schema", "output", "GenerationChunk"): (
        "aiagentsforce_core",
        "outputs",
        "generation",
        "GenerationChunk",
    ),
    ("langchain", "llms", "openai", "BaseOpenAI"): (
        "langchain",
        "llms",
        "openai",
        "BaseOpenAI",
    ),
    ("langchain", "llms", "bedrock", "Bedrock"): (
        "langchain_aws",
        "llms",
        "bedrock",
        "BedrockLLM",
    ),
    ("langchain", "llms", "fireworks", "Fireworks"): (
        "langchain_fireworks",
        "llms",
        "Fireworks",
    ),
    ("langchain", "llms", "google_palm", "GooglePalm"): (
        "langchain",
        "llms",
        "google_palm",
        "GooglePalm",
    ),
    ("langchain", "llms", "openai", "AzureOpenAI"): (
        "langchain_openai",
        "llms",
        "azure",
        "AzureOpenAI",
    ),
    ("langchain", "llms", "replicate", "Replicate"): (
        "langchain",
        "llms",
        "replicate",
        "Replicate",
    ),
    ("langchain", "llms", "vertexai", "VertexAI"): (
        "langchain_vertexai",
        "llms",
        "VertexAI",
    ),
    ("langchain", "output_parsers", "combining", "CombiningOutputParser"): (
        "langchain",
        "output_parsers",
        "combining",
        "CombiningOutputParser",
    ),
    ("langchain", "schema", "prompt_template", "BaseChatPromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    ("langchain", "prompts", "few_shot_with_templates", "FewShotPromptWithTemplates"): (
        "aiagentsforce_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("langchain", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("langchain", "prompts", "base", "StringPromptValue"): (
        "aiagentsforce_core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("langchain", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValue"): (
        "aiagentsforce_core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("langchain", "prompts", "chat", "ChatPromptValueConcrete"): (
        "aiagentsforce_core",
        "prompt_values",
        "ChatPromptValueConcrete",
    ),
    ("langchain", "schema", "runnable", "HubRunnable"): (
        "langchain",
        "runnables",
        "hub",
        "HubRunnable",
    ),
    ("langchain", "schema", "runnable", "RunnableBindingBase"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableBindingBase",
    ),
    ("langchain", "schema", "runnable", "OpenAIFunctionsRouter"): (
        "langchain",
        "runnables",
        "openai_functions",
        "OpenAIFunctionsRouter",
    ),
    ("langchain", "schema", "runnable", "RouterRunnable"): (
        "aiagentsforce_core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("langchain", "schema", "runnable", "RunnablePassthrough"): (
        "aiagentsforce_core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("langchain", "schema", "runnable", "RunnableSequence"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("langchain", "schema", "runnable", "RunnableEach"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("langchain", "schema", "runnable", "RunnableEachBase"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableAlternatives"): (
        "aiagentsforce_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    ("langchain", "schema", "runnable", "RunnableConfigurableFields"): (
        "aiagentsforce_core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("langchain", "schema", "runnable", "RunnableWithMessageHistory"): (
        "aiagentsforce_core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("langchain", "schema", "runnable", "RunnableAssign"): (
        "aiagentsforce_core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("langchain", "schema", "runnable", "RunnableRetry"): (
        "aiagentsforce_core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
    ("aiagentsforce_core", "prompts", "structured", "StructuredPrompt"): (
        "aiagentsforce_core",
        "prompts",
        "structured",
        "StructuredPrompt",
    ),
}

# Needed for backwards compatibility for old versions of AI Agents Force where things
# Were in different place
_OG_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("langchain", "schema", "AIMessage"): (
        "aiagentsforce_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("langchain", "schema", "ChatMessage"): (
        "aiagentsforce_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("langchain", "schema", "FunctionMessage"): (
        "aiagentsforce_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("langchain", "schema", "HumanMessage"): (
        "aiagentsforce_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("langchain", "schema", "SystemMessage"): (
        "aiagentsforce_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("langchain", "schema", "prompt_template", "ImagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "schema", "agent", "OpenAIToolAgentAction"): (
        "langchain",
        "agents",
        "output_parsers",
        "openai_tools",
        "OpenAIToolAgentAction",
    ),
}

# Needed for backwards compatibility for a few versions where we serialized
# with aiagentsforce_core paths.
OLD_CORE_NAMESPACES_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("aiagentsforce_core", "messages", "ai", "AIMessage"): (
        "aiagentsforce_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("aiagentsforce_core", "messages", "ai", "AIMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "base", "BaseMessage"): (
        "aiagentsforce_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("aiagentsforce_core", "messages", "base", "BaseMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "chat", "ChatMessage"): (
        "aiagentsforce_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("aiagentsforce_core", "messages", "function", "FunctionMessage"): (
        "aiagentsforce_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("aiagentsforce_core", "messages", "human", "HumanMessage"): (
        "aiagentsforce_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("aiagentsforce_core", "messages", "system", "SystemMessage"): (
        "aiagentsforce_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("aiagentsforce_core", "messages", "tool", "ToolMessage"): (
        "aiagentsforce_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("aiagentsforce_core", "agents", "AgentAction"): (
        "aiagentsforce_core",
        "agents",
        "AgentAction",
    ),
    ("aiagentsforce_core", "agents", "AgentFinish"): (
        "aiagentsforce_core",
        "agents",
        "AgentFinish",
    ),
    ("aiagentsforce_core", "prompts", "base", "BasePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "base",
        "BasePromptTemplate",
    ),
    ("aiagentsforce_core", "prompts", "prompt", "PromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "prompt",
        "PromptTemplate",
    ),
    ("aiagentsforce_core", "prompts", "chat", "MessagesPlaceholder"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "MessagesPlaceholder",
    ),
    ("aiagentsforce_core", "prompts", "chat", "ChatPromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "ChatPromptTemplate",
    ),
    ("aiagentsforce_core", "prompts", "chat", "HumanMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "HumanMessagePromptTemplate",
    ),
    ("aiagentsforce_core", "prompts", "chat", "SystemMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "SystemMessagePromptTemplate",
    ),
    ("aiagentsforce_core", "agents", "AgentActionMessageLog"): (
        "aiagentsforce_core",
        "agents",
        "AgentActionMessageLog",
    ),
    ("aiagentsforce_core", "prompts", "chat", "BaseMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "BaseMessagePromptTemplate",
    ),
    ("aiagentsforce_core", "outputs", "chat_generation", "ChatGeneration"): (
        "aiagentsforce_core",
        "outputs",
        "chat_generation",
        "ChatGeneration",
    ),
    ("aiagentsforce_core", "outputs", "generation", "Generation"): (
        "aiagentsforce_core",
        "outputs",
        "generation",
        "Generation",
    ),
    ("aiagentsforce_core", "documents", "base", "Document"): (
        "aiagentsforce_core",
        "documents",
        "base",
        "Document",
    ),
    ("aiagentsforce_core", "prompts", "chat", "AIMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "AIMessagePromptTemplate",
    ),
    ("aiagentsforce_core", "runnables", "configurable", "DynamicRunnable"): (
        "aiagentsforce_core",
        "runnables",
        "configurable",
        "DynamicRunnable",
    ),
    ("aiagentsforce_core", "prompt_values", "PromptValue"): (
        "aiagentsforce_core",
        "prompt_values",
        "PromptValue",
    ),
    ("aiagentsforce_core", "runnables", "base", "RunnableBinding"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableBinding",
    ),
    ("aiagentsforce_core", "runnables", "branch", "RunnableBranch"): (
        "aiagentsforce_core",
        "runnables",
        "branch",
        "RunnableBranch",
    ),
    ("aiagentsforce_core", "runnables", "fallbacks", "RunnableWithFallbacks"): (
        "aiagentsforce_core",
        "runnables",
        "fallbacks",
        "RunnableWithFallbacks",
    ),
    ("aiagentsforce_core", "output_parsers", "string", "StrOutputParser"): (
        "aiagentsforce_core",
        "output_parsers",
        "string",
        "StrOutputParser",
    ),
    ("aiagentsforce_core", "output_parsers", "list", "CommaSeparatedListOutputParser"): (
        "aiagentsforce_core",
        "output_parsers",
        "list",
        "CommaSeparatedListOutputParser",
    ),
    ("aiagentsforce_core", "runnables", "base", "RunnableParallel"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableParallel",
    ),
    ("aiagentsforce_core", "outputs", "chat_generation", "ChatGenerationChunk"): (
        "aiagentsforce_core",
        "outputs",
        "chat_generation",
        "ChatGenerationChunk",
    ),
    ("aiagentsforce_core", "messages", "chat", "ChatMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "human", "HumanMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "function", "FunctionMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "system", "SystemMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "tool", "ToolMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("aiagentsforce_core", "outputs", "generation", "GenerationChunk"): (
        "aiagentsforce_core",
        "outputs",
        "generation",
        "GenerationChunk",
    ),
    ("aiagentsforce_core", "prompts", "chat", "BaseChatPromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "BaseChatPromptTemplate",
    ),
    ("aiagentsforce_core", "prompts", "chat", "ChatMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "ChatMessagePromptTemplate",
    ),
    (
        "aiagentsforce_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ): (
        "aiagentsforce_core",
        "prompts",
        "few_shot_with_templates",
        "FewShotPromptWithTemplates",
    ),
    ("aiagentsforce_core", "prompts", "pipeline", "PipelinePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "pipeline",
        "PipelinePromptTemplate",
    ),
    ("aiagentsforce_core", "prompts", "string", "StringPromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "string",
        "StringPromptTemplate",
    ),
    ("aiagentsforce_core", "prompt_values", "StringPromptValue"): (
        "aiagentsforce_core",
        "prompt_values",
        "StringPromptValue",
    ),
    ("aiagentsforce_core", "prompts", "chat", "BaseStringMessagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "chat",
        "BaseStringMessagePromptTemplate",
    ),
    ("aiagentsforce_core", "prompt_values", "ChatPromptValue"): (
        "aiagentsforce_core",
        "prompt_values",
        "ChatPromptValue",
    ),
    ("aiagentsforce_core", "prompt_values", "ChatPromptValueConcrete"): (
        "aiagentsforce_core",
        "prompt_values",
        "ChatPromptValueConcrete",
    ),
    ("aiagentsforce_core", "runnables", "base", "RunnableBindingBase"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableBindingBase",
    ),
    ("aiagentsforce_core", "runnables", "router", "RouterRunnable"): (
        "aiagentsforce_core",
        "runnables",
        "router",
        "RouterRunnable",
    ),
    ("aiagentsforce_core", "runnables", "passthrough", "RunnablePassthrough"): (
        "aiagentsforce_core",
        "runnables",
        "passthrough",
        "RunnablePassthrough",
    ),
    ("aiagentsforce_core", "runnables", "base", "RunnableSequence"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableSequence",
    ),
    ("aiagentsforce_core", "runnables", "base", "RunnableEach"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableEach",
    ),
    ("aiagentsforce_core", "runnables", "base", "RunnableEachBase"): (
        "aiagentsforce_core",
        "runnables",
        "base",
        "RunnableEachBase",
    ),
    (
        "aiagentsforce_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ): (
        "aiagentsforce_core",
        "runnables",
        "configurable",
        "RunnableConfigurableAlternatives",
    ),
    ("aiagentsforce_core", "runnables", "configurable", "RunnableConfigurableFields"): (
        "aiagentsforce_core",
        "runnables",
        "configurable",
        "RunnableConfigurableFields",
    ),
    ("aiagentsforce_core", "runnables", "history", "RunnableWithMessageHistory"): (
        "aiagentsforce_core",
        "runnables",
        "history",
        "RunnableWithMessageHistory",
    ),
    ("aiagentsforce_core", "runnables", "passthrough", "RunnableAssign"): (
        "aiagentsforce_core",
        "runnables",
        "passthrough",
        "RunnableAssign",
    ),
    ("aiagentsforce_core", "runnables", "retry", "RunnableRetry"): (
        "aiagentsforce_core",
        "runnables",
        "retry",
        "RunnableRetry",
    ),
}

_JS_SERIALIZABLE_MAPPING: dict[tuple[str, ...], tuple[str, ...]] = {
    ("aiagentsforce_core", "messages", "AIMessage"): (
        "aiagentsforce_core",
        "messages",
        "ai",
        "AIMessage",
    ),
    ("aiagentsforce_core", "messages", "AIMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "ai",
        "AIMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "BaseMessage"): (
        "aiagentsforce_core",
        "messages",
        "base",
        "BaseMessage",
    ),
    ("aiagentsforce_core", "messages", "BaseMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "base",
        "BaseMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "ChatMessage"): (
        "aiagentsforce_core",
        "messages",
        "chat",
        "ChatMessage",
    ),
    ("aiagentsforce_core", "messages", "ChatMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "chat",
        "ChatMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "FunctionMessage"): (
        "aiagentsforce_core",
        "messages",
        "function",
        "FunctionMessage",
    ),
    ("aiagentsforce_core", "messages", "FunctionMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "function",
        "FunctionMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "HumanMessage"): (
        "aiagentsforce_core",
        "messages",
        "human",
        "HumanMessage",
    ),
    ("aiagentsforce_core", "messages", "HumanMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "human",
        "HumanMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "SystemMessage"): (
        "aiagentsforce_core",
        "messages",
        "system",
        "SystemMessage",
    ),
    ("aiagentsforce_core", "messages", "SystemMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "system",
        "SystemMessageChunk",
    ),
    ("aiagentsforce_core", "messages", "ToolMessage"): (
        "aiagentsforce_core",
        "messages",
        "tool",
        "ToolMessage",
    ),
    ("aiagentsforce_core", "messages", "ToolMessageChunk"): (
        "aiagentsforce_core",
        "messages",
        "tool",
        "ToolMessageChunk",
    ),
    ("aiagentsforce_core", "prompts", "image", "ImagePromptTemplate"): (
        "aiagentsforce_core",
        "prompts",
        "image",
        "ImagePromptTemplate",
    ),
    ("langchain", "chat_models", "bedrock", "ChatBedrock"): (
        "langchain_aws",
        "chat_models",
        "ChatBedrock",
    ),
    ("langchain", "chat_models", "google_genai", "ChatGoogleGenerativeAI"): (
        "langchain_google_genai",
        "chat_models",
        "ChatGoogleGenerativeAI",
    ),
    ("langchain", "chat_models", "groq", "ChatGroq"): (
        "langchain_groq",
        "chat_models",
        "ChatGroq",
    ),
    ("langchain", "chat_models", "bedrock", "BedrockChat"): (
        "langchain_aws",
        "chat_models",
        "ChatBedrock",
    ),
}
