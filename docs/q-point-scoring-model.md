# Q-Point Scoring Model v0.2

**Status:** Working Draft
**Version:** 0.2.0-candidate
**Related Protocol:** Q-Point Protocol v0.1
**Category:** Scoring Model / Catalyst Vector / Value Trace Evaluation
**Primary Schema:** `schemas/q-point-record.schema.json`
**Primary Example:** `examples/q-point-record.example.yaml`

---

## 1. Purpose

This document defines the **Q-Point Scoring Model v0.2**.

The purpose of this scoring model is to describe how question-based intellectual contribution can be evaluated as a non-monetary value trace within AI-mediated knowledge systems.

The main update in v0.2 is the introduction of the **Catalyst C-vector**, a multi-dimensional model for measuring how a question, idea, or conceptual contribution moves AI-mediated reasoning.

In v0.1, Catalyst was treated as a single scalar value.

In v0.2, Catalyst is decomposed into four sub-components:

1. Self-Question Trigger
2. Confidence Shift
3. Internal Conflict Detection
4. Viewpoint Shift

This allows Q-Point to record not only that a contribution influenced AI-mediated reasoning, but also how that influence occurred.

---

## 2. Non-Monetary Nature

Q-Point is not money.

Q-Point is not a currency.

Q-Point is not a crypto asset.

Q-Point is not a legal claim.

Q-Point is not an automatic royalty.

Q-Point is a non-monetary value trace score.

The scores defined in this document may be used as reference data for future review, attribution, gratitude, licensing, or allocation systems.

They do not create payment obligations by themselves.

Recommended disclaimer:

```text
This Q-Point record is a non-monetary value trace. It does not represent currency, securities, legal ownership, automatic royalty rights, debt, or a claim to payment. It may be used as reference data for future review, attribution, gratitude, licensing, or allocation systems.
```

---

## 3. Core Q-Point Formula

The overall Q-Point score is defined as:

```text
Q = w1O + w2D + w3C + w4T
```

Where:

| Symbol | Component         | Meaning                                                                         |
| ------ | ----------------- | ------------------------------------------------------------------------------- |
| `O`    | Originality       | How distinct, non-derivative, or conceptually original the contribution is.     |
| `D`    | Depth             | How deep, layered, or structurally meaningful the contribution is.              |
| `C`    | Catalyst          | How strongly the contribution moves AI-mediated reasoning.                      |
| `T`    | Trace Persistence | How persistently the contribution can be traced across time, records, or reuse. |

The recommended initial weights are:

```text
Q = 0.30O + 0.25D + 0.30C + 0.15T
```

All scores must be normalized to the range:

```text
0.0 <= score <= 1.0
```

---

## 4. Score Normalization

All Q-Point scoring components should use normalized values from `0.0` to `1.0`.

| Value  | Interpretation                 |
| ------ | ------------------------------ |
| `0.0`  | No meaningful signal detected. |
| `0.25` | Weak signal.                   |
| `0.50` | Moderate signal.               |
| `0.75` | Strong signal.                 |
| `1.0`  | Very strong signal.            |

Implementations may internally use other ranges, such as `0-100`, but stored Q-Point records should use `0.0-1.0` unless a future schema version explicitly permits otherwise.

This keeps schema validation, weighted scoring, dashboard visualization, and cross-system comparison simple.

---

## 5. Main Q-Point Components

### 5.1 Originality

Originality measures whether a contribution introduces a distinct idea, structure, framing, or conceptual pattern.

Possible signals include:

* semantic distance from existing records
* low similarity to prior known examples
* new combination of known concepts
* unusual but coherent framing
* human reviewer assessment
* cross-record novelty comparison

Originality should not reward randomness.

A contribution should be both distinct and meaningful.

---

### 5.2 Depth

Depth measures whether a contribution contains layered context, structural reasoning, philosophical weight, technical density, or long-range implication.

Possible signals include:

* multi-step reasoning potential
* conceptual density
* structural clarity
* relation to broader systems
* long-term interpretive value
* ability to generate further inquiry

