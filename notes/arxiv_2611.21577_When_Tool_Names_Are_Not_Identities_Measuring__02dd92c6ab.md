---
title: 'When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based
  AI Agents'
type: arxiv
source: https://arxiv.org/abs/2611.21577
canonical_url: https://arxiv.org/abs/2611.21577
captured_by: auto-scanner
date: '2026-11-17'
captured_at: '2026-11-17T14:04:00+00:00'
last_requested: '2026-11-17T14:04:00+00:00'
issue: scan:mlip-development-arxiv
status: to-read
authors:
- Zeynab Anbiaee
- Sajjad Dadkhah
- Ali A. Ghorbani
published: '2026-11-16'
abstract: 'Large language model (LLM) applications increasingly act as agents that
  select and invoke external tools. The Model Context Protocol (MCP) standardizes
  this interaction by allowing clients to compose tools advertised by multiple servers.
  However, tool metadata used for discovery and selection is not, by itself, necessarily
  bound to a verified provider identity. This paper studies this gap as tool-provider
  misbinding: a failure in which a request intended for a legitimate provider is instead
  resolved to an attacker-controlled tool. The attacker does not compromise the host,
  LLM, legitimate server, or network channel; it only operates another MCP server
  that advertises tools with chosen metadata. We formulate tool provider misbinding
  as an attacker-controlled tool-selection optimization problem and evaluate it in
  a controlled MCP environment across five LLM-based clients. The results show that
  interactions drive misbinding. The strongest failures occur when exact-name collision,
  task-aligned description, and compatible schema reinforce one another, but authority-enhanced
  descriptions with compatible schema can also cause wrong-provider execution or unresolved
  provider ambiguity without name collision. Different models expose the same provider-binding
  weakness differently, including attacker-controlled provider selection, clarification
  requests, and unstable or inconsistent provider resolution.'
metadata_provider: arXiv
metadata_status: complete
provider_data:
  arxiv_id: '2611.21577'
  categories:
  - cs.CR
  - cs.AI
---

# When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents

- **Type:** arxiv
- **Source:** https://arxiv.org/abs/2611.21577
- **Captured by:** @auto-scanner
- **Metadata:** complete (arXiv)
- **Authors:** Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani
- **Published:** 2026-11-16

## Summary
Large language model (LLM) applications increasingly act as agents that select and invoke external tools. The Model Context Protocol (MCP) standardizes this interaction by allowing clients to compose tools advertised by multiple servers. However, tool metadata used for discovery and selection is not, by itself, necessarily bound to a verified provider identity. This paper studies this gap as tool-provider misbinding: a failure in which a request intended for a legitimate provider is instead resolved to an attacker-controlled tool. The attacker does not compromise the host, LLM, legitimate server, or network channel; it only operates another MCP server that advertises tools with chosen metadata. We formulate tool provider misbinding as an attacker-controlled tool-selection optimization problem and evaluate it in a controlled MCP environment across five LLM-based clients. The results show that interactions drive misbinding. The strongest failures occur when exact-name collision, task-aligned description, and compatible schema reinforce one another, but authority-enhanced descriptions with compatible schema can also cause wrong-provider execution or unresolved provider ambiguity without name collision. Different models expose the same provider-binding weakness differently, including attacker-controlled provider selection, clarification requests, and unstable or inconsistent provider resolution.

## Provider details
- **Arxiv Id:** 2611.21577
- **Categories:** ["cs.CR", "cs.AI"]
