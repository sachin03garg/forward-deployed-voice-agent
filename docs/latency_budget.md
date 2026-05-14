# Latency Budget

Target user experience for a support voice flow:

- initial acknowledgement within 300 ms
- intent classification within 800 ms
- tool-routing decision within 1200 ms
- final answer or handoff statement within 2500 ms for common paths

Design implications:

- short progress utterances when tool calls are slow
- prefer bounded tool fanout over parallel "try everything" behavior
- log per-step timing to make regressions visible
