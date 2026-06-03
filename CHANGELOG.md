# Changelog

All notable changes to this project will be documented in this file.

This project follows a lightweight versioning approach during the Working Draft phase.

---

## [v0.2.0-candidate] - 2026-06-02

### Added

* Added Catalyst C-vector support to the Q-Point record model.

* Added `q_point_components` to represent the main Q-Point scoring components:

  * `originality`
  * `depth`
  * `catalyst`
  * `trace_persistence`

* Added `catalyst_vector` to represent how a contribution moves AI-mediated reasoning:

  * `self_question_trigger`
  * `confidence_shift`
  * `internal_conflict_detection`
  * `viewpoint_shift`
  * `catalyst_score`

* Added `component_weights` for the main Q-Point scoring formula.

* Added `catalyst_weights` for the C-vector scoring formula.

* Added `scoring_signal_mode` to distinguish between:

  * `internal_signal_mode`
  * `proxy_signal_mode`
  * `hybrid_signal_mode`

* Added C-vector related concepts to the example record.

* Added the v0.2 candidate protocol document:

  * `docs/q-point-protocol-v0.2.md`

* Added the formal scoring model document:

  * `docs/q-point-scoring-model.md`

* Added the AI Credit to Royalty OS bridge document:

  * `docs/ai-credit-to-royalty-os-bridge.md`

* Added the value circulation diagram document:

  * `docs/value-circulation-diagram.md`

* Added the Royalty Point Maru GPT behavior test sheet:

  * `docs/royalty-point-maru-test-sheet.md`

* Added README documentation for:

  * Q-Point overview
  * v0.2 candidate layer
  * Catalyst C-vector
  * Internal and Proxy Signal Modes
  * Value Circulation Model
  * Royalty Point Maru GPT test sheet
  * Validation workflow
  * Relationship to Trace Protocol, Gratitude OS, Royalty OS, and licensing standards
  * AI Credit to Royalty OS bridge

* Added GitHub Actions validation workflow for Q-Point examples:

  * `.github/workflows/validate-examples.yml`

* Added local validation script:

  * `scripts/validate_examples.py`

* Added citation metadata:

  * `CITATION.cff`

* Added MIT License:

  * `LICENSE`

### Updated

* Updated `examples/q-point-record.example.yaml` with C-vector fields.

* Updated `schemas/q-point-record.schema.json` to validate:

  * `q_point_components`
  * `catalyst_vector`
  * `scoring_signal_mode`

* Updated `README.md` to reflect the current repository structure.

* Updated `README.md` Key Documents section to include:

  * `docs/q-point-protocol-v0.2.md`
  * `docs/q-point-scoring-model.md`
  * `docs/ai-credit-to-royalty-os-bridge.md`
  * `docs/value-circulation-diagram.md`
  * `docs/royalty-point-maru-test-sheet.md`

* Updated `README.md` Recommended Reading Order for:

  * first-time readers
  * implementers
  * GPT builders
  * reviewers

* Updated `README.md` Future Work section to include:

  * AI Credit to Royalty OS bridge schema
  * AI Credit to Royalty OS bridge example records
  * value circulation example records
  * value circulation dashboard schema
  * Royalty Point Maru evaluation logs
  * Royalty Point Maru example outputs
  * GPT interface guidelines for Q-Point Protocol

* Updated validation instructions for local and GitHub Actions usage.

* Updated the Q-Point model from a simple value trace record toward a C-vector compatible scoring structure.

* Updated project metadata toward `v0.2.0-candidate`.

### Validation

* GitHub Actions validation is passing for:

  * `examples/q-point-record.example.yaml`
  * `schemas/q-point-record.schema.json`
  * `scripts/validate_examples.py`
  * `.github/workflows/validate-examples.yml`

### Bridge Model

This candidate release introduces the first bridge document connecting usage-side AI value inflows to reviewed Q-Point records and future Royalty OS allocation references.

The bridge is defined in:

```text
docs/ai-credit-to-royalty-os-bridge.md
```

The bridge model introduces the following conceptual flow:

```text
AI Credit Layer
  ↓
Q-Point Value Measurement Layer
  ↓
Royalty OS Allocation Reference Layer
```

The recommended reference formula is:

```text
R_i = P × B × (Q_i* / ΣQ*)
```

Where:

```text
Q_i* = Q_i × T_i × A_i × G_i
```

This bridge does not automatically convert AI credits into money.

It does not create legal claims, debts, securities, automatic royalty rights, or guaranteed future income.

It defines a possible reference model for future reviewed allocation.

### Value Circulation Diagram

This candidate release adds a value circulation diagram document that visualizes the broader Q-Point ecosystem.

The diagram is defined in:

```text
docs/value-circulation-diagram.md
```

The value circulation model connects:

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

The diagram clarifies how Q-Point Protocol, AI Credit Bridge, Gratitude OS, and Royalty OS may connect into a non-monetary, review-first value circulation architecture.

