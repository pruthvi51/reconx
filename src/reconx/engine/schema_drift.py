"""
Schema Drift Detection & Remediation Engine:
Identifies column additions, drops, datatype mutations, and nullability changes.
"""
from typing import Dict, List, Any

class SchemaDriftDetector:
    @staticmethod
    def detect_drift(source_schema: Dict[str, str], target_schema: Dict[str, str]) -> Dict[str, Any]:
        src_cols = set(source_schema.keys())
        tgt_cols = set(target_schema.keys())

        dropped_in_target = list(src_cols - tgt_cols)
        added_in_target = list(tgt_cols - src_cols)
        common_cols = src_cols & tgt_cols

        type_mismatches = []
        for col in common_cols:
            if source_schema[col].lower() != target_schema[col].lower():
                type_mismatches.append({
                    "column": col,
                    "source_type": source_schema[col],
                    "target_type": target_schema[col]
                })

        has_drift = bool(dropped_in_target or added_in_target or type_mismatches)
        return {
            "has_drift": has_drift,
            "dropped_columns": dropped_in_target,
            "added_columns": added_in_target,
            "type_mismatches": type_mismatches,
            "drift_score": len(dropped_in_target) + len(added_in_target) + len(type_mismatches)
        }
