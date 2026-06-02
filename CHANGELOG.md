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
* Added README documentation for:

  * Q-Point overview
  * Catalyst C-vector
  * Internal and Proxy Signal Modes
  * Validation workflow
  * Relationship to Trace Protocol, Gratitude OS, Royalty OS, and licensing standards
* Added GitHub Actions validation workflow for Q-Point examples.
* Added local validation script:

  * `scripts/validate_examples.py`

### Updated

* Updated `examples/q-point-record.example.yaml` with C-vector fields.
* Updated `schemas/q-point-record.schema.json` to validate:

  * `q_point_components`
  * `catalyst_vector`
  * `scoring_signal_mode`
* Updated README repository structure to reflect the current files.
* Updated validation instructions for local and GitHub Actions usage.
* Updated the Q-Point model from a simple value trace record toward a C-vector compatible scoring structure.

### Validation

* GitHub Actions validation is passing for:

  * `examples/q-point-record.example.yaml`
  * `schemas/q-point-record.schema.json`
  * `scripts/validate_examples.py`

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

* Add `docs/q-point-scoring-model.md`.
* Add pass / fail validation examples.
* Add Epicenter ID specification.
* Add Cross-AI Aggregation schema.
* Add Gratitude OS bridge document.
* Add Royalty OS bridge document.
* Add licensing metadata bridge document.
* Add dashboard metadata schema.
* Add dispute resolution workflow.
* Add privacy-preserving contribution tracking notes.
* Add cryptographic content hash verification notes.
* Add `LICENSE`.
* Add `CITATION.cff`.

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
