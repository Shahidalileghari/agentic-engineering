"""Illustrative allowlist only; production authorization needs caller identity and policy."""
ALLOWED_TOOLS = {"search_public_docs", "get_order_status"}

def validate_tool_name(name: str) -> str:
    if name not in ALLOWED_TOOLS:
        raise PermissionError(f"Tool is not allowlisted: {name}")
    return name
