"""Style-pass dispatch (impl §11.5): run style modules, validate completion
contracts, record divergence from the general route.

V4 divergence resolution (v6 §II.4.4):
- style + general agree → record agreement, proceed
- disagree → branch-completeness + calibration on both, record, verify before select
- style contract fails → general route governs; failure is a curriculum item
"""

from typing import Any

from thinking_agent.domain.alternatives import StylePassResult
from thinking_agent.styles.contract_validator import ContractValidator, contract_for
from thinking_agent.styles.registry import StyleRegistry


class StyleModuleRunner:
    def __init__(self, registry: StyleRegistry, validator: ContractValidator | None = None):
        self.registry = registry
        self.validator = validator or ContractValidator()

    def run_passes(
        self,
        style_ids: list[str],
        state: dict[str, Any],
        ctx: Any,
        budget_per_pass: int = 2,
    ) -> list[StylePassResult]:
        """Runs each style as a first-class pass through the model adapter.
        Mock adapters script StylePassResult per scenario; live adapters get
        the style's contract in the prompt."""
        results: list[StylePassResult] = []
        model = ctx.models.get("style_pass") or ctx.models.get("main")
        for style_id in style_ids:
            style = self.registry.get(style_id)
            if style is None:
                continue
            contract = contract_for(style.id, style.name, style.strengths, style.weaknesses)
            try:
                result: StylePassResult = model.invoke_structured(
                    StylePassResult,
                    _pass_messages(state, style_id, contract),
                )
            except RuntimeError:
                # no script for this style → recorded incomplete pass
                result = StylePassResult(
                    style_id=style_id, style_name=style.name,
                    claims=[], contract_met=False,
                    contract_gaps=list(contract.get("outputs", [])),
                )
            result = self.validator.validate(result, contract)
            results.append(result)
        return results

    def divergence(self, style_results: list[StylePassResult],
                   general_summary: str) -> dict[str, Any]:
        """Style vs general route resolution (impl §11.5)."""
        agreed = all(
            (r.summary or "").strip() == general_summary.strip() or not r.summary
            for r in style_results
        )
        return {
            "agreed": agreed,
            "resolution": ("agreement recorded" if agreed
                           else "disagreement recorded; selection deferred to verification"),
            "curriculum_items": [
                f"{r.style_id}: incomplete contract {r.contract_gaps}"
                for r in style_results if not r.contract_met
            ],
        }


def _pass_messages(state: dict[str, Any], style_id: str, contract: dict[str, object]) -> list[dict]:
    content = {
        "scenario": ((state.get("request") or {}).get("task_metadata") or {}).get("scenario", "default"),
        "role": "style_pass",
        "style_id": style_id,
        "contract": contract,
        "required_outputs": list(contract.get("outputs", [])),
        "frame": state.get("frame") or {},
    }
    return [
        {"role": "system",
         "content": "You are executing one thinking-style pass. Produce its "
                    "completion-contract outputs as claims."},
        {"role": "user", "content": repr(content)},
    ]
