# Q-Point Scoring Model v0.2

**Status:** Working Draft
**Version:** 0.2
**Related Protocol:** Q-Point Protocol v0.1
**Category:** Scoring Model / Catalyst Vector / Value Trace Evaluation

---

## 1. Purpose

This document defines the Q-Point Scoring Model v0.2.

The main update from v0.1 is the introduction of the **C-vector**, a multi-dimensional Catalyst model that decomposes the Catalyst score into four sub-components.

In v0.1, Catalyst was treated as a single scalar value.

In v0.2, Catalyst is defined as a composite score generated from four observable or inferable signals:

1. Self-Question Trigger
2. Confidence Shift
3. Internal Conflict Detection
4. Viewpoint Shift

This allows Q-Point to measure not only how strongly a contribution influenced an AI-mediated knowledge system, but also how that influence occurred.

---

## 2. Core Q-Point Formula

The overall Q-Point score is defined as:

```text
Q = w1O + w2D + w3C + w4T
```

Where:

| Symbol | Meaning           |
| ------ | ----------------- |
| `O`    | Originality       |
| `D`    | Depth             |
| `C`    | Catalyst          |
| `T`    | Trace Persistence |

The recommended initial weights are:

```text
Q = 0.30O + 0.25D + 0.30C + 0.15T
```

All component scores must be normalized to the range:

```text
0.0 <= score <= 1.0
```

---

## 3. Catalyst C-Vector

Catalyst measures how strongly a question, idea, or conceptual contribution moves an AI-mediated reasoning process.

In v0.2, Catalyst is decomposed into four sub-components:

```text
C = wc1S + wc2Δ + wc3K + wc4V
```

Where:

| Symbol | Component                   | Meaning                                                                                               |
| ------ | --------------------------- | ----------------------------------------------------------------------------------------------------- |
| `S`    | Self-Question Trigger       | The degree to which the contribution causes the AI system to generate new questions or inquiry paths. |
| `Δ`    | Confidence Shift            | The degree to which the contribution changes confidence, uncertainty, or answer stability.            |
| `K`    | Internal Conflict Detection | The degree to which the contribution triggers contradiction, tension, or re-evaluation signals.       |
| `V`    | Viewpoint Shift             | The degree to which the contribution shifts the conceptual or semantic viewpoint of the response.     |

The recommended initial weights are:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

All C-vector component scores must be normalized to the range:

```text
0.0 <= S, Δ, K, V <= 1.0
```

---

## 4. Component 1: Self-Question Trigger

### 4.1 Definition

Self-Question Trigger measures whether a contribution causes the AI system to generate new questions, inquiry paths, or reflective prompts.

A high Self-Question Trigger score indicates that the contribution did not merely receive an answer, but caused the AI system to open additional reasoning paths.

### 4.2 Possible Signals

Internal implementation may use:

* generated self-questions
* reflective subqueries
* planner-generated inquiry steps
* retrieval expansion queries
* internal decomposition steps

External or proxy implementation may use:

* assistant follow-up questions
* newly generated research angles
* number of distinct reasoning branches
* number of derived subtopics
* human-reviewed inquiry expansion

### 4.3 Suggested Formula

```text
S = normalized_self_question_intensity
```

Where `normalized_self_question_intensity` may be estimated from:

```text
self_question_count / expected_baseline
```

The result must be capped or normalized to the range:

```text
0.0 <= S <= 1.0
```

### 4.4 Anti-Gaming Note

Self-Question Trigger should not reward unnecessary or low-quality questions.

Implementations should evaluate the relevance and usefulness of generated questions, not only their count.

---

## 5. Component 2: Confidence Shift

### 5.1 Definition

Confidence Shift measures whether a contribution changes the AI system's certainty, uncertainty, or answer stability.

A high Confidence Shift score indicates that the contribution caused the system to revise, soften, strengthen, or re-evaluate its prior assumptions.

### 5.2 Possible Signals

Internal implementation may use:

* logit margin shifts
* confidence calibration changes
* uncertainty estimates
* answer distribution changes
* model self-evaluation deltas

External or proxy implementation may use:

* change in answer wording
* increase in uncertainty markers
* explicit revision of prior assumptions
* self-correction
* changed stance between draft and final output
* human-reviewed confidence movement

