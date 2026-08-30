# NeuroPerm AI: Blood-Brain Barrier (BBB) Permeability Predictor

An autonomous cheminformatics agent running on the **TrueForge** agent harness and powered by **Google Gemini**, grounded on the **B3DB (Blood-Brain Barrier Database)** benchmark dataset.

## Problem Statement
Predicting Blood-Brain Barrier (BBB) penetration is a major bottleneck in Central Nervous System (CNS) drug discovery. NeuroPerm AI automates early-stage molecular screening by analyzing physicochemical constraints and cross-referencing candidates against curated experimental data.

## Architecture & Tech Stack
- **Agent Harness:** TrueForge (TrueFoundry runtime managing model calls, context, and execution safety)
- **AI Model:** Google Gemini (`gemini-3-6-flash`) via Google AI Studio
- **Domain Grounding:** B3DB Benchmark Dataset (7,800+ curated molecules)
- **Evaluation Pipeline:** Dual-layer classification combining experimental dataset queries (`b3db_tool.py`) with de novo physicochemical property heuristics (MW, LogP/LogD, TPSA, HBD, HBA, Efflux liability).

## Qodo Code Review Evidence
- **Merged Pull Request:** [Insert Merged PR URL here]
- **Review Summary:** Qodo analyzed the repository structure, verified tool script modularity (`b3db_tool.py`), and validated agent harness instructions before merging into main.

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/biplab349/BBBP-B3DB-Agent.git](https://github.com/biplab349/BBBP-B3DB-Agent.git)
   cd BBBP-B3DB-Agent
