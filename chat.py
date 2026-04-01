from langchain_core.messages import AIMessage, ToolMessage
from agent import build_agent

TOOL_ICONS = {
    "wikipedia_search": "📖 Wikipedia",
    "web_search":       "🔍 Web Search",
    "calculator":       "🧮 Calculator",
}

def print_tool_usage(response):
    for message in response["messages"]:
        if isinstance(message, AIMessage) and message.tool_calls:
            for tc in message.tool_calls:
                icon = TOOL_ICONS.get(tc["name"], f"🔧 {tc['name']}")
                print(f"  {icon} → {tc['args']}")
        if isinstance(message, ToolMessage):
            preview = message.content[:150].replace("\n", " ")
            print(f"  ↳ {preview}...")

def main():
    agent = build_agent()
    config = {"configurable": {"thread_id": "research-session"}}

    print("🤖 Research Agent ready! Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
        )

        print_tool_usage(response)
        print(f"Agent: {response['messages'][-1].content}\n")

if __name__ == "__main__":
    main()