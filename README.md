# VBPM-Core: Value-Based Personality Model (Prototype)
**A minimal implementation of a value‑based personality architecture**

---
## 🚀 The Mission: Externalizing Personality
I am exploring the frontier of computational personality.

This repository provides the core theoretical framework (VBPM) and a minimal prototype. Personality is often treated as a "black box" hidden within neural weights or vague traits. VBPM changes this by modeling personality as an externalizable, modular, and computable system of value-weight optimization.

---

## ⚡ Why I am sharing this (and why I need a GPU)
The current prototype is a static "toy" (Baby Model). To evolve this into a dynamic, learning agent capable of complex social interactions—essentially, to move from a "Baby" to an "Adult" architecture—I need to implement:

- Dynamic Weight Updating using Reward Prediction Error (RPE).

- LLM-Integrated Scoring for high-dimensional scenarios.

- Value Lifecycle Simulation (Integration/Dormancy).

My current local environment has hit its limit. To push these "toys" into the next stage of implementation, I am building a dedicated GPU rig.

If this theory sparks something in you, consider it an investment in the next phase of this research.

---

## 🔍 Overview
Value-Based Personality Model (VBPM) defines personality as:
Value Dimensions × Weights × Optimization

This repository provides:

- A minimal, runnable prototype (“Baby Personality”).

- A clear theoretical foundation (see docs/paper.md).

- An externalizable structure for AI, cognitive science, and behavioral modeling.

---

## 🧠 Core Idea: Personality as Optimization
VBPM treats personality as a multi-objective optimization system composed of:

- Value Dimensions: Evaluative axes derived from physical brain modules (e.g., Amygdala = Safety).

- Weights: Individual importance assigned to each value (The "DNA" of decision-making).

- Optimization: Selecting actions that maximize Internal Self-Consistency.

"Why do individuals choose different actions under the same circumstances? Because their internal 'Economy of Value' is weighted differently."


## 📁 Repository Structure
```
VBPM-Core/
├── README.md
├── LICENSE
├── docs/
│   └── paper.pdf     # Full paper (Markdonwn)
└── prototype/
    ├── baby_personality.py       # Minimal runnable prototype
    ├── scenarios.json            # Externalized scenarios
    └── values.json               # Externalized values

```

---

## 👶 Prototype: Baby Personality Model
This is a "Playable Proof-of-Concept." It isolates the core mechanism without the noise of complex LLMs.

- JSON-Driven: Personality weights and scenario scores are externalized.

- Predictable: Watch how a "Baby" chooses safety over novelty based on its weighted utility.

- Extensible: A foundation for researchers to test their own value-weight update rules.

```bash
python prototype/baby_personality.py
```

---

#### 🧪 Try It
You can modify value weights or scenario scores in `prototype/values.json`, `prototype/scenarios.json`
to observe how the decision function changes.

This prototype is intentionally minimal and designed for experimentation.

---

#### Example Output

Personality: baby
Value weights:
  safety: 0.9
  comfort: 0.8
  novelty: 0.6
  social: 0.4
  autonomy: 0.1

Scenarios and utilities:
  reach_for_toy: The baby reaches for a colorful toy. => 0.390
  stay_with_parent: The baby stays close to the parent. => 0.970

Selected scenario:
  stay_with_parent: The baby stays close to the parent.

---

## ⚠️ Status & Future Work
This repository is the minimal theoretical core.
The more advanced mechanisms—dynamic weight updates, hierarchical value networks, and LLM-scoring integrations—are currently in development and require the aforementioned computing power to be fully realized.

Current Repo Status: Maintenance mode / Feature-complete for the Prototype phase.

---

## 📄 License
MIT License

---

## 📄 Paper (PDF)
The full VBPM-Core theoretical paper is available here:
👉 docs/paper/paper.md
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19732788.svg)](https://doi.org/10.5281/zenodo.19732788)

---

## 📚 Citation

SwayMagpie (2026). VBPM-Core: Value-Based Personality Model (Prototype).
GitHub: https://github.com/SwayMagpie/VBPM-Core

---

## Support the Next Play
If this framework contributes to your research or you want to see the "Adult" version of this model, support my GPU fund via GitHub Sponsors.

I make no promises for support, but every contribution moves the "next game" closer to reality.

