# Security and safety
Threats include direct/indirect prompt injection, malicious retrieved content, tool abuse, SSRF, data exfiltration, cross-tenant leakage, insecure secrets, excessive agency, replay, and denial of service.

Controls: treat user/retrieved/tool text as untrusted; enforce authorization in backend code; use least-privilege tools, allowlists, egress controls, and sandboxing; keep secrets out of prompts/logs; bound runtime, steps, payloads, and spend; require approval for high-impact actions; continuously test tenant isolation and injection.
