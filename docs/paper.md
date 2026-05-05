# VBPM: Value-Based Personality Model


## 1. Introduction

### 1.1 Background and Motivation

In organizational settings, it is often observed that “high-performing individuals are excluded or marginalized.”  
If members were selecting their actions according to a single, shared organizational criterion, such a phenomenon would be difficult to explain in a rational manner.

High-performing individuals typically propose solutions that are optimal from economic or efficiency-oriented perspectives.  
If friction arose merely from differences in processing speed or cognitive capacity, the resulting behavioral mismatch would be understandable.  
However, in reality, there are cases in which individuals who present optimal solutions are nevertheless rejected.  
This suggests that the two sides are acting on the basis of *different forms of rationality*.

Importantly, this is not a matter of good or bad.  
Rather, it concerns differences in the *conditions under which rationality is established*.  
Some individuals are oriented toward change, while others prioritize stability.  
The latter, in particular, tend to engage in order-preserving or political behavior grounded in their own value systems.  
Such behavior is internallay coherent and rational from their perspective.

From these observations arises the hypothesis that differences in behavior are driven by differences in **Value Criteria**.  
Value criteria are not singular; multiple criteria coexist, and their priority ordering varies across individuals.  
Consequently, even when placed in the same situation, individuals may select different actions, sometimes resulting in conflict or exclusion.



### 1.2 Problem Statement

This study addresses two central questions:

(1) Why do individuals choose different actions under the same circumstances?  
(2) Why does what appears to be “rational behavior” differ across individuals?

Existing personality theories have succeeded in classifying observable behavioral tendencies (traits), but they do not sufficiently explain the underlying structure of evaluative criteria.  
Decision-making models, on the other hand, describe the process of action selection, yet they lack a framework for representing the structure or dynamics of the value criteria that serve as inputs to that process.

In this work, we adopt the position that differences in behavior arise from differences in the structure of value criteria.

### 1.3 Formation of the Hypothesis

Individuals possess multiple value criteria and assign weights to them when evaluating situations and selecting rational actions.  
The set of behaviors that emerges from this process—“value criteria × weights × optimization”—may constitute what is externally observed as personality.

Value criteria are not fixed.  
They may be added, reweighted, integrated, become dormant, or disappear depending on experience and environment.  
We therefore arrive at the hypothesis that changes in the structure of this network of value criteria constitute the essence of personality formation and personality change.

### 1.4 Value Criteria and the ``Economy of Value''

Human decision-making can be viewed as operating within a broad “economy of value,” which includes fundamental motivations such as survival, gain, and loss avoidance.  
Individuals evaluate information from their environment through multiple value criteria, assign weights to these criteria, and select actions that optimize the resulting evaluation.

Value criteria function as basis functions for computing this economy of value.  
The structure of these criteria—and how they are added, integrated, made dormant, or removed—determines what an individual considers important.  
The weights assigned to each criterion serve as coefficients in this computation, meaning that even individuals who share the same criteria may behave quite differently depending on their weighting.

Notably, the mechanisms of value criteria and weighting correspond to physical modules in the brain.  
For example, the amygdala evaluates safety-related values such as danger and fear;  
the prefrontal cortex handles long-term gain and planning;  
and the insular cortex evaluates bodily and emotional pleasantness or unpleasantness.  
These regions can be understood as modules that compute distinct value criteria.

This correspondence suggests that value criteria are not merely abstract metaphors but constitute an “implementable hypothesis” consistent with the brain’s information-processing architecture.  
For the author, this alignment is particularly significant, as it connects the intuitive idea that differences in value criteria generate differences in behavior with neuroscientific structure.

Taken together, human behavior can be understood as the result of computing  
“value criteria × weights × optimization”  
within an economy of value.  
The structure and dynamics of this system form the basis of personality formation and change.

### 1.5 Purpose of This Study

The purpose of this study is to propose the Value-Based Personality Model (VBPM), a personality model grounded in value criteria and their weighting, and to present a new framework that interprets personality as structural change within a network of value criteria.

Specifically, this study aims to:


- Formalize an action-selection model based on value criteria, weights, and optimization.

- Introduce a lifecycle for value criteria (addition, dormancy, integration, deletion).

- Demonstrate a minimal prototype (“baby-personality”) as a proof of concept.


### 1.6 Structure of This Paper

The remainder of this paper is organized as follows.

Chapter 2 reviews the limitations of existing research and motivates the need for a model centered on value criteria.  