Depth is different from length.

A short question may have high depth if it opens a powerful reasoning path.

---

### 5.3 Catalyst

Catalyst measures how strongly a contribution moves AI-mediated reasoning.

In v0.2, Catalyst is no longer treated as a single undifferentiated score.

Instead, it is calculated through the C-vector:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

Where:

| Symbol | Component                   | Meaning                                                                        |
| ------ | --------------------------- | ------------------------------------------------------------------------------ |
| `S`    | Self-Question Trigger       | Whether the contribution causes new questions or inquiry paths.                |
| `Δ`    | Confidence Shift            | Whether the contribution changes uncertainty, confidence, or answer stability. |
| `K`    | Internal Conflict Detection | Whether the contribution triggers contradiction, tension, or re-evaluation.    |
| `V`    | Viewpoint Shift             | Whether the contribution shifts the conceptual or semantic viewpoint.          |

---

### 5.4 Trace Persistence

Trace Persistence measures whether the contribution can be linked, followed, reused, or referenced over time.

Possible signals include:

* stable Epicenter ID
* trace links
* related records
* reuse references
* content hash
* source metadata
* citation or attribution links
* cross-AI aggregation references

Trace Persistence is important because future attribution, gratitude, licensing, or royalty systems require reliable records.

A contribution with high conceptual value but poor traceability may require additional review before it can be used in allocation systems.

---

## 6. Catalyst C-Vector

The Catalyst C-vector decomposes Catalyst into four measurable or inferable sub-components.

```text
C = wc1S + wc2Δ + wc3K + wc4V
```

Recommended weights:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

Where:

| Symbol | Component                   | Recommended Weight |
| ------ | --------------------------- | ------------------ |
| `S`    | Self-Question Trigger       | `0.35`             |
| `Δ`    | Confidence Shift            | `0.25`             |
| `K`    | Internal Conflict Detection | `0.25`             |
| `V`    | Viewpoint Shift             | `0.15`             |

The weights must sum to `1.0`.

```text
wc1 + wc2 + wc3 + wc4 = 1.0
```

The recommended weights are intentionally conservative.

They may be adjusted in future versions after empirical testing, reviewer feedback, or cross-AI comparison.

---

## 7. Component S: Self-Question Trigger

### 7.1 Definition

Self-Question Trigger measures the degree to which a contribution causes an AI-mediated system to generate new questions, inquiry paths, subqueries, or exploratory branches.

A high Self-Question Trigger score indicates that the contribution did not merely receive an answer. It caused the reasoning process to expand.

### 7.2 Possible Signals

Internal signal mode may use:

* planner-generated subquestions
* retrieval expansion queries
* internal decomposition steps
* reflection loops
* task planning branches

Proxy signal mode may use:

* assistant follow-up questions
* newly generated research directions
* number of derived subtopics
* visible reasoning branches
* human-reviewed inquiry expansion

### 7.3 Suggested Calculation

```text
S = normalized_self_question_intensity
```

A possible proxy formula:

```text
S = min(1.0, self_question_count / expected_baseline)
```

Where:

| Term                  | Meaning                                                                                |
| --------------------- | -------------------------------------------------------------------------------------- |
| `self_question_count` | Number or intensity of new inquiry paths triggered by the contribution.                |
| `expected_baseline`   | Expected number of inquiry paths in an ordinary interaction of similar length or type. |

### 7.4 Anti-Gaming Note

Self-Question Trigger should not reward unnecessary or low-quality question generation.

The system should evaluate the relevance, usefulness, and conceptual coherence of generated questions.

---

## 8. Component Δ: Confidence Shift

### 8.1 Definition

Confidence Shift measures the degree to which a contribution changes confidence, uncertainty, or answer stability.

A high Confidence Shift score indicates that the contribution caused the system to revise, soften, strengthen, or re-evaluate its prior assumptions.

### 8.2 Possible Signals

Internal signal mode may use:

* log probability changes
* logit margin shifts
* uncertainty estimates
* self-evaluation deltas
* answer distribution changes
* calibration movement

