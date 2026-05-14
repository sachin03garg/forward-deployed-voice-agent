#!/usr/bin/env python3
"""Run a mocked voice-agent session and print the resulting trace."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.voice_agent import VoiceSupportAgent, format_trace


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Caller transcript for the mock session.")
    args = parser.parse_args()

    agent = VoiceSupportAgent(str(ROOT / "data" / "mock_tool_results.json"))
    trace = agent.run(args.input)
    print(format_trace(trace))


if __name__ == "__main__":
    main()
