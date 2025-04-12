from langchain.tools import tool

@tool
def simple_tool(query: str) -> str:
    """Simple tool that echoes a response."""
    return f"You asked: {query}"
