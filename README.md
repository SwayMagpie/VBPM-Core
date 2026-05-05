# VBPM-Core: Value-Based Personality Model (Prototype)
**A minimal implementation of a value‑based personality architecture**

## [Final Notice]
I want a GPU rig. In anticipation of some 'donations' to make that happen, I’m sharing a few 'toys' from my brain with you. Once I hit my goal and secure that extra computing power, I’m moving on to the next play. Until then, this repo stays as-is. Enjoy.

---

## 🔍 Overview
Value-Based Personality Model (VBPM) defines personality as:

Value Dimensions × Weights × Optimization

This repository provides:

- A minimal, runnable prototype

- A clear theoretical foundation (see docs/theory_overview_en.md)

- A simple “baby personality” model demonstrating the core mechanism

The goal is to present a unified, externalizable structure for personality that can be used in AI, cognitive science, behavioral modeling, and organizational design.

This repository is intended for researchers, developers, and theorists
interested in value-based cognitive architectures.

---

## 🧩 What is VBPM?
VBPM (Value-Based Personality Model) is a minimal theoretical framework that models personality as
a value-weight optimization system. It provides a unified structure for understanding decision-making
across AI, cognitive science, and behavioral modeling.

---

## 📘 Relationship to the Paper
This repository contains the minimal prototype described in the paper.
The PDF provides the full theoretical background, including:
- Value dimensions
- Weight update mechanisms
- Integration and dormancy
- Future extensions

The prototype implements only the static value-weight evaluation described in the paper.
Dynamic weight updates and higher-order mechanisms are not included.

---

## 🧠 Core Idea
VBPM treats personality as a multi-objective optimization system composed of:
1. Value Dimensions — axes for evaluating actions

2. Weights — importance assigned to each value

3. Decision Function — selects the action with the highest weighted utility

Full theoretical details are available in:

👉 docs/theory_overview_en.md

---

## 👶 Prototype: Baby Personality Model
This repository includes a minimal implementation using a “baby personality”:

- Few value dimensions

- Simple innate weights

- No LLM required

- Easy to extend with learning mechanisms

The prototype evaluates scenarios such as:

- “A stranger approaches”

- “Mother picks up the baby”

and selects the action with the highest utility.

---

## 📁 Repository Structure


```
VBPM-Core/
├── README.md                     # English (main)
├── LICENSE
├── docs/
│   ├── paper.pdf                 # Full paper (PDF)
│   ├── theory_overview.md        # Japanese theory overview
│   └── theory_overview_en.md     # English theory overview
└── prototype/
    ├── baby_personality.py       # Minimal runnable prototype
    ├── scenarios.json            # Externalized scenarios
    └── values.json               # Externalized values

```

---

## ▶️ Running the Prototype

```bash
python prototype/baby_personality.py
```

#### 🧪 Try It
You can modify value weights or scenario scores in `prototype/baby_personality.py`
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

## ⚠️ Notes
This repository provides only the theoretical core and a minimal prototype.
Further extensions — including spatial models, advanced behavior systems, or learning mechanisms — are private and will not be published.

Weight‑update algorithms, LLM-based scoring, and higher‑order value systems are not included.
This project is intended purely for research and conceptual exploration.

---

## 📄 License
MIT License

---

## 📄 Paper (PDF)
The full VBPM-Core theoretical paper is available here:
👉 docs/paper/paper.pdf
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19732788.svg)](https://doi.org/10.5281/zenodo.19732788)

---

## 📚 Citation

SwayMagpie (2026). VBPM-Core: Value-Based Personality Model (Prototype).
GitHub: https://github.com/SwayMagpie/VBPM-Core


## Support & GPU Fund
If these "toys" contributed to your research or sparked a new perspective, you can fund my next GPU rig through GitHub Sponsors.

I make no promises. I provide no support. I am simply moving to the next game.

