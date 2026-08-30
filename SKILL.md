---
name: search_b3db
description: Queries the local B3DB dataset to retrieve experimental Blood-Brain Barrier (BBB) permeability classification, logBB values, and compound metadata.
---

# search_b3db Skill

Use this skill to search the B3DB benchmark dataset (`B3DB_classification.tsv`) via `b3db_tool.py` for experimental BBB status, logBB values, and molecular metadata.

## Input Parameters
- `query` (string): The chemical compound name or SMILES string.

## Output
- `found` (boolean): Whether the compound was present in experimental records.
- `BBB_class` (string): Experimental classification (`BBB+` or `BBB-`).
- `logBB` (string/number): Brain-to-plasma partition coefficient.
