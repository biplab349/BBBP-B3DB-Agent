"""
B3DB Query Tool for NeuroPerm AI Agent
Cross-references candidate molecules against the B3DB benchmark dataset.
"""

import pandas as pd

def search_b3db(query: str, dataset_path: str = "B3DB_classification.tsv"):
    """
    Search the B3DB dataset by compound name or SMILES string.
    Returns experimental BBB status, logBB, and uncertainty group.
    """
    try:
        df = pd.read_csv(dataset_path, sep="\t")
        
        # Search by compound name or SMILES match
        matches = df[
            df['compound_name'].str.contains(query, case=False, na=False) |
            df['SMILES'].str.contains(query, case=False, na=False)
        ]
        
        if matches.empty:
            return {"status": "not_found", "message": "Molecule not in experimental B3DB dataset. Perform de novo heuristic prediction."}
            
        top_match = matches.iloc[0]
        return {
            "status": "found",
            "compound_name": top_match.get("compound_name", "N/A"),
            "SMILES": top_match.get("SMILES", "N/A"),
            "BBB_class": top_match.get("BBB+/BBB-", "Unknown"),
            "uncertainty_group": top_match.get("group", "Standard"),
            "source": "B3DB Benchmark Dataset"
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Quick test
    print(search_b3db("Caffeine"))
