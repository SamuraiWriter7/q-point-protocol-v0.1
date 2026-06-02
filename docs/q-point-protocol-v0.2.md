# Q-Point Protocol v0.2

**Status:** Candidate Working Draft
**Version:** 0.2.0-candidate
**Date:** 2026-06-02
**Category:** Non-Monetary Value Trace / AI-Mediated Knowledge Protocol
**Primary Schema:** `schemas/q-point-record.schema.json`
**Primary Example:** `examples/q-point-record.example.yaml`
**Related Documents:**

* `docs/q-point-protocol-v0.1.md`
* `docs/q-point-scoring-model.md`

---

## 1. Purpose

Q-Point Protocol v0.2 defines a non-monetary value trace protocol for recording question-based intellectual contribution in AI-mediated knowledge systems.

The purpose of this protocol is to record not only that a question, idea, prompt, concept, or structural insight contributed value, but also how that contribution moved AI-mediated reasoning.

Version 0.2 introduces the **Catalyst C-vector**, a structured scoring layer that decomposes catalytic influence into multiple components.

This allows Q-Point to function as:

* a contribution record
* a depth-value signal
* a traceable intellectual epicenter record
* a non-monetary meaning return layer
* a future reference layer for attribution, gratitude, licensing, or royalty review

Q-Point is designed to operate before monetary allocation.

It records value first.

It does not execute payment.

---

## 2. Core Definition

**Q-Point** is a non-monetary value trace score for recording the depth, originality, catalytic force, and trace persistence of question-based intellectual contribution within AI-mediated knowledge systems.

Q-Point records may be used as structured reference data for future systems, but they do not create legal rights or automatic financial claims.

In short:

```text
Q-Point = Non-monetary value trace of question-based intellectual contribution
```

---

## 3. Non-Monetary Status

Q-Point is not money.

Q-Point is not a currency.

Q-Point is not a crypto asset.

Q-Point is not a security.

Q-Point is not a debt.

Q-Point is not a legal claim.

Q-Point is not an automatic royalty.

Q-Point is not a guarantee of future income.

Q-Point is a structured record of intellectual contribution.

Recommended disclaimer:

```text
This Q-Point record is a non-monetary value trace. It does not represent currency, securities, legal ownership, automatic royalty rights, debt, or a claim to payment. It may be used as reference data for future review, attribution, gratitude, licensing, or allocation systems.
```

This disclaimer should be included in any implementation that displays Q-Point records to users.

---

## 4. Background

Most web-based value systems measure surface attention.

Common indicators include:

* page views
* likes
* clicks
* impressions
* shares
* follower counts
* sales
* subscriptions

These signals may measure visibility, but they do not necessarily measure depth.

A question may receive little public attention and still produce a major conceptual shift in an AI-mediated reasoning process.

A single idea may:

* generate a reusable framework
* change the direction of analysis
* reveal hidden contradictions
* trigger new inquiry paths
* become the seed of a protocol
* persist across future outputs

Q-Point Protocol exists to record this deeper form of value.

It shifts the evaluation axis from:

```text
PV: Page View
```

to:

```text
DV: Depth Value
```

---

## 5. Design Principles

Q-Point Protocol v0.2 is based on the following principles.

### 5.1 Record First

The protocol begins by recording contribution traces.

It does not begin with payment.

```text
Record first.
Interpret second.
Distribute later.
```

### 5.2 Non-Monetary First

Q-Point must remain non-monetary at the protocol layer.

Any future monetary or quasi-monetary allocation requires a separate legal, contractual, governance, and review framework.

### 5.3 Contribution-Centered

The primary unit of value is the contribution.

The contribution may be:

* a question
* a prompt
* an idea
* a concept
* a document
* a protocol
* a conversation
* a structural insight

The contributor may be human, AI, organizational, hybrid, or unknown, but the protocol should first identify the contribution itself.

### 5.4 Traceable

Every Q-Point record should be connected to an Epicenter ID or equivalent source identifier.

This allows contribution records to persist across time, platforms, and future review systems.

### 5.5 Interpretable

Q-Point should not be a black-box score.

The protocol should expose scoring components, confidence, signal mode, and review status.

### 5.6 Anti-Gaming

Q-Point should reward meaningful contribution, not scoring manipulation.

The protocol should include safeguards against shallow optimization, duplicated prompts, artificial complexity, and false novelty.

---