Chapter 3 presents the structure of VBPM, detailing value criteria, weights, optimization, and their lifecycle.  

Chapter 4 describes the implementation of the minimal prototype.  

Chapter 5 discusses the significance and limitations of the model.  

Chapter 6 concludes the study.

Chapter 7 outlines possible extensions.  




## 2. Related Work

This chapter briefly reviews existing personality theories and decision-making models in order to position VBPM within the broader research landscape.  
The aim is not to provide a comprehensive or systematic review.  
Rather, we offer a high-level overview based on surface-level interpretations of prior work, with the goal of clarifying which conceptual gaps VBPM seeks to address.

#### Personality Trait Models

Personality trait models such as the Big Five and HEXACO provide frameworks for classifying human behavioral tendencies across multiple dimensions.  
These models are empirically robust and widely applied in psychology.  
However, they focus on “observable tendencies as outcomes of behavior” and do not address the underlying structure of evaluative criteria (value criteria) that give rise to such tendencies.

From the perspective of this study, trait models constitute a “classification of outputs,” not an explanation of the “mechanisms of evaluation.”

#### Decision-Making Models

In decision-making research, models such as the Drift Diffusion Model (DDM) and Reinforcement Learning (RL) are widely used.  
DDM describes the temporal process of decision formation, while RL explains learning based on reward prediction errors.  
These models align well with known computational structures of the brain, yet they are not designed to account for personality differences or the multidimensional nature of value.

In our understanding, these models describe “processes,” but do not explain the “structure of value.”

#### Research on Values and Social Behavior

Research on Social Value Orientation (SVO) and Schwartz’s value model examines which values individuals prioritize.  
These frameworks provide taxonomies of values, but they do not address the dynamic aspects of how value criteria are generated, updated, or integrated over time.

From the viewpoint of this study, these models offer “classifications of values,” but not “computational models of value criteria.”

#### Positioning of VBPM

Based on this high-level review, VBPM can be positioned as a model that fills the following conceptual gaps:

- It addresses the “structure of value criteria,” situated between trait models (which classify behavioral tendencies) and decision-making models (which describe processes).

- By aligning value criteria with modular structures in the brain, it provides a framework that spans neuroscience, computational modeling, and psychology.

- By incorporating dynamic changes—addition, dormancy, integration, and deletion of value criteria—it enables the explanation of personality development over time.


The content of this chapter is not intended as a rigorous review of prior research, but rather as a conceptual overview to clarify the positioning of VBPM.



## 3. Model Structure

### 3.1 Value Criteria

In this study, a Value Criterion is defined as an
“evaluation module composed of a Value Dimension and its associated Weight.”

A value dimension serves as a fundamental axis for evaluating the environment.  
Examples include safety, efficiency, harmony, novelty, status, pleasure, and duty—each of which can be understood as an independent evaluative function.

The weight represents how strongly an individual prioritizes each value dimension, and it constitutes a major source of individual differences.  
Even when two individuals share the same set of value dimensions, differences in weighting can lead to markedly different behaviors.

Formally, a value criterion can be expressed as:



$[
\text{Value Criterion}_i = (\text{Value Dimension}_i, \; w_i)
]$



Action selection is performed by integrating the evaluations produced by each value criterion in a weighted manner:



$[
\text{Utility}(a) = \sum_i w_i \cdot V_i(a)
]$



where $(V_i(a))$ denotes the evaluation of action $(a)$ under value dimension $(i)$.

Interestingly, these value dimensions correspond to physical modules in the brain.  
The amygdala evaluates safety-related values such as danger and fear;  
the prefrontal cortex handles long-term gain and planning;  
and the insular cortex evaluates bodily and emotional pleasantness or unpleasantness.  
These regions can be interpreted as modules that compute distinct value dimensions.

This correspondence suggests that the concept of value criteria is not merely an abstract metaphor, but an “implementable hypothesis” consistent with the brain’s information-processing architecture.



### 3.2 Value Dimensions

In this study, Value Dimensions are defined as
“independent evaluative axes computed by distinct physical modules in the brain.”

The brain does not compute a single unified notion of value.  
Rather, multiple regions evaluate different types of value in parallel.  
For example, the amygdala evaluates safety-related values such as danger and fear;  
the prefrontal cortex handles long-term gain and planning;  
the insular cortex evaluates bodily and emotional pleasantness or unpleasantness;  
and the anterior cingulate cortex evaluates social values such as approval and harmony.

