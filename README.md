# forward-deployed-voice-agent

An enterprise support voice agent that optimizes for operational reality: `tool-calling`, `voice agents`, escalation, traces, fallbacks, and a clear `forward deployed` story.

## Problem

Many voice-agent demos work only when the user speaks clearly, the backend is healthy, and the request fits one happy path. This repo is intentionally about what happens when those conditions fail.

## What This Repo Proves

- you can model a support workflow as a control loop instead of a single prompt
- you can route across tools, fallback states, and human handoff
- you think about latency budget, interruption handling, and observability up front

## Repo Layout

- `app/voice_agent.py`: orchestration loop and state machine
- `docs/architecture.md`: system design and deployment notes
- `docs/runbook.md`: operator playbook
- `docs/latency_budget.md`: user-facing responsiveness targets
- `scripts/demo_session.py`: run a mocked session locally
- `data/mock_tool_results.json`: synthetic backend data
- `traces/sample_trace.json`: example execution trace

## Demo Flow

1. caller describes an issue
2. agent classifies intent and confidence
3. tool call executes against mocked support systems
4. agent either answers, asks a clarifying question, or escalates
5. trace is written for debugging and review

## Run

```bash
python3 scripts/demo_session.py --input "My refund is stuck and the bot said my account is locked."
```

## Failure and Fallback Paths

- low ASR confidence triggers clarification
- missing tool data triggers a bounded fallback response
- policy-risk or repeated failure triggers human handoff
- long latency triggers a brief progress utterance before the next step
