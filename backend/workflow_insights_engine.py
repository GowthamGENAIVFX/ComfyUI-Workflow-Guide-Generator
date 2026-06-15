class WorkflowInsightsEngine:

    def generate(
        self,
        workflow
    ):

        nodes = workflow.get(
            "nodes",
            []
        )

        result = {

            "sampler":
                "Not Detected",

            "scheduler":
                "Not Detected",

            "steps":
                "Not Detected",

            "cfg":
                "Not Detected",

            "resolution":
                "Not Detected",

            "output":
                "Generated Output",

            "performance_tips":
                []
        }

        node_types = []

        for node in nodes:

            node_type = str(
                node.get(
                    "type",
                    ""
                )
            )

            node_types.append(
                node_type.lower()
            )

            widgets = node.get(
                "widgets_values",
                []
            )

            #
            # KSAMPLER
            #

            if (
                "ksampler"
                in node_type.lower()
            ):

                try:

                    for value in widgets:

                        #
                        # Steps
                        #

                        if (
                            isinstance(
                                value,
                                int
                            )
                            and
                            result["steps"]
                            ==
                            "Not Detected"
                        ):

                            result[
                                "steps"
                            ] = value

                        #
                        # CFG
                        #

                        if (
                            isinstance(
                                value,
                                float
                            )
                            and
                            result["cfg"]
                            ==
                            "Not Detected"
                        ):

                            result[
                                "cfg"
                            ] = value

                        #
                        # Sampler
                        #

                        if (
                            isinstance(
                                value,
                                str
                            )
                        ):

                            lower = (
                                value.lower()
                            )

                            sampler_keywords = [

                                "euler",
                                "heun",
                                "ddim",
                                "dpm",
                                "uni_pc",
                                "deis"
                            ]

                            for keyword in sampler_keywords:

                                if (
                                    keyword
                                    in lower
                                ):

                                    result[
                                        "sampler"
                                    ] = value

                        #
                        # Scheduler
                        #

                        if (
                            isinstance(
                                value,
                                str
                            )
                        ):

                            lower = (
                                value.lower()
                            )

                            scheduler_keywords = [

                                "normal",
                                "karras",
                                "sgm_uniform",
                                "simple",
                                "beta"
                            ]

                            for keyword in scheduler_keywords:

                                if (
                                    keyword
                                    in lower
                                ):

                                    result[
                                        "scheduler"
                                    ] = value

                except Exception:

                    pass

            #
            # LATENT SIZE
            #

            if (
                "emptylatentimage"
                in node_type.lower()

                or

                "emptyflux"
                in node_type.lower()
            ):

                try:

                    width = None
                    height = None

                    for value in widgets:

                        if (
                            isinstance(
                                value,
                                int
                            )
                        ):

                            if width is None:

                                width = value

                            elif height is None:

                                height = value

                    if (
                        width
                        and
                        height
                    ):

                        result[
                            "resolution"
                        ] = (
                            f"{width}x{height}"
                        )

                except Exception:

                    pass

            #
            # OUTPUT
            #

            if (
                "saveexrframes"
                in node_type.lower()
            ):

                result[
                    "output"
                ] = (
                    "EXR Sequence"
                )

            elif (
                "saveimage"
                in node_type.lower()
            ):

                result[
                    "output"
                ] = (
                    "PNG Image"
                )

            elif (
                "save"
                in node_type.lower()
            ):

                result[
                    "output"
                ] = (
                    "Saved Output"
                )

        #
        # WORKFLOW DETECTION
        #

        node_text = " ".join(
            node_types
        )

        #
        # VIDEO → EXR
        #

        if (

            "vhs_loadvideo"
            in node_text

            and

            "saveexrframes"
            in node_text
        ):

            result[
                "performance_tips"
            ] = [

                "Test with 50 frames before full export",

                "Store EXRs on SSD storage",

                "Verify frame numbering before rendering",

                "Disable overwrite if preserving previous renders",

                "Use EXR only when HDR data is required"
            ]

            return result

        #
        # VIDEO
        #

        if (
            "video"
            in node_text
        ):

            result[
                "performance_tips"
            ] = [

                "Process short clips before full sequences",

                "Reduce resolution during testing",

                "Export previews before final renders",

                "Use SSD storage for frame caching"
            ]

            return result

        #
        # UPSCALE
        #

        if (

            "upscale"
            in node_text

            or

            "esrgan"
            in node_text
        ):

            result[
                "performance_tips"
            ] = [

                "Preview using a single image first",

                "Avoid unnecessary upscale passes",

                "Use moderate upscale factors for faster processing",

                "Batch process only after validation"
            ]

            return result

        #
        # INPAINT
        #

        if (

            "mask"
            in node_text

            or

            "inpaint"
            in node_text
        ):

            result[
                "performance_tips"
            ] = [

                "Mask only the required areas",

                "Use lower denoise values to preserve details",

                "Generate previews before final renders",

                "Keep backup versions of source images"
            ]

            return result

        #
        # CONTROLNET
        #

        if (
            "controlnet"
            in node_text
        ):

            result[
                "performance_tips"
            ] = [

                "Use clean reference images",

                "Avoid excessive ControlNet strength",

                "Preview composition before long renders",

                "Combine with LoRAs carefully"
            ]

            return result

        #
        # FLUX / IMAGE GENERATION
        #

        if (

            "unetloader"
            in node_text

            or

            "flux"
            in node_text

            or

            "ksampler"
            in node_text
        ):

            result[
                "performance_tips"
            ] = [

                "Increase steps for higher quality output",

                "Reduce resolution for faster previews",

                "Generate preview renders before final rendering",

                "Use lower CFG values for more natural results",

                "Save successful settings as presets"
            ]

            return result

        #
        # FALLBACK
        #

        result[
            "performance_tips"
        ] = [

            "Test with small inputs first",

            "Validate output before large runs",

            "Save working workflow versions",

            "Document successful settings"
        ]

        return result