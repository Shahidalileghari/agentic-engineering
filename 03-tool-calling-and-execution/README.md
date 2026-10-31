# Tool calling and execution
Tool calling is a proposal mechanism—not permission. Define narrow tools with typed arguments, allowlisted operations, timeouts, and bounded results. The application must authenticate the caller, authorize the action, validate arguments, execute safely, and audit outcomes.

Safer sequence: model proposal -> schema validation -> identity/authorization -> policy checks -> approval if needed -> bounded execution -> sanitized result.

Avoid unrestricted shell, filesystem, SQL, or browser tools in production agents.
