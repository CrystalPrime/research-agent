from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.retrievers import WikipediaRetriever
from langchain.tools import tool

wiki_retriever = WikipediaRetriever(lang="en", load_max_docs=2)

@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for factual and encyclopedic knowledge about
    people, places, history, science, and concepts."""
    docs = wiki_retriever.invoke(query)
    if not docs:
        return "No results found on Wikipedia."
    results = []
    for doc in docs:
        title = doc.metadata.get("title", "")
        results.append(f"## {title}\n{doc.page_content[:1000]}")
    return "\n\n".join(results)

@tool
def web_search(query: str) -> str:
    """Search the web for current news, recent events, and up-to-date information."""
    return DuckDuckGoSearchRun().run(query)

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression. Input must be a valid Python
    math expression like '2 + 2' or '(15 * 4) / 2'."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

tools = [wikipedia_search, web_search, calculator]