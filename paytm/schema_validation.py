from jsonschema import Draft7Validator, FormatChecker

schema = {
    "type": "object",
    "properties": {
        "name":     {"type": "string"},
        "age":      {"type": "integer", "minimum": 0},
        "email":    {"type": "string", "format": "email"},
        "is_active": {"type": "boolean"}
    },
    "required": ["name", "email"]
}

data = {
    "name": "Mayank",
    "age": "45",
    "email": "mayank@example.com",
    "is_active": "True"
}

validator = Draft7Validator(schema, format_checker=FormatChecker())
errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
for error in errors:
    print("Error:", error.message)
