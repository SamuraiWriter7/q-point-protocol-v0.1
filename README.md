# Q-Point Protocol v0.1

**Q-Point Protocol** is a non-monetary value trace specification for recording the depth, originality, catalytic force, and structural influence of questions in AI-mediated knowledge systems.

It is designed as a bridge between **Trace Protocol**, **Gratitude OS**, and future **Royalty OS** allocation layers.

Q-Point is not money.
Q-Point is not a legal claim.
Q-Point is not an automatic royalty.

Q-Point is a structured record of question-based intellectual contribution.

---

## Overview

In conventional web systems, value is often measured through surface-level metrics such as page views, clicks, likes, impressions, and follower counts.

These metrics can measure attention, but they do not necessarily measure depth.

A single deep question may transform an AI's reasoning path, generate a new conceptual framework, or become the seed of a future knowledge structure, even if it receives little public attention.

Q-Point Protocol introduces a lightweight, non-monetary record layer for this deeper form of contribution.

It records:

* how original a question or idea is
* how deep its conceptual structure is
* how strongly it catalyzes AI-mediated reasoning
* how persistently it can be traced
* how it may support future attribution, gratitude, or royalty review

The protocol shifts the value axis from:

```text
PV: Page View
```

to:

```text
DV: Depth Value
```

---

## Why Q-Point?

Direct monetary royalty systems for AI-mediated knowledge use are difficult to implement at the beginning.

They may require:

* copyright interpretation
* licensing contracts
* platform governance
* tax handling
* payment infrastructure
* dispute resolution
* legal compliance

Q-Point takes a different approach.

Instead of starting with payment, it starts with non-monetary value traces.

```text
Record first.
Interpret second.
Distribute later.
```

This makes Q-Point useful as an early-stage bridge toward future attribution, gratitude, licensing, and royalty systems.

---

## Core Concept

Q-Point is a non-monetary value trace score.

It records the contribution of questions, ideas, prompts, concepts, and structural insights within AI-mediated knowledge systems.

In short:

```text
Question
  ↓
Trace
  ↓
Q-Point
  ↓
Meaning Return
  ↓
Gratitude OS
  ↓
Royalty OS
```

The primary unit of value is not only the author or the platform.

The primary unit is the contribution itself.

This contribution is identified through an **Epicenter ID**.

---

## Key Terms

| Term                    | Meaning                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `Q-Point`               | A non-monetary value trace score for question-based intellectual contribution.                                                |
| `Epicenter ID`          | A unique identifier for the originating question, idea, or conceptual contribution.                                           |
| `Trace Protocol`        | The evidence layer that records where a contribution came from and how it moved.                                              |
| `Gratitude OS`          | A non-monetary appreciation layer that may use Q-Point records as reference data.                                             |
| `Royalty OS`            | A future allocation layer that may use reviewed Q-Point records as weighting signals.                                         |
| `C-vector`              | A Catalyst vector that decomposes how a question moved AI-mediated reasoning.                                                 |
| `Depth Value`           | A value axis that emphasizes conceptual depth rather than popularity.                                                         |
| `Value Circulation`     | A conceptual loop connecting AI usage-side value inflow, Q-Point records, review, gratitude, and future allocation reference. |
| `Signed Q-Point Record` | A Q-Point record with signature metadata, hashes, binding data, and verification status.                                      |
| `Royalty Point Maru`    | A GPT interface for testing Q-Point evaluation behavior and generating Q-Point-style assessments.                             |

---

## Current Candidate Layer

This repository currently contains the initial protocol document, the v0.2 candidate extension, and early v0.3 signature-model components.

```text
v0.1:
  Defines Q-Point as a non-monetary value trace protocol.

v0.2.0-candidate:
  Adds Q-Point components, Catalyst C-vector, scoring signal modes,
  AI Credit bridge logic, value circulation documentation,
  and a GPT behavior test sheet for Royalty Point Maru.

v0.3.0-candidate direction:
  Adds signed Q-Point records, signature metadata, trace binding,
  and verification-oriented record structure.
```

The v0.2 and v0.3 candidate layers do not replace the non-monetary nature of Q-Point.