## 6. Q-Point Lifecycle

The Q-Point lifecycle has three phases.

### Phase 1: Value Trace Recording

A question, idea, or structural contribution is recorded as a value trace.

At this stage, no monetary value is assigned.

```text
Question → Trace → Q-Point Record
```

### Phase 2: Meaning Return

The contribution record may be visualized or interpreted.

This allows the contributor to see how their question or idea affected AI-mediated reasoning.

Possible outputs include:

* contribution map
* concept graph
* Q-Point dashboard
* C-vector visualization
* gratitude message
* trace history

This phase provides non-monetary meaning return.

```text
Q-Point Record → Meaning Return
```

### Phase 3: Future Allocation Reference

Reviewed Q-Point records may later serve as reference data for:

* attribution
* gratitude
* licensing
* royalty weighting
* institutional recognition
* creator economy systems
* AI-mediated value distribution

Q-Point does not execute allocation by itself.

```text
Q-Point Record → Review → Allocation Reference
```

---

## 7. Epicenter ID

An **Epicenter ID** identifies the originating contribution.

The purpose of the Epicenter ID is to record the source of value without reducing the protocol to user popularity or platform identity.

Example:

```yaml
epicenter:
  epicenter_id: "qsrc-2026-000001"
  source_type: "question"
  source_hash: "sha256-example-placeholder"
  origin_actor_type: "human"
  origin_platform: "chat_interface"
  origin_language: "en"
  created_at: "2026-06-02T09:00:00+09:00"
```

The Epicenter ID should remain stable wherever possible.

It may be connected to:

* trace records
* source hashes
* content references
* contribution signatures
* cross-AI aggregation records
* future attribution systems

---

## 8. Q-Point Record Structure

A Q-Point record should include the following sections:

| Section              | Purpose                                           |
| -------------------- | ------------------------------------------------- |
| `record_id`          | Unique identifier for the Q-Point record.         |
| `protocol_version`   | Protocol version used by the record.              |
| `epicenter`          | Source contribution metadata.                     |
| `source`             | Human-readable source summary.                    |
| `q_point_vector`     | Broad value vector.                               |
| `q_point_components` | Main scoring components used to compute Q-Point.  |
| `catalyst_vector`    | Decomposed Catalyst C-vector.                     |
| `q_point_summary`    | Total score, confidence, method, and signal mode. |
| `trace_links`        | Related trace and reference records.              |
| `cross_ai`           | Cross-AI aggregation metadata.                    |
| `status`             | Monetary, legal, review, and dispute status.      |
| `governance`         | Reviewer and dispute metadata.                    |
| `privacy`            | Privacy and identity handling.                    |
| `anti_gaming`        | Anti-manipulation safeguards.                     |
| `disclaimer`         | Non-monetary disclaimer.                          |
| `notes`              | Implementation or evaluator notes.                |

Primary example:

```text
examples/q-point-record.example.yaml
```

Primary schema:

```text
schemas/q-point-record.schema.json
```

---

## 9. Q-Point Vector

The `q_point_vector` records broad value dimensions.

Required core dimensions:

| Field             | Meaning                                                                       |
| ----------------- | ----------------------------------------------------------------------------- |
| `originality`     | Distinctiveness or non-derivative quality of the contribution.                |
| `depth`           | Conceptual, structural, philosophical, or technical depth.                    |
| `catalyst`        | Degree to which the contribution moves AI-mediated reasoning.                 |
| `structurality`   | Ability to become a reusable framework, protocol, model, or architecture.     |
| `resonance`       | Degree of connection to broader systems, communities, or future developments. |
| `reuse_potential` | Likelihood that the contribution can be reused in later outputs or systems.   |

Optional dimensions may include:

* `clarity`
* `traceability`
* `ethical_alignment`
* `cross_ai_relevance`
* `long_term_value`

All scores must be normalized to:

```text
0.0 <= score <= 1.0
```

---

## 10. Q-Point Components

Version 0.2 introduces `q_point_components`.

