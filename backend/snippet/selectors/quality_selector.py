from typing import List, Dict, Any
from snippet.ir.code_block import CodeBlock

class QualitySelector:
    """
    Computes quality metrics from code blocks.
    does NOT return snippets, only metrics.
    """

    def compute_metrics(self, blocks: List[CodeBlock]) -> Dict[str, Any]:
        """
        Compute aggregation metrics for the file.
        
        Metrics:
        - loc (lines of code)
        - avg_function_length
        - max_function_length
        - avg_complexity
        - max_complexity
        - function_count
        - class_count
        - max_nesting_depth
        """
        functions = [b for b in blocks if b.type == "function"]
        classes = [b for b in blocks if b.type == "class"]
        
        # Calculate total LOC and max nesting depth
        total_loc = 0
        max_nesting_depth = 0
        for block in blocks:
            total_loc += block.length()
            # Assume complexity is a proxy for nesting depth
            max_nesting_depth = max(max_nesting_depth, min(block.complexity, 10))
        
        if not functions:
            return {
                "loc": total_loc,
                "avg_function_length": 0,
                "max_function_length": 0,
                "avg_complexity": 0,
                "max_complexity": 0,
                "function_count": 0,
                "class_count": len(classes),
                "max_nesting_depth": max_nesting_depth
            }
            
        # Length metrics
        lengths = [f.length() for f in functions]
        max_len = max(lengths) if lengths else 0
        avg_len = sum(lengths) / len(lengths) if lengths else 0
        
        # Complexity metrics
        complexities = [f.complexity for f in functions]
        max_comp = max(complexities) if complexities else 0
        avg_comp = sum(complexities) / len(complexities) if complexities else 0
        
        return {
            "loc": total_loc,
            "avg_function_length": round(avg_len, 2),
            "max_function_length": max_len,
            "avg_complexity": round(avg_comp, 2),
            "max_complexity": max_comp,
            "function_count": len(functions),
            "class_count": len(classes),
            "max_nesting_depth": max_nesting_depth
        }
