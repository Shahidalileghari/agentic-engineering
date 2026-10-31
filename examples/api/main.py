from fastapi import FastAPI
from examples.api.schemas import AgentRunRequest, AgentRunResponse

app = FastAPI(title="Agentic AI Mastery Demo", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/run-demo", response_model=AgentRunResponse)
def run_demo(request: AgentRunRequest):
    # Deterministic simulation: no model call and no external tool execution.
    goal = request.goal.strip()
    return AgentRunResponse(
        status="completed",
        steps_used=1,
        result=f"Demo accepted the goal ({len(goal)} characters). "
               "A real system would validate and authorize each proposed action.",
    )