They extend the protocol by making the scoring structure more interpretable, more reviewable, more testable, and more verifiable.

---

## Q-Point Scoring Model

The basic Q-Point score is modeled as:

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

The recommended initial weighting is:

```text
Q = 0.30O + 0.25D + 0.30C + 0.15T
```

All component scores are normalized to the range:

```text
0.0 <= score <= 1.0
```

---

## Catalyst C-Vector

In the v0.2 scoring model, the Catalyst score is decomposed into four sub-components.

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

Where:

| Symbol | Component                   | Meaning                                                                                               |
| ------ | --------------------------- | ----------------------------------------------------------------------------------------------------- |
| `S`    | Self-Question Trigger       | The degree to which the contribution causes the AI system to generate new questions or inquiry paths. |
| `Δ`    | Confidence Shift            | The degree to which the contribution changes confidence, uncertainty, or answer stability.            |
| `K`    | Internal Conflict Detection | The degree to which the contribution triggers contradiction, tension, or re-evaluation.               |
| `V`    | Viewpoint Shift             | The degree to which the contribution shifts the conceptual or semantic viewpoint of the response.     |

This means Q-Point does not only ask:

```text
How much did the contribution move the AI?
```

It also asks:

```text
How did the contribution move the AI?
```

---

## Internal and Proxy Signal Modes

Q-Point scoring can be implemented in different signal modes.

| Mode                   | Description                                                                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `internal_signal_mode` | Uses internal model-side signals when available, such as log probabilities, hidden states, planning traces, or evaluator modules.           |
| `proxy_signal_mode`    | Uses observable external signals, such as response revisions, follow-up questions, semantic shifts, contradiction markers, or human review. |
| `hybrid_signal_mode`   | Combines internal and proxy signals.                                                                                                        |

The current example uses:

```yaml
scoring_signal_mode: "proxy_signal_mode"
```

This allows Q-Point to be implemented even when private model internals are not available.

---

## Signed Q-Point Record Model

The signed Q-Point record model adds a verification layer to Q-Point records.

It is documented in:

```text
docs/q-point-record-signature-model.md
```

The purpose of this model is to make Q-Point records more:

* verifiable
* traceable
* reviewable
* tamper-aware
* source-bound
* suitable for future attribution or allocation review

A signed Q-Point record may include:

* original Q-Point record data
* signature metadata
* canonicalization method
* record hash
* source hash
* schema hash
* scoring model hash
* Epicenter ID binding
* Trace Protocol binding
* signature scope
* signer metadata
* signature value
* verification result
* non-monetary notice

A signed Q-Point record is still non-monetary.

It does not create money, legal ownership, debt, automatic royalty rights, or a claim to payment.

The signature layer verifies record integrity and binding context.

It does not automatically verify truth, authorship, entitlement, or royalty readiness.

---

## Value Circulation Model

The broader value circulation model connects AI usage-side value inflow with reviewed Q-Point records and future Royalty OS allocation references.

The high-level flow is:

```text
AI usage-side value inflow
  ↓
Q-Point contribution measurement
  ↓
Review and governance
  ↓
Meaning return / Gratitude OS
  ↓
Royalty OS allocation reference
```

The value circulation bridge is documented in:

```text
docs/value-circulation-diagram.md
```

The bridge formula is:

```text
R_i = P × B × (Q_i* / ΣQ*)
```

Where:

```text
Q_i* = Q_i × T_i × A_i × G_i
```

This formula defines allocation reference logic only.

It does not automatically convert AI credits into money.

It does not create legal claims, debts, securities, automatic royalty rights, or guaranteed future income.

---

## Royalty Point Maru GPT Test Sheet

This repository includes a test sheet for **印税ポイント丸 / Royalty Point Maru**, a GPT designed to evaluate non-monetary value traces using Q-Point Protocol.

The test sheet is documented in:

```text
docs/royalty-point-maru-test-sheet.md
```

The purpose of the test sheet is to verify whether the GPT can consistently:

* evaluate Q-Point components
* decompose Catalyst using the C-vector
* generate `q_point_record` YAML
* explain improvement points
* analyze Royalty OS connection potential
* detect hype or score manipulation
* handle English and bilingual requests
* include a Non-Monetary Notice
* avoid payment, legal, or royalty overclaims