These are the main components used for Q-Point calculation.

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
```

The recommended formula is:

```text
Q = 0.30O + 0.25D + 0.30C + 0.15T
```

Where:

| Symbol | Field               | Meaning                                 |
| ------ | ------------------- | --------------------------------------- |
| `O`    | `originality`       | Originality of the contribution.        |
| `D`    | `depth`             | Depth of the contribution.              |
| `C`    | `catalyst`          | Catalyst score derived from C-vector.   |
| `T`    | `trace_persistence` | Persistence and traceability over time. |

The weights should sum to:

```text
1.0
```

---

## 11. Catalyst C-Vector

The Catalyst score is decomposed into the C-vector.

```yaml
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
```

The recommended formula is:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

Where:

| Symbol | Field                         | Meaning                                                                       |
| ------ | ----------------------------- | ----------------------------------------------------------------------------- |
| `S`    | `self_question_trigger`       | Whether the contribution causes new questions or inquiry paths.               |
| `Δ`    | `confidence_shift`            | Whether the contribution shifts confidence, uncertainty, or answer stability. |
| `K`    | `internal_conflict_detection` | Whether the contribution triggers contradiction, tension, or re-evaluation.   |
| `V`    | `viewpoint_shift`             | Whether the contribution shifts the conceptual or semantic viewpoint.         |

The Catalyst score records not only the strength of influence, but the direction and type of intellectual movement.

---

## 12. Scoring Signal Mode

Version 0.2 introduces `scoring_signal_mode`.

This field describes how the score was generated.

Allowed values:

```text
internal_signal_mode
proxy_signal_mode
hybrid_signal_mode
```

Example:

```yaml
q_point_summary:
  scoring_signal_mode: "proxy_signal_mode"
```

### 12.1 Internal Signal Mode

Internal Signal Mode may use model-side or system-side signals such as:

* log probabilities
* hidden states
* attention patterns
* planning traces
* retrieval expansion
* evaluator modules
* confidence estimates
* internal decomposition steps

This mode is suitable for model providers, research systems, or controlled environments.

### 12.2 Proxy Signal Mode

Proxy Signal Mode may use externally observable signals such as:

* generated follow-up questions
* visible answer revisions
* uncertainty language
* contradiction markers
* semantic embedding shift
* response structure changes
* human review

This mode is suitable for API users, creator tools, external dashboards, and audit systems.

### 12.3 Hybrid Signal Mode

Hybrid Signal Mode combines internal and proxy signals.

This mode may be useful where partial model-side data is available but still requires external review or interpretation.

---

## 13. Q-Point Summary

The `q_point_summary` section records the total score and scoring metadata.

Example:

```yaml
q_point_summary:
  total_score: 0.84
  confidence: 0.79
  scoring_method: "hybrid_ai_assisted_review"
  scoring_signal_mode: "proxy_signal_mode"
  scoring_model_version: "q-point-scoring-model-v0.2"
  evaluation_status: "draft"
```

Required concepts:

| Field                   | Meaning                          |
| ----------------------- | -------------------------------- |
| `total_score`           | Final normalized Q-Point score.  |
| `confidence`            | Reliability of the score.        |
| `scoring_method`        | Evaluation method used.          |
| `scoring_signal_mode`   | Type of signal used for scoring. |
| `scoring_model_version` | Scoring model version.           |
| `evaluation_status`     | Review status of the record.     |

A high Q-Point score with low confidence should not be treated as final.

---

## 14. Cross-AI Aggregation

Q-Point records may include cross-AI aggregation metadata.

Example:

```yaml
cross_ai:
  aggregation_enabled: true
  aggregation_method: "weighted_average_with_review"
  participating_systems:
    - system_name: "AI-System-A"
      local_q_point_score: 0.82
      confidence: 0.76
    - system_name: "AI-System-B"
      local_q_point_score: 0.79
      confidence: 0.72
    - system_name: "AI-System-C"
      local_q_point_score: 0.87
      confidence: 0.81
  aggregate_score: 0.83
```

Cross-AI aggregation should remain transparent.

Different AI systems may produce different evaluations.

The protocol should preserve disagreement rather than forcing artificial uniformity.

---

## 15. Status Fields

The `status` section clarifies legal, monetary, and review status.

Example:

```yaml
status:
  monetary_value: false
  legal_claim: false
  royalty_ready: false
  review_required: true
  reviewed: false
  disputed: false
```

Recommended interpretation:

| Field             | Meaning                                                                         |
| ----------------- | ------------------------------------------------------------------------------- |
| `monetary_value`  | Whether the record itself represents monetary value. Should usually be `false`. |
| `legal_claim`     | Whether the record asserts a legal claim. Should usually be `false`.            |
| `royalty_ready`   | Whether the record is ready for royalty review.                                 |
| `review_required` | Whether human or institutional review is required.                              |
| `reviewed`        | Whether review has been completed.                                              |
| `disputed`        | Whether the record is disputed.                                                 |

---

## 16. Governance

Governance metadata may include:

```yaml
governance:
  reviewer_type: "none"
  reviewer_id: null
  dispute_status: "none"
  version_status: "working_draft"
