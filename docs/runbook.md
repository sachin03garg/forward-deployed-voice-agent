# Runbook

## Operator checks

- confirm transcript capture is healthy
- inspect classification confidence
- inspect tool-result availability
- escalate if fallback rate spikes or handoff volume changes unexpectedly

## Common failure patterns

- repeated low-confidence transcripts: likely STT quality issue
- empty tool responses: dependency or schema drift
- too many handoffs: policy thresholds may be too strict
