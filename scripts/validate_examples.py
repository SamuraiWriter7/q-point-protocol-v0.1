#!/usr/bin/env python3
"""
Validate Q-Point Protocol example YAML files against JSON Schema files.

Required packages:

* PyYAML
* jsonschema

Usage:
python scripts/validate_examples.py
"""

import json
import sys
from pathlib import Path
from typing import Any, Iterable

try:
import yaml
except ImportError as exc:
print("Missing dependency: PyYAML")
print("Install with: pip install PyYAML")
raise SystemExit(1) from exc

try:
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError
except ImportError as exc:
print("Missing dependency: jsonschema")
print("Install with: pip install jsonschema")
raise SystemExit(1) from exc

REPO_ROOT = Path(**file**).resolve().parents[1]

VALIDATION_TARGETS = [
{
"name": "Q-Point Record",
"schema": "schemas/q-point-record.schema.json",
"example": "examples/q-point-record.example.yaml",
},
{
"name": "Signed Q-Point Record",
"schema": "schemas/signed-q-point-record.schema.json",
"example": "examples/signed-q-point-record.example.yaml",
},
]

def load_json(path: Path) -> Any:
try:
with path.open("r", encoding="utf-8") as file:
return json.load(file)
except FileNotFoundError:
raise FileNotFoundError(f"JSON schema file not found: {path}") from None
except json.JSONDecodeError as exc:
raise ValueError(f"Invalid JSON in {path}: {exc}") from exc

def load_yaml(path: Path) -> Any:
try:
with path.open("r", encoding="utf-8") as file:
data = yaml.safe_load(file)
except FileNotFoundError:
raise FileNotFoundError(f"YAML example file not found: {path}") from None
except yaml.YAMLError as exc:
raise ValueError(f"Invalid YAML in {path}: {exc}") from exc

```
if data is None:
    raise ValueError(f"YAML example file is empty: {path}")

return data
```

def format_error_path(error_path: Iterable[Any]) -> str:
parts = [str(part) for part in error_path]

```
if not parts:
    return "$"

return "$." + ".".join(parts)
```

def validate_pair(name: str, schema_relative_path: str, example_relative_path: str) -> bool:
schema_path = REPO_ROOT / schema_relative_path
example_path = REPO_ROOT / example_relative_path

```
print(f"Validating target: {name}")
print(f"Validating example: {example_relative_path}")
print(f"Using schema: {schema_relative_path}")

schema = load_json(schema_path)
example = load_yaml(example_path)

try:
    Draft202012Validator.check_schema(schema)
except SchemaError as exc:
    print("")
    print("Schema validation failed.")
    print(f"Target: {name}")
    print(f"Schema: {schema_relative_path}")
    print(f"Error: {exc.message}")
    return False

validator = Draft202012Validator(schema, format_checker=FormatChecker())
errors = sorted(validator.iter_errors(example), key=lambda err: list(err.path))

if errors:
    print("")
    print("Example validation failed.")
    print(f"Target: {name}")

    for error in errors:
        print(f"- Path: {format_error_path(error.path)}")
        print(f"  Error: {error.message}")

    return False

print("Validation passed.")
print("")
return True
```

def main() -> int:
all_passed = True

```
for target in VALIDATION_TARGETS:
    try:
        passed = validate_pair(
            name=target["name"],
            schema_relative_path=target["schema"],
            example_relative_path=target["example"],
        )
    except Exception as exc:
        print("")
        print("Validation failed.")
        print(f"Target: {target.get('name', 'unknown')}")
        print(f"Error: {exc}")
        passed = False

    if not passed:
        all_passed = False

if all_passed:
    print("All examples passed validation.")
    return 0

print("One or more examples failed validation.")
return 1
```

if **name** == "**main**":
sys.exit(main())
