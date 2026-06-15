class WorkflowGuideNode:

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
    "WorkflowGuideNode": WorkflowGuideNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowGuideNode": "Workflow Guide Generator"
}