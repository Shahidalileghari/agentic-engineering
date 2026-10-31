import pytest
from labs.agent_budget import RunBudget, within_budget

def test_within_budget():
    assert within_budget(3, 2, "ok", RunBudget())

def test_step_limit():
    assert not within_budget(9, 1, "ok", RunBudget())

def test_tool_limit():
    assert not within_budget(2, 6, "ok", RunBudget())

def test_invalid_budget():
    with pytest.raises(ValueError):
        RunBudget(max_steps=0)
