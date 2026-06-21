# VBPM-Core: Value-Based Personality Model (Prototype)

**A minimal computational model of value‑based action selection**

---

## 📘 Overview

VBPM (Value-Based Personality Model) is a **minimal, computational framework**  
that models personality as:

**Value Dimensions × Weights → Internal Consistency → Action Selection**

This repository provides:

- A **clean, minimal implementation** of the VBPM model  
- A **demonstration** using a “baby personality” example  
- The **full research paper** describing the theoretical foundation  

The goal of VBPM-Core is not to simulate full human personality,  
but to provide a **simple and extensible starting point**  
for exploring value‑based behavior modeling.

---

## 🧠 Core Idea

VBPM assumes that:

- Individuals hold **multiple value dimensions** (e.g., safety, novelty, comfort)  
- Each value has an associated **weight**  
- Actions are evaluated by **internal consistency**:

$$
Consistency(a) = \sum_i w_i \cdot V_i(a)
$$

- The selected action is the one that maximizes this value‑weighted score:

$$
a^\star = \arg\max_a Consistency(a)
$$

This minimal structure allows VBPM to reproduce  
**value‑consistent action selection** in a transparent and interpretable way.

---

## 👶 Demonstration: Baby Personality

The prototype includes a simple demonstration using a “baby personality”:

- High weight on **safety** and **comfort**  
- Moderate weight on **novelty** and **sociality**  
- Low weight on **autonomy**

Two scenarios are evaluated:

- Reaching for a colorful toy  
- Staying close to the parent  

The model computes internal consistency for each scenario  
and selects the action most aligned with the given value priorities.

Run the demo:

```bash
python prototype/baby_personality.py
```

You can modify:

- `prototype/values.json`  
- `prototype/scenarios.json`  

to observe how behavior changes with different value structures.

---

## 📁 Repository Structure

```
VBPM-Core/
├── README.md
├── LICENSE
├── docs/
│   └── paper.pdf          # Full research paper
└── prototype/
    ├── baby_personality.py
    ├── scenarios.json
    └── values.json
```

---

## 🔬 Scope of This Repository

This repository intentionally focuses on the **minimal theoretical core**:

- No learning mechanisms  
- No perception model  
- No multi-agent interaction  
- No LLM integration  

These are discussed as **future directions** in the paper,  
but are outside the scope of this prototype.

VBPM-Core is designed to be:

- **Simple**  
- **Transparent**  
- **Extensible**  

A foundation for researchers exploring value‑based behavior modeling.

---

## 📄 Paper

The full VBPM-Core research paper is available here:

👉 `docs/paper/paper.pdf`

---

## 📚 Citation

SwayMagpie (2026). *VBPM-Core: Value-Based Personality Model (Prototype).*  
GitHub: [https://github.com/SwayMagpie/VBPM-Core](https://github.com/SwayMagpie/VBPM-Core)

---

## 📄 License

- **Code (prototype/)** — MIT License  
- **Paper & Documentation (docs/)** — CC BY‑SA 4.0  

See each directory for details.

---

## ❤️ Support the Research

VBPM-Core is the **first step** in a broader exploration of  
value‑based personality modeling.

This repository provides the minimal theoretical core.  
Future directions—such as perception‑driven evaluation functions,  
value–perception interaction models, and multi‑agent simulations—  
require significantly more computational resources.

If this framework contributes to your research,  
or if you would like to support the next stage of development,  
you can do so through **GitHub Sponsors**.

Your support helps fund the GPU resources needed  
to explore more advanced versions of this model.

I make no promises for support,  
but every contribution helps move the research forward.

---