Proxy signal mode may use:

* visible change in answer stance
* self-correction
* explicit uncertainty markers
* revision of earlier assumptions
* change between draft and final output
* human-reviewed confidence movement

### 8.3 Suggested Calculation

```text
Δ = normalized_confidence_shift
```

A possible formula:

```text
Δ = abs(confidence_before - confidence_after)
```

The result must be normalized to:

```text
0.0 <= Δ <= 1.0
```

### 8.4 Interpretation

Confidence Shift is a movement signal, not a truth signal.

A high Confidence Shift score does not prove that the contribution is correct.

It means the contribution moved the certainty state of the reasoning process.

Human review is recommended when high Confidence Shift is used for attribution, gratitude, or allocation review.

---

## 9. Component K: Internal Conflict Detection

### 9.1 Definition

Internal Conflict Detection measures the degree to which a contribution triggers contradiction, tension, inconsistency detection, or re-evaluation.

A high Internal Conflict Detection score indicates that the contribution forced the system to compare incompatible assumptions or resolve conceptual tension.

### 9.2 Possible Signals

Internal signal mode may use:

* contradiction detection signals
* reasoning branch disagreement
* retrieval conflict
* attribution conflict
* evaluator disagreement
* policy or safety tension
* self-checking conflict signals

Proxy signal mode may use:

* visible contradiction markers
* phrases such as "however", "on the other hand", or "this conflicts with"
* answer revision
* multiple competing interpretations
* explicit comparison of alternatives
* human-reviewed conceptual tension

### 9.3 Suggested Calculation

```text
K = normalized_conflict_intensity
```

A possible proxy formula:

```text
K = min(1.0, conflict_signal_count / normalized_baseline)
```

Where:

| Term                    | Meaning                                                                  |
| ----------------------- | ------------------------------------------------------------------------ |
| `conflict_signal_count` | Number or intensity of contradiction, tension, or re-evaluation signals. |
| `normalized_baseline`   | Expected conflict signal level for a comparable interaction.             |

### 9.4 Interpretation

Conflict is not automatically bad.

In Q-Point scoring, conflict may indicate that a contribution forced deeper reasoning.

However, confusion, hallucination, or false contradiction should not be rewarded.

High-K records should be reviewed carefully.

---

## 10. Component V: Viewpoint Shift

### 10.1 Definition

Viewpoint Shift measures the degree to which a contribution changes the conceptual, semantic, interpretive, or structural viewpoint of the response.

A high Viewpoint Shift score indicates that the contribution moved the reasoning process from one frame of interpretation to another.

### 10.2 Possible Signals

Internal signal mode may use:

* hidden state movement
* semantic frame changes
* representation shifts
* response planning vector movement
* topic representation changes

Proxy signal mode may use:

* embedding distance between response drafts
* change in conceptual framing
* change in analogy or metaphor
* change in problem decomposition
* change in explanatory level
* human-reviewed perspective shift

### 10.3 Suggested Calculation

```text
V = 1 - cosine_similarity(v_before, v_after)
```

Where:

| Symbol     | Meaning                                                                   |
| ---------- | ------------------------------------------------------------------------- |
| `v_before` | Semantic or conceptual representation before the contribution is applied. |
| `v_after`  | Semantic or conceptual representation after the contribution is applied.  |

The result must be normalized to:

```text
0.0 <= V <= 1.0
```

### 10.4 Interpretation

Viewpoint Shift is especially important for:

* philosophical reframing
* protocol design
* structural insight
* cross-domain analogy
* new conceptual architecture
* problem redefinition

A large viewpoint shift alone does not guarantee high value.

It should be interpreted together with Originality, Depth, Catalyst, and Trace Persistence.

---

## 11. Full Q-Point v0.2 Formula

The recommended Q-Point v0.2 formula is:

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

All values must be normalized to:

```text
0.0 <= score <= 1.0
```

---

## 12. Example Scoring Record