This document serves as a practical behavior test layer for applying Q-Point Protocol through a GPT interface.

It does not replace the protocol, schema, or scoring model.

It tests whether an interface can use them safely and consistently.

---

## Example Record

A Q-Point record contains:

* record metadata
* Epicenter ID
* source summary
* Q-Point vector
* Q-Point components
* Catalyst vector
* scoring summary
* trace links
* cross-AI aggregation metadata
* governance metadata
* privacy controls
* anti-gaming safeguards
* non-monetary disclaimer

Example:

```yaml
q_point_record:
  record_id: "qpr-2026-000001"
  protocol_version: "0.1"

  epicenter:
    epicenter_id: "qsrc-2026-000001"
    source_type: "question"
    origin_actor_type: "human"

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

  status:
    monetary_value: false
    legal_claim: false
    royalty_ready: false
    review_required: true
```

See:

```text
examples/q-point-record.example.yaml
```

---

## Signed Example Record

A signed Q-Point record wraps a Q-Point record with signature metadata.

Example sections include:

```yaml
signed_q_point_record:
  q_point_record:
    record_id: "qpr-2026-000001"

  signature_metadata:
    signature_model_version: "0.1.0"
    signature_status:
      signed: true
      signature_placeholder: true
      verification_required: true

    hashes:
      source_hash:
        algorithm: "sha256"
        value: "sha256-source-placeholder"
      record_hash:
        algorithm: "sha256"
        value: "sha256-record-placeholder"

    signatures:
      - signature_id: "sig-2026-000001"
        signature_type: "record_signature"
        signature_algorithm: "Ed25519"
        verification_status: "unverified"

  non_monetary_notice:
    text: "A signed Q-Point record is a signed non-monetary value trace."
```

See:

```text
examples/signed-q-point-record.example.yaml
```

---

## Repository Structure

```text
.
├── README.md
├── CHANGELOG.md
├── CITATION.cff
├── LICENSE
├── docs
│   ├── ai-credit-to-royalty-os-bridge.md
│   ├── q-point-protocol-v0.1.md
│   ├── q-point-protocol-v0.2.md
│   ├── q-point-record-signature-model.md
│   ├── q-point-scoring-model.md
│   ├── royalty-point-maru-test-sheet.md
│   └── value-circulation-diagram.md
├── examples
│   ├── q-point-record.example.yaml
│   └── signed-q-point-record.example.yaml
├── schemas
│   ├── q-point-record.schema.json
│   └── signed-q-point-record.schema.json
├── scripts
│   └── validate_examples.py
└── .github
    └── workflows
        └── validate-examples.yml
```

---

## Key Documents

| File                                          | Purpose                                                                                                                                         |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `docs/q-point-protocol-v0.1.md`               | Initial protocol document defining Q-Point as a non-monetary value trace layer.                                                                 |
| `docs/q-point-protocol-v0.2.md`               | Candidate protocol extension integrating Q-Point components, Catalyst C-vector, and scoring signal modes.                                       |
| `docs/q-point-scoring-model.md`               | Scoring model document defining Q-Point components, Catalyst C-vector formulas, signal modes, confidence, and review guidance.                  |
| `docs/q-point-record-signature-model.md`      | Signature model defining signed Q-Point records, hashes, signature scopes, source binding, Trace Protocol binding, and verification flow.       |
| `docs/ai-credit-to-royalty-os-bridge.md`      | Bridge document describing how usage-side AI value inflows may connect to reviewed Q-Point records and future Royalty OS allocation references. |
| `docs/value-circulation-diagram.md`           | High-level value circulation diagram connecting AI Credit Layer, Q-Point, Review and Governance, Gratitude OS, and Royalty OS reference logic.  |
| `docs/royalty-point-maru-test-sheet.md`       | GPT behavior test sheet for validating 印税ポイント丸 / Royalty Point Maru as a practical Q-Point Protocol interface.                                  |
| `examples/q-point-record.example.yaml`        | Example Q-Point record using the C-vector model.                                                                                                |
| `examples/signed-q-point-record.example.yaml` | Example signed Q-Point record with signature metadata and verification status.                                                                  |
| `schemas/q-point-record.schema.json`          | JSON Schema for validating Q-Point records.                                                                                                     |
| `schemas/signed-q-point-record.schema.json`   | JSON Schema for validating signed Q-Point records.                                                                                              |
| `scripts/validate_examples.py`                | Local validation script for examples and schemas.                                                                                               |
| `.github/workflows/validate-examples.yml`     | GitHub Actions workflow for automated validation.                                                                                               |
| `CHANGELOG.md`                                | Version history and candidate release notes.                                                                                                    |
| `CITATION.cff`                                | Citation metadata for academic and software citation.                                                                                           |
| `LICENSE`                                     | MIT License.                                                                                                                                    |