These brain regions can therefore be interpreted as modules that compute distinct value dimensions.  
Accordingly, value dimensions are not arbitrarily defined constructs;  
they represent a natural decomposition derived from the brain’s information-processing architecture.

In this framework, a Value Criterion is treated as an evaluation module composed of a value dimension and its associated weight.  
The value dimension specifies *what* is being evaluated,  
while the weight determines *how strongly* that value is prioritized.


### 3.3 Weights

In this study, Weights are defined as
“parameters that determine the contribution of each value dimension when their outputs are integrated.”

Weights are variable quantities that are updated through experience, much like parameters in a neural network.  
The brain’s decision-making process integrates the outputs of multiple value dimensions in a weighted manner and selects actions through nonlinear processing.  
In this respect, its computational structure resembles that of a neural network.

The updating of weights is consistent with reinforcement learning rules based on Reward Prediction Error (RPE):



$[
w_i \leftarrow w_i + \alpha \cdot \delta \cdot V_i
]$



Here, $(\delta)$ denotes the prediction error, $(\alpha)$ the learning rate,  
and $(V_i)$ the output of value dimension $(i)$.  
Through this update rule, the weights of value criteria change with experience,  
and as a result, behavioral tendencies—i.e., personality—also change.

Weights are not fixed.  
They vary dynamically depending on environment, experience, social roles, and bodily states.  
Even when individuals share the same value dimensions, differences in weighting can lead to substantial differences in behavior.  
Thus, weights constitute a major source of individual personality differences.

In this study, weights are treated as parameters analogous to those in neural networks,  
allowing personality change to be modeled in a manner consistent with the brain’s computational architecture.


### 3.4 Optimization

In this study, Optimization is defined as
“the maximization of self-consistency within the range of states accessible to the individual.”

Traditional decision-making models often treat optimization as the maximization of external rewards or as learning based on accumulated experience.  
However, such formulations are insufficient for explaining personality formation and behavioral selection.  

Humans not only choose actions based on value criteria and their weights,  
but also evaluate whether those actions are consistent with their internal model of themselves.  
This “internal consistency” is distinct from subjective emotions such as satisfaction or regret;  
it can be treated as a computable quantity grounded in the structure of value criteria and weights.

In this framework, the selection of an action \(a\) is understood as maximizing the following objective function:



$[
\text{Consistency}(a) = \sum_i w_i \cdot V_i(a)
]$



Here, $(V_i(a))$ denotes the evaluation of action $(a)$ under value dimension $(i)$,  
and $(w_i)$ represents the importance of that dimension.

This formulation does not describe the maximization of external reward.  
Rather, it represents an internal optimization process in which the individual selects the action that is most consistent with the structure of their value criteria and weights.

Such optimization of self-consistency aligns with neuroscientific findings on predictive coding—where the brain minimizes prediction error—as well as with theories of cognitive dissonance reduction.


### 3.5 Information Processing and the Flow of Action Selection

This section summarizes how the components introduced earlier—Value Dimensions,  
Weights, and Optimization of self-consistency—interact to produce action selection.

Human decision-making can be understood as proceeding through the following sequence:

#### 1. Information Input
  Information obtained from the external environment is fed into multiple value-dimension modules in the brain.

#### 2. Evaluation by Value Dimensions  
  Each value dimension independently computes an evaluation value $(V_i(a))$ for the situation or candidate action $(a)$.  
  This corresponds to computations performed by regions such as the amygdala, prefrontal cortex, and insular cortex.

#### 3. Weighted Integration
  The evaluation values from each value dimension are integrated according to their respective weights $(w_i)$.  
  This structure resembles the weighted linear combination used in neural networks.

#### 4. Computation of Self-Consistency  
  The integrated value is interpreted as the self-consistency of action $(a)$:



$[
  \text{Consistency}(a) = \sum_i w_i \cdot V_i(a)
]$



#### 5. Action Selection
  The action that maximizes self-consistency is selected.  
  This is not the maximization of external reward, but an internal optimization process in which  
  the individual chooses the action that is least contradictory with the structure of their value criteria and weights.

#### 6. Feedback and Weight Updating
  The outcome of the action is processed as a prediction error,  
  which updates the weights \(w_i\).  
  Through this mechanism, the network of value criteria changes dynamically,  
  and these changes manifest externally as personality development or transformation.

Through this sequence, value dimensions, weights, and optimization


