from drf_spectacular.utils import extend_schema, extend_schema_view



def apply_schema(schema, default_tag="user"):
    """Apply schema with a default tag if not specified."""
    kwargs = schema.copy()
    if "tags" not in kwargs:
        kwargs["tags"] = [default_tag]
    return extend_schema(**kwargs)

def apply_schema_view(schemas, default_tag="user"):
    """Apply schema_view with default tags for all operations."""
    new_schemas = {}
    for method, schema in schemas.items():
        kwargs = schema.copy()
        if "tags" not in kwargs:
            kwargs["tags"] = [default_tag]
        new_schemas[method] = extend_schema(**kwargs)
    return extend_schema_view(**new_schemas)