### 5.3 Suggested Formula

```text
Δ = normalized_confidence_shift
```

Example:

```text
Δ = abs(confidence_before - confidence_after)
```

The result must be normalized to:

```text
0.0 <= Δ <= 1.0
```

### 5.4 Interpretation

Confidence Shift does not automatically mean the contribution is correct.

It means the contribution moved the system's certainty state.

Therefore, high Δ should be interpreted as a catalyst signal, not as a truth signal.

---

## 6. Component 3: Internal Conflict Detection

### 6.1 Definition

Internal Conflict Detection measures whether a contribution triggers contradiction, tension, inconsistency detection, or re-evaluation inside the reasoning process.

A high Internal Conflict score indicates that the contribution forced the system to compare incompatible assumptions or resolve a conceptual conflict.

### 6.2 Possible Signals

Internal implementation may use:

* contradiction detection signals
* reasoning branch conflict
* safety-policy tension
* retrieval conflict
* attribution conflict
* self-evaluation disagreement

External or proxy implementation may use:

* explicit phrases such as "however", "on the other hand", or "this conflicts with"
* answer revision
* contradiction flags
* multiple competing interpretations
* human-reviewed conceptual tension
* evaluator disagreement

### 6.3 Suggested Formula

```text
K = normalized_conflict_intensity
```

Possible proxy:

```text
K = conflict_signal_count / token_or_turn_normalized_baseline
```

The result must be normalized to:

```text
0.0 <= K <= 1.0
```

### 6.4 Interpretation

Conflict is not a failure.

In Q-Point scoring, conflict may indicate that a contribution forced deeper reasoning.

However, false contradiction, hallucination, or confusion should not be rewarded.

Human review is recommended for high-K records.

---

## 7. Component 4: Viewpoint Shift

### 7.1 Definition

Viewpoint Shift measures whether a contribution changes the conceptual, semantic, or interpretive viewpoint of the AI-mediated response.

A high Viewpoint Shift score indicates that the contribution moved the system from one frame of interpretation to another.

### 7.2 Possible Signals

Internal implementation may use:

* hidden state movement
* embedding space movement
* semantic frame changes
* response planning vector changes
* topic representation shifts

External or proxy implementation may use:

* embedding distance between initial and final response drafts
* change in conceptual framing
* change in analogy or metaphor
* change in problem decomposition
* human-reviewed perspective shift

### 7.3 Suggested Formula

```text
V = 1 - cosine_similarity(v_before, v_after)
```

The result must be normalized to:

```text
0.0 <= V <= 1.0
```

Where:

| Symbol     | Meaning                                                                   |
| ---------- | ------------------------------------------------------------------------- |
| `v_before` | Semantic or conceptual representation before the contribution is applied. |
| `v_after`  | Semantic or conceptual representation after the contribution is applied.  |

### 7.4 Interpretation

Viewpoint Shift is especially important for deep questions, philosophical reframing, protocol design, and structural insight.

However, a large viewpoint shift alone does not guarantee high value.

It should be interpreted together with Originality, Depth, and Trace Persistence.

---

## 8. Full Q-Point v0.2 Formula

The full v0.2 formula is:

```text
Q = 0.30O + 0.25D + 0.30C + 0.15T
```

Where:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

Expanded:

```text
Q = 0.30O + 0.25D + 0.30(0.35S + 0.25Δ + 0.25K + 0.15V) + 0.15T
```

All scores must be normalized to the range:

```text
0.0 <= score <= 1.0
```

---

## 9. Example Output

```yaml
q_point_summary:
  total_score: 0.84
  scoring_method: "hybrid_ai_assisted_review"
  scoring_model_version: "q-point-scoring-model-v0.2"
  confidence: 0.79

q_point_components:
  originality: 0.86
  depth: 0.90
  catalyst: 0.83
  trace_persistence: 0.74

catalyst_vector:
  self_question_trigger: 0.88
  confidence_shift: 0.76
  internal_conflict_detection: 0.82
  viewpoint_shift: 0.72

catalyst_weights:
  self_question_trigger: 0.35
  confidence_shift: 0.25
  internal_conflict_detection: 0.25
  viewpoint_shift: 0.15
```

---

## 10. Pseudocode

