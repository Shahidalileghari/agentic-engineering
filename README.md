# Agentic AI Engineering 

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
- 
## Engineering principles
1. Prefer deterministic workflows when steps are known.
2. Treat model output as an untrusted proposal, never authorization.
3. Enforce identity and permissions in application code.
4. Use least-privilege tools with typed schemas and allowlists.
5. Bound steps, time, tokens, tool calls, retries, and spend.
6. Require human approval for consequential actions.
7. Keep audit trails while minimizing sensitive data in logs.
8. Test adversarial inputs, failure paths, and tenant isolation.
