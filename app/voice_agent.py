#!/usr/bin/env python3
"""Mock enterprise support voice-agent control loop."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path


@dataclass
class AgentTrace:
    transcript: str
    intent: str
    confidence: float
    action: str
    resolution: str


class VoiceSupportAgent:
    def __init__(self, tool_data_path: str) -> None:
        self.tool_data = json.loads(Path(tool_data_path).read_text())

    def classify(self, transcript: str) -> tuple[str, float]:
        lowered = transcript.lower()
        if "refund" in lowered:
            return "billing_refund", 0.93
        if "locked" in lowered or "verify" in lowered:
            return "account_access", 0.74
        return "general_support", 0.61

    def run(self, transcript: str) -> AgentTrace:
        intent, confidence = self.classify(transcript)
        if confidence < 0.65:
            return AgentTrace(transcript, intent, confidence, "clarify", "Asked caller for more detail.")

        tool_result = self.tool_data.get(intent)
        if not tool_result:
            return AgentTrace(transcript, intent, confidence, "fallback", "Explained that live support will take over.")

        if tool_result.get("requires_handoff"):
            return AgentTrace(transcript, intent, confidence, "handoff", tool_result["message"])

        return AgentTrace(transcript, intent, confidence, "resolve", tool_result["message"])


def format_trace(trace: AgentTrace) -> str:
    return json.dumps(asdict(trace), indent=2)
