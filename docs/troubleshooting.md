# Troubleshooting
- Import errors: activate the virtual environment and install requirements from repo root.
- API validation error: inspect Pydantic response details and request schema.
- Agent loops: enforce step/deadline budgets and inspect terminal-state transitions.
- Duplicate side effects: use idempotency keys and reconcile uncertain outcomes.
- Unexpected tool access: audit allowlists and backend authorization checks.
- RAG leakage: apply tenant filters before retrieved content enters model context.
