# tracker/utils.py
def apply_schemas(schema_decorator):
    """
    Apply a schema decorator (created with extend_schema_view)
    to a viewset.
    Usage: @apply_schemas(income_schemas)
    """
    return schema_decorator