```

Possible reviewer types:

* `none`
* `ai`
* `human`
* `hybrid`
* `organization`

Possible dispute statuses:

* `none`
* `open`
* `under_review`
* `resolved`
* `rejected`

Q-Point should not be treated as an absolute automated judgment.

High-impact records should be reviewable.

---

## 17. Privacy

Q-Point systems should minimize personal data.

Recommended privacy fields:

```yaml
privacy:
  personal_data_minimized: true
  public_record: false
  identity_disclosure: "pseudonymous_or_private"
  deletion_request_supported: true
```

Recommended safeguards:

* record the contribution, not unnecessary personal identity
* use contribution IDs when possible
* support private records
* support deletion or suppression requests where appropriate
* separate contributor identity from contribution record
* clearly explain what is being recorded

---

## 18. Anti-Gaming

Any point system can be manipulated.

Q-Point records should include anti-gaming safeguards.

Example:

```yaml
anti_gaming:
  duplicate_check_required: true
  novelty_check_required: true
  high_score_human_review_required: true
  delayed_influence_scoring: true
```

Q-Point implementations should avoid rewarding:

* artificially complex prompts
* repeated similar questions
* buzzword stuffing
* self-praise
* fake cross-references
* forced contradiction without value
* artificial viewpoint shift
* prompt patterns designed only to increase score

The goal is contribution quality, not score optimization.

---

## 19. Validation

Q-Point records should be validated against the JSON Schema.

Primary schema:

```text
schemas/q-point-record.schema.json
```

Primary example:

```text
examples/q-point-record.example.yaml
```

Local validation:

```bash
python scripts/validate_examples.py
```

Expected success output:

```text
Validating example: examples/q-point-record.example.yaml
Using schema: schemas/q-point-record.schema.json
Validation passed.

All examples passed validation.
```

GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

---

## 20. Relationship to Q-Point Protocol v0.1

Q-Point Protocol v0.1 introduced the basic concept of non-monetary value traces for question-based intellectual contribution.

Version 0.2 extends v0.1 by adding:

* `q_point_components`
* `catalyst_vector`
* `scoring_signal_mode`
* C-vector scoring
* internal / proxy / hybrid signal modes
* clearer scoring interpretation
* stronger validation structure

Conceptual shift:

```text
v0.1:
  Records that a contribution generated value.

v0.2:
  Records how the contribution moved AI-mediated reasoning.
```

---

## 21. Relationship to Q-Point Scoring Model

This protocol document defines the overall Q-Point record structure and governance context.

The detailed scoring model is defined in:

```text
docs/q-point-scoring-model.md
```

That document should be used for:

* scoring formulas
* component interpretation
* Catalyst C-vector calculation
* signal modes
* scoring confidence
* human review guidance

---

## 22. Relationship to Trace Protocol

Trace Protocol records evidence.

Q-Point Protocol interprets value-depth.

```text
Trace Protocol = Evidence layer
Q-Point Protocol = Value trace layer
```

Possible flow:

```text
Trace Record
  ↓
Epicenter ID
  ↓
Q-Point Record
  ↓
Review
  ↓
Meaning Return or Future Allocation Reference
```

Trace Protocol answers:

```text
Where did this contribution come from?
```

Q-Point Protocol answers:

```text
What kind of value did this contribution generate?
```

---

## 23. Relationship to Gratitude OS

Gratitude OS expresses non-monetary appreciation.

Q-Point Protocol provides structured value traces that Gratitude OS may use.

```text
Q-Point = Value trace
Gratitude OS = Meaning return
```

Possible flow:

```text
High-depth question
  ↓
Q-Point Record
  ↓
Gratitude Message
  ↓
Contribution Map
```

Q-Point does not replace gratitude.

It supports gratitude with structured evidence.

---

## 24. Relationship to Royalty OS

Royalty OS handles monetary or quasi-monetary allocation.

Q-Point Protocol does not execute allocation directly.

Q-Point records may become reference data for future allocation review.

```text
Q-Point = Contribution weight signal
Royalty OS = Allocation execution layer
```

Possible future flow:

```text
Trace Record
  ↓
