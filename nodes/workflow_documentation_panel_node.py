class WorkflowDocumentationPanelNode:

    CATEGORY = "Workflow Documentation"

    FUNCTION = "execute"

    OUTPUT_NODE = True

    RETURN_TYPES = ()

    @classmethod
    def INPUT_TYPES(cls):

        return {
            "required": {}
        }

    def execute(self):

        return ()


NODE_CLASS_MAPPINGS = {
    "WorkflowDocumentationPanelNode":
        WorkflowDocumentationPanelNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowDocumentationPanelNode":
        "Workflow Documentation Panel"
}