```yaml
q_point_components:
  originality: 0.86
  depth: 0.90
  catalyst: 0.81
  trace_persistence: 0.74
  component_weights:
    originality: 0.30
    depth: 0.25
    catalyst: 0.30
    trace_persistence: 0.15

catalyst_vector:
  self_question_trigger: 0.88
  confidence_shift: 0.76
  internal_conflict_detection: 0.82
  viewpoint_shift: 0.72
  catalyst_score: 0.81
  catalyst_weights:
    self_question_trigger: 0.35
    confidence_shift: 0.25
    internal_conflict_detection: 0.25
    viewpoint_shift: 0.15

q_point_summary:
  total_score: 0.84
  confidence: 0.79
  scoring_method: "hybrid_ai_assisted_review"
  scoring_signal_mode: "proxy_signal_mode"
  scoring_model_version: "q-point-scoring-model-v0.2"
  evaluation_status: "draft"
```

---

## 13. Pseudocode

```python
def calculate_q_point(session_data):
    # Main Q-Point components
    originality = compute_originality(session_data)
    depth = compute_depth(session_data)
    trace_persistence = compute_trace_persistence(session_data)

    # Catalyst C-vector components
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
            "component_weights": {
                "originality": 0.30,
                "depth": 0.25,
                "catalyst": 0.30,
                "trace_persistence": 0.15,
            },
        },
        "catalyst_vector": {
            "self_question_trigger": self_question_trigger,
            "confidence_shift": confidence_shift,
            "internal_conflict_detection": internal_conflict,
            "viewpoint_shift": viewpoint_shift,
            "catalyst_score": catalyst,
            "catalyst_weights": {
                "self_question_trigger": 0.35,
                "confidence_shift": 0.25,
                "internal_conflict_detection": 0.25,
                "viewpoint_shift": 0.15,
            },
        },
    }
```

---

## 14. Scoring Signal Modes

Q-Point scoring can be performed in three signal modes.

### 14.1 Internal Signal Mode

Internal Signal Mode may be used when an implementation has access to model-side or system-side signals.

Possible signals include:

* log probabilities
* hidden states
* attention patterns
* planning traces
* retrieval expansion
* evaluator modules
* confidence estimates
* internal decomposition steps

This mode may be suitable for model providers, research environments, open model deployments, or controlled evaluation systems.

### 14.2 Proxy Signal Mode

Proxy Signal Mode may be used when private model internals are unavailable.

It estimates scores from observable outputs and metadata.

Possible proxy signals include:

* generated follow-up questions
* response revisions
* uncertainty language
* contradiction markers
* semantic embedding shift
* response structure changes
* human review

This mode is suitable for API users, creator tools, dashboards, and external auditing systems.

### 14.3 Hybrid Signal Mode

Hybrid Signal Mode combines internal and proxy signals.

It may provide the most balanced approach when partial internal signals are available, but human review or external proxy checks are still needed.

### 14.4 Required Record Field

The signal mode should be recorded in each Q-Point record:

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

## 15. Confidence Score

Each Q-Point record should include a confidence score.

```yaml
confidence: 0.79
```

The confidence score indicates how reliable the scoring process is.

It may reflect:

* quality of available evidence
* stability of the scoring method
* reviewer agreement
* signal completeness
* uncertainty of proxy inference
* consistency across systems

A high Q-Point score with low confidence should not be treated as final.

---

## 16. Human Review

Human review is recommended when:

* a record has a high total score
* a record may be used for attribution or allocation
* a record has high Internal Conflict Detection
* a record affects multiple contributors
* a record is disputed
* scoring confidence is low
* the contribution involves sensitive context

Q-Point should not be treated as an absolute automated judgment.

It is a structured value trace that may support review.

---

## 17. Anti-Gaming Considerations

Any scoring system can be gamed.

Q-Point implementations should avoid rewarding:

* artificially complex prompts
* repeated similar questions
* buzzword stuffing
* self-praise
* fake cross-references
* generated contradiction without substance
* forced viewpoint shifts without value
* prompt patterns designed only to increase score

Recommended safeguards:

