# Architecture

This voice-agent scaffold is built like a forward-deployed system rather than a toy chatbot:

- ingest a caller transcript
- classify intent and confidence
- decide whether to answer, clarify, fallback, or hand off
- call a bounded set of enterprise tools
- write a trace that can be reviewed later

The deployment-minded pieces are the point:

- action gating before tool use
- explicit handoff path
- operator-visible traces
- room for STT/TTS replacement without changing the control loop
