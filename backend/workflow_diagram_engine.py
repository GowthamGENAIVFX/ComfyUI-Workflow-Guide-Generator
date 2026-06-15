class WorkflowDiagramEngine:

    def generate(
        self,
        workflow,
        workflow_stages=None
    ):

        nodes = workflow.get(
            "nodes",
            []
        )

        node_types = [

            str(
                node.get(
                    "type",
                    ""
                )
            ).lower()

            for node in nodes
        ]

        #
        # VIDEO -> EXR
        #

        if (

            self.has(
                node_types,
                "vhs_loadvideo"
            )

            and

            self.has(
                node_types,
                "saveexrframes"
            )
        ):

            return [

                "🎬 Load Video",

                "↓",

                "🖼️ Extract Frames",

                "↓",

                "🎞️ Convert To EXR",

                "↓",

                "📦 Export EXR Sequence"
            ]

        #
        # VIDEO
        #

        if (
            self.contains(
                node_types,
                [
                    "video",
                    "vhs_"
                ]
            )
        ):

            return [

                "🎬 Load Video",

                "↓",

                "🖼️ Extract Frames",

                "↓",

                "🎨 Process Frames",

                "↓",

                "📦 Export Sequence"
            ]

        #
        # UPSCALE
        #

        if (
            self.contains(
                node_types,
                [
                    "upscale",
                    "esrgan"
                ]
            )
        ):

            return [

                "🖼️ Load Image",

                "↓",

                "🚀 Upscale Image",

                "↓",

                "✨ Enhance Details",

                "↓",

                "💾 Save Result"
            ]

        #
        # INPAINT
        #

        if (
            self.contains(
                node_types,
                [
                    "mask",
                    "inpaint"
                ]
            )
        ):

            return [

                "🖼️ Load Source Image",

                "↓",

                "🎭 Apply Mask",

                "↓",

                "✏️ Process Prompt",

                "↓",

                "🎨 Generate Edited Image",

                "↓",

                "💾 Save Result"
            ]

        #
        # CONTROLNET
        #

        if (
            self.contains(
                node_types,
                [
                    "controlnet"
                ]
            )
        ):

            return [

                "📥 Load AI Models",

                "↓",

                "🖼️ Load Reference",

                "↓",

                "🎯 Apply Guidance",

                "↓",

                "✏️ Process Prompt",

                "↓",

                "🎨 Generate Image",

                "↓",

                "💾 Save Result"
            ]

        #
        # FLUX
        #

        if (

            self.has(
                node_types,
                "unetloader"
            )

            or

            self.contains(
                node_types,
                [
                    "flux"
                ]
            )
        ):

            return [

                "📥 Load AI Models",

                "↓",

                "✏️ Process Prompt",

                "↓",

                "🎨 Generate Image",

                "↓",

                "🖼️ Build Final Image",

                "↓",

                "💾 Save Result"
            ]

        #
        # SDXL / CHECKPOINT
        #

        if (
            self.contains(
                node_types,
                [
                    "checkpointloader"
                ]
            )
        ):

            return [

                "📥 Load Checkpoint",

                "↓",

                "✏️ Process Prompt",

                "↓",

                "🎨 Generate Image",

                "↓",

                "🖼️ Decode Image",

                "↓",

                "💾 Save Result"
            ]

        #
        # IMAGE PROCESSING
        #

        if (
            self.contains(
                node_types,
                [
                    "loadimage"
                ]
            )
        ):

            return [

                "🖼️ Load Image",

                "↓",

                "⚙️ Process Image",

                "↓",

                "💾 Save Result"
            ]

        #
        # GENERIC FALLBACK
        #

        return [

            "📥 Load Inputs",

            "↓",

            "⚙️ Process Data",

            "↓",

            "💾 Save Result"
        ]

    def has(
        self,
        node_types,
        value
    ):

        return value.lower() in node_types

    def contains(
        self,
        node_types,
        keywords
    ):

        for node in node_types:

            for keyword in keywords:

                if keyword in node:

                    return True

        return False