### 3.6 Value Criteria Lifecycle

As described in the previous sections, value criteria consist of value dimensions and their associated weights, and they are continuously updated within the information-processing and action-selection pipeline.  
This section organizes how value criteria are generated, transformed, and removed, framing these processes as a lifecycle.

The lifecycle of value criteria consists of the following four processes:

#### 1. Acquisition  
  New value criteria are added when changes in environment, roles, experiences, or social exchange relationships create the need for new value dimensions.  
  This is a natural process grounded in the broad “economy of value,” which includes survival, gain, and loss avoidance.

  Acquisition typically occurs in situations such as:


  - Becoming a parent → values such as “safety” and “stability” are added  

  - Entering a competitive environment → “efficiency” and “achievement” become salient  

  - Joining a community → “cooperation” and “approval” emerge as important  

  - Engaging deeply in creative work → “aesthetics” and “originality” are added


  Value criteria do not increase without bound, but new values naturally emerge as life phases change.

#### 2. Dormancy  
  Even without being deleted, a value criterion may become effectively inactive when its weight decreases significantly.  
  This is analogous to an unused module in an operating system.

  For example, a value such as “approval,” once highly important, may become rarely referenced after an individual develops greater autonomy.

  Dormant value criteria are not eliminated; they retain the potential to be reactivated under specific circumstances.

#### 3. Integration  
  Similar value criteria may be merged and reconstructed as a higher-level, more abstract value criterion.  
  This process resembles garbage collection and serves to reduce redundancy in the value-criteria network.

  For instance, “politeness,” “harmony,” and “approval” may be integrated into a higher-order value such as “social stability.”

#### 4. Deletion  
  Complete deletion of a value criterion is rare, but it may occur under the following conditions:


  - Severe trauma leads the system to judge the value itself as dangerous  

  - Environmental changes render the value detrimental to survival  

  - The value remains unused for an extended period and becomes isolated in the network  

  - Integration processes make the original value redundant

  Deletion is better understood not as absolute erasure, but as part of a broader process of integration, compression, and reorganization.


In summary, value criteria should not be viewed as static entities that simply increase or decrease.  
They are better understood as components of a dynamically evolving network.  
Personality formation is the transformation of this network itself, grounded in the acquisition, dormancy, integration, and deletion of value criteria.


## 4. Prototype

This chapter describes the “baby personality” prototype, a minimal implementation of the VBPM framework.  
The prototype is not intended as a full realization of the value-criteria network.  
Rather, it serves as a highly simplified model for examining the relationship among value dimensions, weights, and action selection.

The implementation is available in the following public repository:

