# baby_personality.py
# Minimal prototype for a Value-Based Personality Model (VBPM)
# "Baby personality" with simple value dimensions and fixed weights.

from dataclasses import dataclass
from typing import Dict, List


# -----------------------------
# Core data structures
# -----------------------------

ValueName = str
ScenarioId = str


@dataclass
class Personality:
    """Value-based personality: value weights define 'who this is'."""
    name: str
    values: Dict[ValueName, float]  # e.g. {"safety": 0.9, "comfort": 0.8, ...}


@dataclass
class Scenario:
    """A situation evaluated along value dimensions."""
    id: ScenarioId
    description: str
    scores: Dict[ValueName, float]  # e.g. {"safety": 0.2, "comfort": 0.3, ...}

# -----------------------------
# JSON Loading (optional)
# -----------------------------
from pathlib import Path

def load_values(path: str | None = None) -> dict[str, float]:
    if path is None:
        # baby_personality.py と同じディレクトリの values.json を見る
        path = Path(__file__).parent / "values.json"
    else:
        path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        import json
        data = json.load(f)
    return dict(data)

def load_scenarios(path=None) -> list[Scenario]:
    if path is None:
        path = Path(__file__).parent / "scenarios.json"
    else:
        path = Path(path)

    import json
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    scenarios = []
    for item in data:
        scenarios.append(
            Scenario(
                id=item["id"],
                description=item["description"],
                scores=item["scores"]
            )
        )
    return scenarios

# -----------------------------
# Model definition
# -----------------------------

def create_baby_personality() -> Personality:
    """
    Baby personality:
    - Strong bias toward safety and comfort
    - Curious (novelty) but not very autonomous
    """
    values = load_values()
    return Personality(name="baby", values=values)


def create_sample_scenarios() -> List[Scenario]:
    """
    Two simple situations:
    - S1: A stranger approaches
    - S2: Mother picks up the baby
    """
    scenarios = load_scenarios()
    return scenarios


# -----------------------------
# Evaluation logic
# -----------------------------

def evaluate_scenario(personality: Personality, scenario: Scenario) -> float:
    """
    Utility(a) = sum_v weight(v) * score(v, a)
    Missing dimensions default to 0.0.
    """
    total = 0.0
    for v, w in personality.values.items():
        s = scenario.scores.get(v, 0.0)
        total += w * s
    return total


def choose_best_scenario(personality: Personality, scenarios: List[Scenario]) -> Scenario:
    scored = [(sc, evaluate_scenario(personality, sc)) for sc in scenarios]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0]


# -----------------------------
# Demo
# -----------------------------

def main() -> None:
    baby = create_baby_personality()
    scenarios = create_sample_scenarios()

    print(f"Personality: {baby.name}")
    print("Value weights:")
    for v, w in baby.values.items():
        print(f"  {v}: {w}")
    print()

    print("Scenarios and utilities:")
    utilities: Dict[ScenarioId, float] = {}
    for sc in scenarios:
        u = evaluate_scenario(baby, sc)
        utilities[sc.id] = u
        print(f"  {sc.id}: {sc.description} => {u:.3f}")
    print()

    best = choose_best_scenario(baby, scenarios)
    print("Selected scenario:")
    print(f"  {best.id}: {best.description}")


if __name__ == "__main__":
    main()