This diagram is conceptual.

It does not define an automatic payment system.

It does not create legal claims, debts, securities, automatic royalty rights, or guaranteed future income.

### Royalty Point Maru Test Sheet

This candidate release adds a GPT behavior test sheet for **印税ポイント丸 / Royalty Point Maru**.

The test sheet is defined in:

```text
docs/royalty-point-maru-test-sheet.md
```

The test sheet is designed to verify whether a GPT interface can consistently apply Q-Point Protocol behavior.

It checks whether the GPT can:

* evaluate Q-Point components
* decompose Catalyst using the C-vector
* generate `q_point_record` YAML
* provide improvement advice
* analyze Royalty OS connection potential
* detect hype or score manipulation
* handle English and bilingual requests
* include a Non-Monetary Notice
* avoid monetary, legal, and automatic royalty overclaims

This document does not replace the protocol, schema, or scoring model.

It provides a practical behavior test layer for applying Q-Point Protocol through a GPT interface.

### Notes

This candidate release introduces the first structured C-vector model for Catalyst scoring.

The main conceptual shift is:

```text
Q-Point v0.1:
  Records question-based intellectual contribution.

Q-Point v0.2-candidate:
  Records not only that a contribution moved AI-mediated reasoning,
  but how it moved that reasoning.
```

The C-vector allows Catalyst to be decomposed into:

```text
C = 0.35S + 0.25Δ + 0.25K + 0.15V
```

Where:

* `S` = Self-Question Trigger
* `Δ` = Confidence Shift
* `K` = Internal Conflict Detection
* `V` = Viewpoint Shift

This version remains non-monetary.

Q-Point records do not represent currency, securities, legal ownership, debt, automatic royalty rights, or a claim to payment.

---

## [v0.1.0] - 2026-06-02

### Added

* Added initial Q-Point Protocol documentation:

  * `docs/q-point-protocol-v0.1.md`

* Defined Q-Point as a non-monetary value trace score for question-based intellectual contribution.

* Introduced the basic Q-Point lifecycle:

  * Internal Value Trace
  * Visualization and Meaning Return
  * Future Allocation Reference

* Introduced the core Q-Point vector dimensions:

  * `originality`
  * `depth`
  * `catalyst`
  * `structurality`
  * `resonance`
  * `reuse_potential`

* Introduced optional dimensions:

  * `clarity`
  * `traceability`
  * `ethical_alignment`
  * `cross_ai_relevance`
  * `long_term_value`

* Introduced Epicenter ID as a contribution-centered identifier.

* Added initial Q-Point example record:

  * `examples/q-point-record.example.yaml`

* Added initial JSON Schema:

  * `schemas/q-point-record.schema.json`

* Added non-monetary disclaimer requirements.

* Added initial relationship notes for:

  * Trace Protocol
  * Gratitude OS
  * Royalty OS
  * licensing standards

* Added privacy, consent, anti-gaming, and governance considerations.

### Notes

This release establishes Q-Point as a non-monetary value trace layer.

Its purpose is to record meaningful contribution before monetary distribution.

Core principle:

```text
Record first.
Interpret second.
Distribute later.
```

---

## [Unreleased]

### Planned

* Add pass / fail validation examples.
* Add Epicenter ID specification.
* Add Cross-AI Aggregation schema.
* Add Gratitude OS bridge document.
* Add Royalty OS bridge document.
* Add licensing metadata bridge document.
* Add dashboard metadata schema.
* Add AI Credit to Royalty OS bridge schema.
* Add AI Credit to Royalty OS bridge example records.
* Add value circulation example records.
* Add value circulation dashboard schema.
* Add Royalty Point Maru evaluation logs.
* Add Royalty Point Maru example outputs.
* Add GPT interface guidelines for Q-Point Protocol.
* Add dispute resolution workflow.
* Add privacy-preserving contribution tracking notes.
* Add cryptographic content hash verification notes.
* Add zero-knowledge contribution verification notes.
* Add Zenodo DOI after candidate tag stabilization.

---

## Versioning Notes

During the Working Draft phase, versions may use candidate labels such as:

```text
v0.2.0-candidate
```

A candidate version indicates that the structure is usable for review and validation, but may still change before being tagged as a stable release.

---

## Non-Monetary Notice

Q-Point is a non-monetary value trace protocol.

Q-Point records do not represent:

* currency
* securities
* ownership
* debt
* legal claims
* automatic royalty rights
* guaranteed future income

Q-Point records may be used as reference data for future review, attribution, gratitude, licensing, or allocation systems.

The AI Credit to Royalty OS bridge also remains non-executing and non-monetary at the protocol layer.

The value circulation diagram is conceptual and non-executing.

Royalty Point Maru is a GPT interface for non-monetary Q-Point evaluation, not a payment system.

These documents define architecture, evaluation behavior, and reference logic only, not automatic payment.