- {https://github.com/SwayMagpie/VBPM-Core.git}

### 4.1 Model Overview

In this prototype, Personality is represented as a set of fixed weights assigned to each value dimension:

```
@dataclass
class Personality:
    name: str
    values: Dict[str, float]
```

A Scenario is defined as a situation that provides a score for each value dimension:

```
@dataclass
class Scenario:
    id: str
    description: str
    scores: Dict[str, float]
```

### 4.2 Initial Configuration of the Baby Personality

The prototype defines a “baby personality” with the following fixed weights:

```
values = {
    "safety":   0.9,
    "comfort":  0.8,
    "novelty":  0.6,
    "social":   0.4,
    "autonomy": 0.1,
}
```

This configuration abstractly models an infant who strongly prioritizes safety and comfort,  
is moderately attracted to novelty,  
and exhibits minimal autonomy.

### 4.3 Scenarios and Evaluation

The prototype includes two scenarios:

```
- S1: A stranger approaches  

- S2: The mother picks up the infant
```

Each scenario provides scores for the value dimensions.

```
Scenario(
    id="S1",
    description="A stranger approaches",
    scores={
        "safety":   0.2,
        "comfort":  0.3,
        "novelty":  0.8,
        "social":   0.5,
        "autonomy": 0.1,
    },
)
```

```
Scenario(
    id="S2",
    description="Mother picks up the infant",
    scores={
        "safety":   0.9,
        "comfort":  0.9,
        "novelty":  0.3,
        "social":   0.8,
        "autonomy": 0.1,
    },
)
```

### 4.4 Action Selection Logic

Action selection is implemented as a simple weighted sum corresponding to the core VBPM formulation:



$[
\text{Utility}(a) = \sum_v w(v) \cdot \text{score}(v, a)
]$



In code, this is expressed as:

```
def evaluate_scenario(personality, scenario):
    total = 0.0
    for v, w in personality.values.items():
        s = scenario.scores.get(v, 0.0)
        total += w * s
    return total
```

The scenario with the highest utility is selected:

```
def choose_best_scenario(personality, scenarios):
    scored = [(sc, evaluate_scenario(personality, sc)) for sc in scenarios]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0]
```

This prototype does not include weight updating or learning.  
It is a static model designed solely to illustrate the minimal structure of VBPM:  
“value dimensions × weights → action selection.”

### 4.5 Position of This Chapter

This prototype is not a full implementation of VBPM.  
It isolates only a subset of the theory—value dimensions, weights, and action selection—  
to provide a minimal working example.  
Dynamic aspects such as weight updating, the lifecycle of value criteria,  
and optimization of self-consistency (as described in Chapter 3)  
are not yet included.

The purpose of this chapter is to demonstrate how the VBPM framework can be instantiated in concrete code,  
providing a foundation for future exploration and extension.

## 5. Discussion

This chapter discusses the theoretical significance and limitations of VBPM,  
as well as the “explorability” that the model enables.  
VBPM does not treat personality as a fixed structure;  
instead, it conceptualizes personality as the dynamic transformation of a network of value criteria.  
Accordingly, the model is not designed as a static, finalized theory,  
but as an exploratory framework that allows observation, experimentation, and manipulation.

### 5.1 Theoretical Significance of VBPM

VBPM is characterized by its explicit treatment of an intermediate layer—Value Criteria—that has been largely absent from existing personality theories.  
Models such as the Big Five and HEXACO classify behavioral tendencies,  
but do not address the evaluative structures that generate those tendencies.  
Conversely, decision-making models such as DDM and reinforcement learning describe processes,  
but are not equipped to explain multidimensional value structures or individual personality differences.

VBPM fills this conceptual gap.  
Value dimensions are derived from the computational roles of physical brain modules;  
weights are treated as parameters analogous to those in neural networks;  
and optimization is formulated as the maximization of self-consistency.  
Through this structure, VBPM functions as an integrative personality model  
that spans neuroscience, computational modeling, and psychology.

### 5.2 Limitations of VBPM

Several limitations of the model should be acknowledged:

- The complete set of value dimensions is not yet established,  
        and it remains an open question how well the model can accommodate cultural and individual variation.

- The neural implementation of weight updating is not fully understood,  
        and RPE-based update rules should be regarded as approximations.
- Although self-consistency can be defined mathematically,  
        its correspondence with subjective human experience requires empirical validation.
- Social values—such as approval, harmony, and role obligations—are strongly shaped by cultural factors,  
        and their universal modeling requires careful consideration.

These limitations represent challenges,  
but they also highlight promising directions for future research.

### 5.3 Explorability

The most distinctive feature of VBPM is that it treats personality as a structure that can be explored.  
The network of value criteria is not static;  
it is a dynamic system that continually changes through acquisition, dormancy, integration, and deletion.

Thus, the model does not need to aim for a final, complete form.  
Rather, exploration itself—through observation, experimentation, and manipulation of the value-criteria network—constitutes the core of the research program.

#### Examples of possible explorations include:


- Observing the conditions under which value criteria are acquired, become dormant, are integrated, or are deleted

- Visualizing the trajectory of weight updates and quantifying personality change

- Analyzing distributions of action selection to identify patterns of conflict among value criteria

- Investigating the conditions under which dormant value criteria reactivate

- Exploring the existence of meta-value criteria (criteria that evaluate other criteria)

- Examining how differences in initial conditions influence personality development


These explorations provide a new methodological approach for understanding personality not as a static classification,  
but as a dynamic system that can be analyzed, manipulated, and evolved.

### 5.4 Position of This Study

The purpose of this study is not to provide a complete description of personality.  
Rather, it aims to present a “playable model” that enables observation, experimentation, and understanding of personality change.

VBPM is not a finished theory.  
It is a prototypical framework for exploring the dynamic system of value criteria.  
Using this framework, phenomena such as personality development, transformation, conflict, and reorganization  
can be examined from a new perspective.



## 6. Conclusion

This study proposed the Value-Based Personality Model (VBPM),  
which conceptualizes personality as a computable structure defined by  
“value dimensions × weights × optimization.”  
VBPM explicitly addresses the structure of value criteria—an intermediate layer  
situated between the behavioral tendencies described by traditional trait models  
and the processes described by decision-making models.

In VBPM, value dimensions are aligned with modular structures of the brain,  
weights are treated as parameters analogous to those in neural networks,  
and action selection is formulated as the maximization of self-consistency.  
Furthermore, by introducing a dynamic lifecycle of value criteria—acquisition,  
dormancy, integration, and deletion—the model provides a framework capable of  
explaining personality development over time.

As a minimal implementation of VBPM, we developed the “baby personality” prototype,  
which offers a simple environment for examining how value dimensions and weights  
influence action selection.  
This prototype is not a full implementation of VBPM;  
rather, it serves as a foundation for beginning the exploration of value-criteria networks.

VBPM offers a new perspective in which personality is not treated as a fixed classification,  
but as the dynamic transformation of a network of value criteria.  
The contribution of this study lies in presenting a foundation for treating personality  
as a structure that can be observed, experimented with, and explored.

In addition, this study is characterized by its treatment of personality  
as a structure that can be externalized.  
By explicitly modeling the internal evaluative structure—value criteria and weights—  
VBPM enables external representations that allow personality to be observed,  
described, shared, and manipulated.

Human evolution can be understood as a history of externalizing abilities and knowledge  
into tools, language, and institutions.  
In a similar manner, the externalization of personality provides a basis for extracting,  
reusing, improving, and evolving an individual’s decision-making and value structures.

By conceptualizing personality not as a fixed trait but as an externalizable  
network of value criteria, VBPM offers a new framework for enabling  
the evolution of personality itself.


## 7. Future Work

The VBPM proposed in this study was developed within a very short time frame  
(on the order of several hours at the time of writing).  
Accordingly, the topics listed in this chapter have not yet been explored in depth  
or validated through implementation.  
What follows is a set of hypotheses—points that appear promising for future exploration.

#### Handling the Subjectivity of Scoring

In the current model, $Score((v, a))$ is treated as a fixed value.  
In reality, however, the score assigned to the same action can vary greatly  
depending on an individual’s experiences, memories, and value structure.

For example, when encountering a dog:

- “Cute” → the Social dimension contributes positively  

- “Scary” → the Safety dimension contributes strongly negatively


Future work should treat $Score((v, a))$ as a dynamic function  
generated by the individual’s value-criteria network.


#### Dynamic Weight Changes Driven by Internal States

Human value priorities fluctuate temporarily depending on internal states  
such as hunger, fatigue, or stress.

- When hungry, the weight of Comfort increases sharply  

- When danger is imminent, the weight of Safety becomes dominant

Modeling these effects would enable more biologically grounded  
and realistic representations of personality.

#### Using Information from Non-Selected Actions

The current prototype selects only the action with the highest utility.  
However, the difference between the top-ranked and second-ranked actions  
contains important information about “personality variability” or “indecision.”

- Small difference → curious, flexible tendencies  

- Large difference → strong consistency, cautious tendencies
\end{itemize}

Future extensions may incorporate fluctuation models based on utility differences  
or probabilistic action selection methods such as softmax.

#### Higher-Order Structure of the Value-Criteria Network

Relationships among value criteria—such as dependency, conflict, or hierarchy—  
could be modeled as a network, enabling richer representations of personality.

- Hierarchical structures such as “ethics → fairness → rule adherence”  

- Conflicts such as “autonomy ↔ need for approval”
\end{itemize}

Defining the topology of the value-criteria network  
is an important direction for future investigation.

#### Refining Weight-Update Algorithms

More precise modeling of weight changes is needed,  
potentially incorporating reward prediction error (RPE),  
Bayesian updating, or other learning mechanisms.  
At present, the discussion remains conceptual,  
and the design and empirical validation of concrete update rules  
remain open challenges.

#### Integration with LLMs and Externalization of Personality

Integrating the value-criteria network into an LLM as an external memory  
may provide a foundation for constructing “AI systems with personality.”

- Logging additions and updates to value criteria  

- Externalizing the process by which personality changes and grows through interaction
\end{itemize}

This aligns with VBPM’s perspective of treating personality  
not as an internal hidden state, but as an externalizable structure.

#### Applications to Empirical Research

Methods for estimating value criteria from behavioral data,  
dialogue logs, or questionnaires will be necessary.

- Quantifying individual differences  

- Predicting interpersonal friction  

- Evaluating the reproducibility of action selection

These ideas remain at the conceptual stage,  
and concrete data collection and analysis represent future work.

