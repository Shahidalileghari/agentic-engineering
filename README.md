# Agentic AI Engineering Mastery

A practical, engineering-first curriculum for designing, building, evaluating, securing, and operating agentic AI systems—from fundamentals to production architecture.

**Stack:** Python 3.11+, FastAPI, Pydantic, pytest. Provider SDKs and orchestration frameworks are optional extensions.

## Learning outcomes
- Understand agentic systems and when not to use an agent.
- Build typed tool-calling interfaces and safe execution boundaries.
- Design state, memory, context, planning, and control loops.
- Compare workflows, graphs, single-agent, and multi-agent architectures.
- Implement retrieval-grounded agents and human approval.
- Evaluate task success, tool use, safety, latency, and cost.
- Secure agents against prompt injection, tool abuse, data leakage, and runaway execution.
- Deploy with observability, budgets, resilience, and rollback.

## Curriculum
00 Setup and roadmap; 01 Agentic foundations; 02 LLM interfaces and structured output; 03 Tool calling and execution; 04 State, memory, and context; 05 Planning and control loops; 06 Workflows and orchestration; 07 RAG and knowledge agents; 08 Multi-agent systems; 09 Human-in-the-loop; 10 Evaluation and observability; 11 Security and safety; 12 Production operations; 13 Portfolio projects.

## Quick start
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest
uvicorn examples.api.main:app --reload
```
Open `http://127.0.0.1:8000/docs`. The included API is a deterministic simulation: it does not call an LLM or execute external tools.

## Engineering principles
1. Prefer deterministic workflows when steps are known.
2. Treat model output as an untrusted proposal, never authorization.
3. Enforce identity and permissions in application code.
4. Use least-privilege tools with typed schemas and allowlists.
5. Bound steps, time, tokens, tool calls, retries, and spend.
6. Require human approval for consequential actions.
7. Keep audit trails while minimizing sensitive data in logs.
8. Test adversarial inputs, failure paths, and tenant isolation.

No model weights, provider credentials, or paid integrations are included. Review official documentation and licenses before production use.
