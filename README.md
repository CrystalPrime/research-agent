# 🤖 Research Agent

A conversational research assistant built with LangChain and Groq. The agent autonomously selects the right tool based on your question — Wikipedia for encyclopedic knowledge, web search for current events, and a calculator for math.

## Features

- **Multi-tool agent** — automatically picks the best tool for each question
- **Conversation memory** — remembers context across multiple turns
- **Tool transparency** — shows which tool was used and why
- **Powered by Groq** — fast inference with Llama 3.3 70B

## Tools

| Tool | When it's used |
|------|---------------|
| 📖 Wikipedia | Facts, history, science, people, concepts |
| 🔍 Web Search (DuckDuckGo) | Current news and recent events |
| 🧮 Calculator | Math expressions |

## Project Structure

```
research-agent/
├── agent.py          # Agent setup and configuration
├── tools.py          # Tool definitions
├── chat.py           # Terminal chat interface
├── requirements.txt
└── .env.example
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/research-agent.git
cd research-agent
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your API key**
```bash
cp .env.example .env
# Add your Groq API key to .env
```

Get a free Groq API key at [console.groq.com](https://console.groq.com)

**4. Run**
```bash
python chat.py
```

## Example

```
You: Who is Nikola Tesla?
  📖 Wikipedia → {'query': 'Nikola Tesla'}
Agent: Nikola Tesla (1856–1943) was a Serbian-American inventor...

You: What happened in the news today?
  🔍 Web Search → {'query': 'latest news today'}
Agent: Here are today's top stories...

You: What's 1856 + 187?
  🧮 Calculator → {'expression': '1856 + 187'}
Agent: 2043
```

## Stack

- [LangChain](https://github.com/langchain-ai/langchain) — agent framework
- [Groq](https://groq.com) — LLM inference (Llama 3.3 70B)
- [LangGraph](https://github.com/langchain-ai/langgraph) — agent memory via MemorySaver
- [DuckDuckGo Search](https://pypi.org/project/duckduckgo-search/) — web search
- [Wikipedia](https://pypi.org/project/wikipedia/) — encyclopedic retrieval
