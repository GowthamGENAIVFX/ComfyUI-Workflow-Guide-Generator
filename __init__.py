WEB_DIRECTORY = "./web"

print(
    "[Workflow Guide Generator] Loading..."
)

try:

    from . import api_server

    from .nodes import (
        NODE_CLASS_MAPPINGS,
        NODE_DISPLAY_NAME_MAPPINGS
    )

    print(
        "[Workflow Guide Generator] Loaded Successfully"
    )

except Exception as e:

    import traceback

    print(
        "\n\n========== WORKFLOW GUIDE ERROR =========="
    )

    traceback.print_exc()

    print(
        "==========================================\n\n"
    )

    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY"
]