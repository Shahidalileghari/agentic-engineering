# Agentic AI foundations
An agentic system uses a model to choose among actions or steps toward a goal, typically through tools and a control loop. An LLM alone is not automatically an agent.

Conceptual loop: receive goal/context -> propose answer or action -> validate proposal in application code -> authorize -> execute bounded action -> observe result -> stop, ask approval, or continue within limits.

Choose a deterministic workflow when steps are predictable. Use an agent when decisions genuinely depend on variable context. More autonomy increases complexity and risk; it is not inherently better.