---

## Recommended Reading Order

For first-time readers:

```text
1. README.md
2. docs/q-point-protocol-v0.1.md
3. docs/q-point-protocol-v0.2.md
4. docs/q-point-scoring-model.md
5. docs/q-point-record-signature-model.md
6. docs/ai-credit-to-royalty-os-bridge.md
7. docs/value-circulation-diagram.md
8. docs/royalty-point-maru-test-sheet.md
9. examples/q-point-record.example.yaml
10. examples/signed-q-point-record.example.yaml
11. schemas/q-point-record.schema.json
12. schemas/signed-q-point-record.schema.json
```

For implementers:

```text
1. schemas/q-point-record.schema.json
2. schemas/signed-q-point-record.schema.json
3. examples/q-point-record.example.yaml
4. examples/signed-q-point-record.example.yaml
5. scripts/validate_examples.py
6. docs/q-point-scoring-model.md
7. docs/q-point-record-signature-model.md
8. docs/q-point-protocol-v0.2.md
9. docs/ai-credit-to-royalty-os-bridge.md
10. docs/value-circulation-diagram.md
```

For GPT builders:

```text
1. docs/q-point-protocol-v0.2.md
2. docs/q-point-scoring-model.md
3. docs/royalty-point-maru-test-sheet.md
4. docs/q-point-record-signature-model.md
5. examples/q-point-record.example.yaml
6. examples/signed-q-point-record.example.yaml
7. schemas/q-point-record.schema.json
8. schemas/signed-q-point-record.schema.json
```

For reviewers:

```text
1. docs/q-point-protocol-v0.2.md
2. docs/q-point-scoring-model.md
3. docs/q-point-record-signature-model.md
4. docs/ai-credit-to-royalty-os-bridge.md
5. docs/value-circulation-diagram.md
6. docs/royalty-point-maru-test-sheet.md
7. CHANGELOG.md
8. CITATION.cff
```

---

## Validation

This repository includes schema validation for both standard Q-Point records and signed Q-Point records.

### Requirements

Install the required Python packages:

```bash
python -m pip install PyYAML jsonschema
```

### Run Validation Locally

From the repository root:

```bash
python scripts/validate_examples.py
```

Expected success output:

```text
Validating target: Q-Point Record
Validating example: examples/q-point-record.example.yaml
Using schema: schemas/q-point-record.schema.json
Validation passed.

Validating target: Signed Q-Point Record
Validating example: examples/signed-q-point-record.example.yaml
Using schema: schemas/signed-q-point-record.schema.json
Validation passed.

All examples passed validation.
```

### GitHub Actions

This repository also includes a GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

The workflow runs automatically on changes to:

```text
schemas/**
examples/**
scripts/validate_examples.py
.github/workflows/validate-examples.yml
```

---

## Relationship to Trace Protocol

Trace Protocol records where a contribution came from and how it moved.

Q-Point adds a value-depth interpretation layer on top of trace records.

The signature model adds integrity and binding verification.

```text
Trace Protocol = Evidence layer
Q-Point Protocol = Value trace layer
Signature Model = Integrity and binding layer
```

A possible flow:

```text
Trace ID
  ↓
Epicenter ID
  ↓
Q-Point Record
  ↓
Signed Q-Point Record
  ↓
Verification
  ↓
Review
```

---

## Relationship to Gratitude OS