Q-Point Record
  ↓
Human / institutional review
  ↓
Royalty Weight
  ↓
Royalty OS Allocation
```

Any conversion from Q-Point to royalty requires separate legal, contractual, governance, and review frameworks.

---

## 25. Relationship to Licensing Standards

Licensing standards may define:

* whether content may be used
* under what terms it may be used
* whether attribution is required
* whether payment is required
* how permissions are expressed

Q-Point Protocol may define:

* how much structural value a contribution generated
* how deeply it influenced AI-mediated outputs
* whether it served as an intellectual epicenter
* how it should be considered during future review

Layer relationship:

```text
License Layer = Permission and terms
Q-Point Layer = Contribution depth and value trace
Royalty Layer = Distribution and settlement
```

---

## 26. Implementation Levels

Q-Point Protocol may be implemented at different levels.

### 26.1 Minimal Implementation

A minimal implementation requires:

* `record_id`
* `protocol_version`
* `created_at`
* `epicenter`
* `source`
* `q_point_vector`
* `q_point_components`
* `catalyst_vector`
* `q_point_summary`
* `status`
* `disclaimer`

### 26.2 Review-Oriented Implementation

A review-oriented implementation should also include:

* `trace_links`
* `governance`
* `privacy`
* `anti_gaming`
* `notes`

### 26.3 Cross-AI Implementation

A cross-AI implementation should include:

* `cross_ai`
* participating systems
* local scores
* aggregate score
* aggregation method
* confidence values

---

## 27. Example Minimal Record

```yaml
q_point_record:
  record_id: "qpr-2026-000001"
  protocol_version: "0.1"
  created_at: "2026-06-02T09:10:00+09:00"

  epicenter:
    epicenter_id: "qsrc-2026-000001"
    source_type: "question"
    origin_actor_type: "human"
    origin_platform: "chat_interface"

  source:
    title: "Can AI record the value of questions before monetary royalty?"
    summary: "A question proposing Q-Point as a non-monetary bridge toward future royalty systems."

  q_point_vector:
    originality: 0.86
    depth: 0.90
    catalyst: 0.81
    structurality: 0.88
    resonance: 0.76
    reuse_potential: 0.72

  q_point_components:
    originality: 0.86
    depth: 0.90
    catalyst: 0.81
    trace_persistence: 0.74

  catalyst_vector:
    self_question_trigger: 0.88
    confidence_shift: 0.76
    internal_conflict_detection: 0.82
    viewpoint_shift: 0.72
    catalyst_score: 0.81

  q_point_summary:
    total_score: 0.84
    confidence: 0.79
    scoring_method: "hybrid_ai_assisted_review"
    scoring_signal_mode: "proxy_signal_mode"
    scoring_model_version: "q-point-scoring-model-v0.2"
    evaluation_status: "draft"

  status:
    monetary_value: false
    legal_claim: false
    royalty_ready: false
    review_required: true
    reviewed: false
    disputed: false

  disclaimer:
    text: "This Q-Point record is a non-monetary value trace. It does not represent currency, securities, legal ownership, automatic royalty rights, debt, or a claim to payment."
```

---

## 28. Future Work

Future versions may add:

* Q-Point Protocol v0.3
* Epicenter ID specification
* Cross-AI aggregation schema
* Dashboard metadata schema
* Gratitude OS bridge document
* Royalty OS bridge document
* licensing metadata bridge document
* dispute resolution workflow
* pass / fail validation examples
* score explanation fields
* decay and persistence model
* cryptographic proof records
* privacy-preserving scoring
* zero-knowledge contribution verification

---

## 29. Summary

Q-Point Protocol v0.2 defines a non-monetary value trace protocol for AI-mediated knowledge systems.

It records question-based intellectual contribution through:

* Q-Point vector
* Q-Point components
* Catalyst C-vector
* scoring signal mode
* trace links
* governance metadata
* privacy safeguards
* anti-gaming controls
* non-monetary disclaimer

The key advancement of v0.2 is the Catalyst C-vector.

It allows Q-Point to record not only that a contribution mattered, but how it moved AI-mediated reasoning.

Q-Point remains non-monetary.

It is a value trace, not a payment claim.

In v0.2, the question becomes not only a source of meaning, but a traceable epicenter of intellectual movement.
