from pydantic import BaseModel, Field

class AgentRunRequest(BaseModel):
    goal: str = Field(min_length=1, max_length=500)

class AgentRunResponse(BaseModel):
    status: str
    steps_used: int
    result: str
    simulated: bool = True
