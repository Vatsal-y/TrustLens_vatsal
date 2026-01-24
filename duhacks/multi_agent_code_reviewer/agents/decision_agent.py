"""
Decision Agent
Recommends actions based on findings from expert agents.
Interprets data but does not determine trust.
"""

from typing import Dict, Any, List, Tuple
from .base_agent import BaseAgent
from schemas.agent_output import AgentOutput, AgentType, RiskLevel


class DecisionAgent(BaseAgent):
    """
    Synthesizes expert findings into a recommended action.
    Strictly follows risk-priority hierarchy and safety penalties.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(AgentType.DECISION, config)
    
    def _validate_config(self) -> None:
        pass
    
    def analyze(self, **kwargs) -> AgentOutput:
        """Required by BaseAgent interface but not used."""
        raise NotImplementedError("Use recommend_action instead")
    
    def recommend_action(
        self,
        agent_outputs: List[AgentOutput],
        overall_confidence: float,
        conflicts: List[Any]
    ) -> AgentOutput:
        """
        Synthesize recommendation and calculate decision confidence.
        """
        try:
            # Filter successful outputs
            success_outputs = [o for o in agent_outputs if o.success]
            
            # 1. Determine Highest Risk Level
            max_risk = RiskLevel.NONE
            if success_outputs:
                max_risk = max(o.risk_level for o in success_outputs)
            
            # 2. Map Risk to Action
            recommendation = self._map_risk_to_action(max_risk)
            reasoning = f"Highest detected risk: {max_risk.value}"
            
            # 3. Critical Risk Safety Rule
            # If CRITICAL risk exists and overall_confidence < 0.80, force DEFER
            if max_risk == RiskLevel.CRITICAL and overall_confidence < 0.80:
                recommendation = "defer"
                reasoning = f"Critical risk detected but overall confidence ({overall_confidence:.2f}) is below 0.80 safety threshold."
            
            # 4. Calculate Decision Confidence (with conflict penalties)
            decision_confidence = self._calculate_decision_confidence(overall_confidence, conflicts)
            
            # 5. Generate reasoning string
            confidence_reasoning = self._generate_reasoning(
                len(agent_outputs) - len(success_outputs), 
                len(conflicts),
                overall_confidence,
                decision_confidence
            )
            
            return self._create_output(
                confidence=decision_confidence,
                findings=[{
                    "recommendation": recommendation,
                    "reasoning": reasoning,
                    "max_risk": max_risk.value
                }],
                risk_level=max_risk,
                metadata={
                    "analysis_confidence": overall_confidence,
                    "decision_confidence": decision_confidence,
                    "recommendation": recommendation,
                    "confidence_reasoning": confidence_reasoning,
                    "conflicts_count": len(conflicts)
                }
            )
        except Exception as e:
            return self._create_output(
                confidence=0.0,
                findings=[],
                risk_level=RiskLevel.NONE,
                metadata={},
                success=False,
                error_message=str(e)
            )

    def _map_risk_to_action(self, risk: RiskLevel) -> str:
        """Map RiskLevel to Action Recommendation per PRD."""
        mapping = {
            RiskLevel.CRITICAL: "manual_review_required",
            RiskLevel.HIGH: "review_required",
            RiskLevel.MEDIUM: "proceed_with_caution",
            RiskLevel.LOW: "acceptable",
            RiskLevel.NONE: "acceptable"
        }
        return mapping.get(risk, "unknown")

    def _calculate_decision_confidence(self, overall_confidence: float, conflicts: List[Any]) -> float:
        """
        Apply conflict penalties to overall confidence.
        Penalty = 0.2 * disagreement_level per conflict, capped at 0.5.
        """
        penalty = 0.0
        for conflict in conflicts:
            # Safely handle conflict objects (assuming they have disagreement_level)
            disagreement = getattr(conflict, "disagreement_level", 1.0)
            penalty += 0.2 * disagreement
            
        penalty = min(penalty, 0.5)
        decision_confidence = max(0.0, overall_confidence - penalty)
        
        # Ensure it never exceeds overall_confidence
        return min(decision_confidence, overall_confidence)

    def _generate_reasoning(self, failed_count: int, conflict_count: int, analytic_conf: float, final_conf: float) -> str:
        """Generate human-readable confidence reasoning."""
        points = []
        if failed_count > 0:
            points.append(f"{failed_count} agent(s) failed")
        if conflict_count > 0:
            points.append(f"{conflict_count} conflict(s) reduced certainty")
        if analytic_conf < 0.85:
            points.append("moderate analytic confidence")
        
        if not points:
            return "High trust integration with full agent consensus."
            
        return " ".join(points).capitalize() + "."