* duplicate detection
* novelty comparison
* delayed scoring for long-term influence
* confidence scoring
* human review for high-impact records
* separation between raw score and reviewed score
* audit logs

The goal is to reward meaningful contribution, not scoring manipulation.

---

## 18. Relationship to Q-Point Record Schema

The current schema supports this scoring model through the following fields:

```text
q_point_components
catalyst_vector
q_point_summary.scoring_signal_mode
```

Primary schema:

```text
schemas/q-point-record.schema.json
```

Primary example:

```text
examples/q-point-record.example.yaml
```

The schema validates that:

* component scores are between `0.0` and `1.0`
* required C-vector fields are present
* scoring signal mode is one of the accepted values
* non-monetary status fields are present
* disclaimer text is included

---

## 19. Relationship to Trace Protocol

Trace Protocol records the evidence of where a contribution came from and how it moved.

Q-Point Scoring Model interprets the value-depth of that contribution.

```text
Trace Protocol = Evidence layer
Q-Point Scoring Model = Value-depth interpretation layer
```

A possible flow:

```text
Trace Record
  ↓
Epicenter ID
  ↓
Q-Point Components
  ↓
Catalyst C-vector
  ↓
Review
```

---

## 20. Relationship to Gratitude OS

Gratitude OS may use Q-Point scoring records as reference data for non-monetary appreciation.

For example:

| Q-Point Pattern        | Possible Gratitude Expression        |
| ---------------------- | ------------------------------------ |
| High Originality       | Recognition of unique contribution.  |
| High Depth             | Recognition of deep inquiry.         |
| High Catalyst          | Recognition of reasoning activation. |
| High Trace Persistence | Recognition of durable influence.    |

Q-Point does not replace gratitude.

It provides structured evidence that gratitude systems may interpret.

---

## 21. Relationship to Royalty OS

Royalty OS may use reviewed Q-Point records as reference data for future allocation weights.

The C-vector may help distinguish different forms of contribution value.

| Catalyst Pattern | Possible Value Type         |
| ---------------- | --------------------------- |
| High `S`         | Inquiry expansion value.    |
| High `Δ`         | Assumption-shifting value.  |
| High `K`         | Conflict-resolution value.  |
| High `V`         | Perspective-shifting value. |

This does not imply automatic monetary allocation.

Any conversion from Q-Point records to royalty allocation requires a separate legal, contractual, governance, and review framework.

---

## 22. Interpretation

Q-Point v0.2 asks two questions.

First:

```text
How much did the contribution move AI-mediated reasoning?
```

Second:

```text
How did the contribution move AI-mediated reasoning?
```

The C-vector makes the second question visible.

A contribution may be valuable because it:

* caused new questions
* shifted uncertainty
* exposed contradiction
* changed viewpoint
* created a reusable structure
* persisted across records
* became a traceable intellectual epicenter

This makes Q-Point more than a score.

It becomes a map of intellectual motion.

---

## 23. Future Work

Future versions may add:

* empirical calibration methods
* cross-AI aggregation scoring
* reviewer agreement metrics
* decay and persistence models
* dashboard visualization schema
* pass / fail scoring examples
* score explanation fields
* dispute resolution fields
* cryptographic proof links
* privacy-preserving scoring methods
* zero-knowledge contribution verification

---

## 24. Summary

Q-Point Scoring Model v0.2 introduces a structured way to evaluate question-based intellectual contribution.

The overall Q-Point formula is:

```text
Q = 0.30O + 0.25D + 0.30C + 0.15T
```

The Catalyst C-vector formula is:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

Where:

* `O` = Originality
* `D` = Depth
* `C` = Catalyst
* `T` = Trace Persistence
* `S` = Self-Question Trigger
* `Δ` = Confidence Shift
* `K` = Internal Conflict Detection
* `V` = Viewpoint Shift

This model records not only that a contribution mattered, but how it moved AI-mediated reasoning.

Q-Point remains non-monetary.

It is a value trace, not a payment claim.

In v0.2, Catalyst becomes a structured record of intellectual movement.