```python
def calculate_q_point(session_data):
    # O, D, and T are evaluated using the v0.1 scoring model.
    originality = compute_originality(session_data)
    depth = compute_depth(session_data)
    trace_persistence = compute_trace_persistence(session_data)

    # Catalyst v0.2 C-vector
    self_question_trigger = compute_self_question_trigger(session_data)
    confidence_shift = compute_confidence_shift(session_data)
    internal_conflict = compute_internal_conflict_detection(session_data)
    viewpoint_shift = compute_viewpoint_shift(session_data)

    catalyst = (
        0.35 * self_question_trigger
        + 0.25 * confidence_shift
        + 0.25 * internal_conflict
        + 0.15 * viewpoint_shift
    )

    q_point = (
        0.30 * originality
        + 0.25 * depth
        + 0.30 * catalyst
        + 0.15 * trace_persistence
    )

    return {
        "total_score": q_point,
        "q_point_components": {
            "originality": originality,
            "depth": depth,
            "catalyst": catalyst,
            "trace_persistence": trace_persistence,
        },
        "catalyst_vector": {
            "self_question_trigger": self_question_trigger,
            "confidence_shift": confidence_shift,
            "internal_conflict_detection": internal_conflict,
            "viewpoint_shift": viewpoint_shift,
        },
    }
```

---

## 11. Internal and Proxy Modes

The C-vector can be calculated in two modes.

### 11.1 Internal Signal Mode

Internal Signal Mode may be used when the implementation has access to model-side signals such as:

* log probabilities
* hidden states
* attention patterns
* planning traces
* retrieval expansion
* evaluator modules
* confidence estimates

This mode is suitable for model providers, research systems, or open model environments.

### 11.2 Proxy Signal Mode

Proxy Signal Mode may be used when internal model signals are unavailable.

It estimates the C-vector using observable outputs such as:

* generated follow-up questions
* answer revisions
* uncertainty language
* contradiction markers
* semantic embedding shift
* response structure changes
* human review

This mode is suitable for API users, creator tools, dashboards, and external auditing systems.

### 11.3 Recommended Practice

The protocol should record which mode was used.

```yaml
scoring_signal_mode: "proxy_signal_mode"
```

Allowed values:

```text
internal_signal_mode
proxy_signal_mode
hybrid_signal_mode
```

---

## 12. Interpretation

Qpoint v0.2 does not merely ask:

```text
How much did the contribution move the AI?
```

It also asks:

```text
How did the contribution move the AI?
```

The C-vector makes this distinction possible.

A contribution may be valuable because it:

* caused the AI to ask new questions
* destabilized a shallow assumption
* exposed an internal contradiction
* shifted the viewpoint of the response
* opened a new conceptual path

This makes Catalyst a more precise and interpretable component of Q-Point.

---

## 13. Relationship to Royalty OS

The C-vector may become useful for future Royalty OS allocation models.

Different Catalyst patterns may correspond to different forms of value.

| Catalyst Pattern | Possible Value Type        |
| ---------------- | -------------------------- |
| High `S`         | Inquiry expansion value    |
| High `Δ`         | Assumption-shifting value  |
| High `K`         | Conflict-resolution value  |
| High `V`         | Perspective-shifting value |

This does not imply automatic monetary allocation.

Instead, the C-vector may serve as reference data for future review, gratitude, attribution, or royalty weighting.

---

## 14. Non-Monetary Disclaimer

The Q-Point Scoring Model does not create monetary value by itself.

Q-Point scores, including C-vector scores, are non-monetary evaluation records.

They do not represent currency, securities, ownership, debt, automatic royalty rights, or legal claims.

They may be used as reference data for future review, attribution, gratitude, licensing, or allocation systems.

---

## 15. Summary

Qpoint v0.2 introduces the C-vector as a refined Catalyst model.

The new Catalyst score is composed of:

```text
S: Self-Question Trigger
Δ: Confidence Shift
K: Internal Conflict Detection
V: Viewpoint Shift
```

The recommended Catalyst formula is:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

The recommended Q-Point formula is:

```text
Q = 0.30O + 0.25D + 0.30C + 0.15T
```

This allows Q-Point to record not only the existence of intellectual contribution, but the way that contribution moves AI-mediated reasoning.

In v0.2, Catalyst becomes a map of intellectual motion.
