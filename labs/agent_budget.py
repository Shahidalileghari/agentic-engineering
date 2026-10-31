from dataclasses import dataclass

@dataclass(frozen=True)
class RunBudget:
    max_steps: int = 8
    max_tool_calls: int = 5
    max_output_chars: int = 4000

    def __post_init__(self):
        if self.max_steps < 1 or self.max_tool_calls < 0 or self.max_output_chars < 1:
            raise ValueError("invalid run budget")

def within_budget(steps: int, tool_calls: int, output: str, budget: RunBudget) -> bool:
    return (0 <= steps <= budget.max_steps
            and 0 <= tool_calls <= budget.max_tool_calls
            and len(output) <= budget.max_output_chars)