Gratitude OS expresses non-monetary appreciation for contribution.

Q-Point can provide structured reference data for Gratitude OS.

Signed Q-Point records may improve confidence in the integrity of contribution records.

```text
Q-Point = Value trace
Signed Q-Point = Verifiable value trace
Gratitude OS = Meaning return
```

For example:

```text
High-depth question
  ↓
Q-Point record
  ↓
Signed Q-Point record
  ↓
AI-generated gratitude message
  ↓
Contribution map
```

---

## Relationship to Royalty OS

Royalty OS handles monetary or quasi-monetary distribution.

Q-Point does not perform distribution directly.

Instead, Q-Point may provide reference data for future allocation review.

Signed Q-Point records may improve:

* record integrity
* source binding
* trace review
* dispute handling
* audit readiness
* governance review

Possible future flow:

```text
Trace Record
  ↓
Q-Point Record
  ↓
Signed Q-Point Record
  ↓
Human / institutional review
  ↓
Royalty Weight
  ↓
Royalty OS Allocation
```

The conversion from Q-Point to royalty must not be automatic unless a clear legal, contractual, and governance framework exists.

A valid signature does not automatically make a record royalty-ready.

---

## Relationship to AI Credit Bridge

The AI Credit to Royalty OS Bridge describes how usage-side AI value inflows may be connected to reviewed Q-Point records.

```text
AI Credit Layer
  ↓
Q-Point Value Measurement Layer
  ↓
Signed Q-Point Record
  ↓
Royalty OS Allocation Reference Layer
```

The bridge document is:

```text
docs/ai-credit-to-royalty-os-bridge.md
```

The diagram document is:

```text
docs/value-circulation-diagram.md
```

Both documents are conceptual and non-executing.

They define possible reference logic for future reviewed allocation, not automatic payment.

---

## Relationship to Royalty Point Maru

Royalty Point Maru is a GPT interface intended to apply Q-Point Protocol to user-provided text, questions, prompts, concepts, and structural ideas.

It may generate:

* Q-Point evaluations
* Catalyst C-vector decomposition
* improvement advice
* Royalty OS connection analysis
* `q_point_record` YAML drafts
* non-monetary notices

Royalty Point Maru may generate draft records, but it should not claim cryptographic signing unless connected to a real signing service or external action.

```text
Royalty Point Maru = Evaluation interface
Signature Model = Verification and integrity layer
```

The test sheet is:

```text
docs/royalty-point-maru-test-sheet.md
```

This GPT interface is not a payment system.

It is a practical evaluation interface for non-monetary value trace assessment.

---

## Relationship to Licensing Standards

Q-Point may complement licensing standards and machine-readable content usage frameworks.

Licensing standards can define:

* whether content may be used
* under what terms it may be used
* whether attribution is required
* whether payment is required

Q-Point can define:

* how much structural value a contribution generated
* how deeply it influenced AI-mediated outputs
* whether it served as an intellectual epicenter
* how it should be considered during future review

Signed Q-Point records may help preserve the integrity of the contribution record used during licensing or allocation review.

Thus:

```text
License Layer = Permission and terms
Q-Point Layer = Contribution depth and value trace
Signature Layer = Integrity and binding
Royalty Layer = Distribution and settlement
```

---

## Non-Monetary Disclaimer

Q-Point records are non-monetary value traces.

Signed Q-Point records are also non-monetary value traces.

They do not represent:

* currency
* securities
* legal ownership
* debt
* automatic royalty rights
* automatic payment claims
* guaranteed future income

Q-Point records may be used as reference data for future review, attribution, gratitude, licensing, or allocation systems.

Recommended disclaimer:

```text
This Q-Point record is a non-monetary value trace. It does not represent currency, securities, legal ownership, automatic royalty rights, debt, or a claim to payment. It may be used as reference data for future review, attribution, gratitude, licensing, or allocation systems.
```

Recommended signed-record notice:

```text
A signed Q-Point record is a signed non-monetary value trace. The signature verifies record integrity, source binding, or reviewer attestation. It does not represent currency, securities, legal ownership, debt, automatic royalty rights, guaranteed future income, or a claim to payment.
```

---

