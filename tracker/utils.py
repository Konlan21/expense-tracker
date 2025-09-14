# tracker/utils.py
from drf_spectacular.utils import extend_schema_view

def apply_schemas(schema_dict):
    """
    Dynamically apply a dictionary of action schemas to a viewset.
    Usage: @apply_schemas(docs.income_schemas)
    """
    return extend_schema_view(**schema_dict)
