class WorkflowFlowEngine:

    def generate(
        self,
        workflow
    ):

        nodes = workflow.get(
            "nodes",
            []
        )

        detected = {

            "video": False,
            "image": False,
            "mask": False,
            "upscale": False,
            "controlnet": False,
            "flux": False,
            "sampler": False,
            "decode": False,
            "save": False,
            "exr": False
        }

        for node in nodes:

            node_type = str(
                node.get(
                    "type",
                    ""
                )
            )

            lower = (
                node_type.lower()
            )

            #
            # VIDEO
            #

            if (

                "video"
                in lower

                or

                "vhs_"
                in lower
            ):

                detected[
                    "video"
                ] = True

            #
            # IMAGE INPUT
            #

            if (

                lower.startswith(
                    "loadimage"
                )

                or

                "image"
                in lower
            ):

                detected[
                    "image"
                ] = True

            #
            # MASK
            #

            if (
                "mask"
                in lower
            ):

                detected[
                    "mask"
                ] = True

            #
            # UPSCALE
            #

            if (

                "upscale"
                in lower

                or

                "esrgan"
                in lower
            ):

                detected[
                    "upscale"
                ] = True

            #
            # CONTROLNET
            #

            if (
                "controlnet"
                in lower
            ):

                detected[
                    "controlnet"
                ] = True

            #
            # FLUX
            #

            if (

                "unetloader"
                in lower

                or

                "flux"
                in lower
            ):

                detected[
                    "flux"
                ] = True

            #
            # SAMPLER
            #

            if (
                "ksampler"
                in lower
            ):

                detected[
                    "sampler"
                ] = True

            #
            # DECODE
            #

            if (

                "decode"
                in lower

                or

                "vae"
                in lower
            ):

                detected[
                    "decode"
                ] = True

            #
            # SAVE
            #

            if (
                "save"
                in lower
            ):

                detected[
                    "save"
                ] = True

            #
            # EXR
            #

            if (
                "exr"
                in lower
            ):

                detected[
                    "exr"
                ] = True

        #
        # EXR WORKFLOW
        #

        if (
            detected["video"]
            and
            detected["exr"]
        ):

            return [

                "🎬 Load Video",

                "🖼️ Extract Frames",

                "🎞️ Convert To EXR",

                "📦 Export EXR Sequence"
            ]

        #
        # VIDEO WORKFLOW
        #

        if (
            detected["video"]
        ):

            return [

                "🎬 Load Video",

                "🖼️ Extract Frames",

                "🎨 Process Frames",

                "📦 Export Sequence"
            ]

        #
        # UPSCALE WORKFLOW
        #

        if (
            detected["upscale"]
        ):

            return [

                "🖼️ Load Image",

                "🚀 Upscale Image",

                "✨ Enhance Details",

                "💾 Save Result"
            ]

        #
        # CONTROLNET WORKFLOW
        #

        if (
            detected["controlnet"]
        ):

            return [

                "📥 Load AI Models",

                "🖼️ Load Reference",

                "🎯 Apply Guidance",

                "✏️ Process Prompt",

                "🎨 Generate Image",

                "💾 Save Result"
            ]

        #
        # INPAINT WORKFLOW
        #

        if (
            detected["mask"]
        ):

            return [

                "📥 Load AI Models",

                "🖼️ Load Source Image",

                "🎭 Apply Mask",

                "✏️ Process Prompt",

                "🎨 Generate Edited Image",

                "💾 Save Result"
            ]

        #
        # FLUX / IMAGE GENERATION
        #

        if (
            detected["flux"]
            or
            detected["sampler"]
        ):

            return [

                "📥 Load AI Models",

                "✏️ Process Prompt",

                "🎨 Generate Image",

                "🖼️ Build Final Image",

                "💾 Save Result"
            ]

        #
        # IMAGE WORKFLOW
        #

        if (
            detected["image"]
        ):

            return [

                "🖼️ Load Image",

                "⚙️ Process Image",

                "💾 Save Result"
            ]

        #
        # FALLBACK
        #

        return [

            "📥 Load Inputs",

            "⚙️ Process Data",

            "💾 Save Result"
        ]