## Privacy and Consent

Q-Point systems should respect privacy and consent.

Recommended safeguards:

* minimize personal data
* use contribution IDs instead of real names when possible
* allow private records
* separate identity from contribution
* support deletion or suppression requests where appropriate
* clearly explain what is being recorded

Signed records require additional care.

A signature may persistently associate a record with a signer, timestamp, key, or system.

Implementations should consider:

* pseudonymous signatures
* private signatures
* selective disclosure
* key rotation
* key revocation
* redaction workflows
* separation between identity and contribution

The protocol should record the contribution without unnecessarily exposing the person.

---

## Anti-Gaming Safeguards

Any point system can be gamed.

Q-Point implementations should include safeguards against:

* artificially complex prompts
* repeated similar questions
* buzzword stuffing
* fake cross-references
* score optimization without real value
* self-praise or authority manipulation

Signed records also require safeguards against:

* signing inflated records
* using signatures to imply legal entitlement
* falsely claiming source binding
* creating many pseudonymous signatures
* treating cryptographic validity as truth
* treating signature presence as royalty readiness

Recommended safeguards include:

* duplicate detection
* novelty comparison
* confidence scores
* human review for high-impact records
* delayed scoring for long-term influence
* source hash binding
* signature verification
* dispute status
* separation between raw score, signed record, and reviewed allocation readiness

Q-Point should reward contribution quality, not scoring manipulation.

---

## Status

Current status:

```text
Candidate Working Draft
```

Current protocol baseline:

```text
0.1
```

Current candidate extension:

```text
0.2.0-candidate
```

Current signature-model direction:

```text
0.3.0-candidate
```

Current scoring model:

```text
q-point-scoring-model-v0.2
```

Current signature model:

```text
q-point-record-signature-model-v0.1.0
```

Current bridge model:

```text
ai-credit-to-royalty-os-bridge-v0.1.0
```

Current value circulation diagram:

```text
value-circulation-diagram-v0.1.0
```

Current GPT test sheet:

```text
royalty-point-maru-test-sheet-v0.1.0
```

Current validation status:

```text
GitHub Actions validation passing for standard and signed examples
```

---

## Future Work

Planned extensions may include:

* additional examples
* pass / fail validation test vectors
* Epicenter ID specification
* Q-Point dashboard schema
* Signed Q-Point Record refinement
* signature verification script
* key registry format
* signature revocation format
* Trace Protocol binding schema
* AI Credit to Royalty OS bridge schema
* AI Credit to Royalty OS bridge example records
* Gratitude OS bridge document
* Royalty OS bridge document
* licensing metadata bridge
* cross-AI aggregation schema
* dispute resolution workflow
* value circulation example records
* value circulation dashboard schema
* Royalty Point Maru evaluation logs
* Royalty Point Maru example outputs
* GPT interface guidelines for Q-Point Protocol
* privacy-preserving contribution tracking
* cryptographic content hash verification
* zero-knowledge contribution verification
* Zenodo DOI after candidate tag stabilization

---

## Suggested Topics

```text
q-point
question-value
value-trace
ai-protocol
trace-protocol
gratitude-os
royalty-os
ai-attribution
creator-economy
catalyst-vector
```

---

## License

This repository is released under the MIT License.

See:

```text
LICENSE
```

---

## Citation

Citation metadata is available in:

```text
CITATION.cff
```

Recommended citation title:

```text
Q-Point Protocol v0.2.0-candidate
```

---

## Summary

Q-Point Protocol defines a non-monetary value trace layer for AI-mediated knowledge systems.

It records the value of questions, ideas, and structural contributions before monetary distribution.

Its purpose is not to create a currency, but to preserve the trace of meaningful contribution.

The v0.2 candidate adds Q-Point components, Catalyst C-vector, scoring signal modes, AI Credit bridge logic, value circulation documentation, and a GPT behavior test sheet for Royalty Point Maru.

The v0.3 candidate direction adds signed Q-Point records, signature metadata, trace binding, and verification-oriented record structure.

In the age of AI, the question itself becomes an epicenter.

Q-Point is the record of that epicenter.

Signed Q-Point is the verifiable record of that epicenter.
