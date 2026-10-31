import pytest
from labs.tool_policy import validate_tool_name

def test_allowlisted_tool():
    assert validate_tool_name("search_public_docs") == "search_public_docs"

def test_unlisted_tool_denied():
    with pytest.raises(PermissionError):
        validate_tool_name("run_shell")
