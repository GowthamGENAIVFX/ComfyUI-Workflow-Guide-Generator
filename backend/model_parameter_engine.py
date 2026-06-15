class ModelParameterEngine:

    def extract(
        self,
        workflow
    ):

        parameters = {

            "sampler":
                "Not Detected",

            "scheduler":
                "Not Detected",

            "steps":
                "Not Detected",

            "cfg":
                "Not Detected",

            "seed":
                "Random",

            "denoise":
                "Not Detected",

            "resolution":
                "Not Detected",

            "flux_guidance":
                None,

            "loras":
                [],

            "controlnets":
                []
        }

        nodes = workflow.get(
            "nodes",
            []
        )

        for node in nodes:

            node_type = str(
                node.get(
                    "type",
                    ""
                )
            )

            widgets = node.get(
                "widgets_values",
                []
            )

            lower_type = (
                node_type.lower()
            )

            #
            # KSAMPLER
            #

            if (
                node_type ==
                "KSampler"
            ):

                try:

                    parameters[
                        "seed"
                    ] = str(
                        widgets[0]
                    )

                    parameters[
                        "steps"
                    ] = str(
                        widgets[2]
                    )

                    parameters[
                        "cfg"
                    ] = str(
                        widgets[3]
                    )

                    parameters[
                        "sampler"
                    ] = str(
                        widgets[4]
                    )

                    parameters[
                        "scheduler"
                    ] = str(
                        widgets[5]
                    )

                    parameters[
                        "denoise"
                    ] = str(
                        widgets[6]
                    )

                except Exception:

                    pass

            #
            # KSAMPLER ADVANCED
            #

            elif (
                node_type ==
                "KSamplerAdvanced"
            ):

                try:

                    parameters[
                        "steps"
                    ] = str(
                        widgets[4]
                    )

                    parameters[
                        "cfg"
                    ] = str(
                        widgets[6]
                    )

                except Exception:

                    pass

            #
            # FLUX GUIDANCE
            #

            elif (
                node_type ==
                "FluxGuidance"
            ):

                try:

                    parameters[
                        "flux_guidance"
                    ] = str(
                        widgets[0]
                    )

                except Exception:

                    pass

            #
            # FLUX RESOLUTION
            #

            elif (
                node_type ==
                "EmptyFlux2LatentImage"
            ):

                try:

                    width = str(
                        widgets[0]
                    )

                    height = str(
                        widgets[1]
                    )

                    parameters[
                        "resolution"
                    ] = (
                        f"{width}x{height}"
                    )

                except Exception:

                    pass

            #
            # SDXL RESOLUTION
            #

            elif (
                node_type ==
                "EmptyLatentImage"
            ):

                try:

                    width = str(
                        widgets[0]
                    )

                    height = str(
                        widgets[1]
                    )

                    parameters[
                        "resolution"
                    ] = (
                        f"{width}x{height}"
                    )

                except Exception:

                    pass

            #
            # LORA
            #

            elif (
                "lora"
                in lower_type
            ):

                self.extract_lora(
                    widgets,
                    parameters
                )

            #
            # CONTROLNET
            #

            elif (
                "controlnet"
                in lower_type
            ):

                self.extract_controlnet(
                    widgets,
                    parameters
                )

        return parameters

    def extract_lora(
        self,
        widgets,
        parameters
    ):

        try:

            if (
                not isinstance(
                    widgets,
                    list
                )
            ):

                return

            if len(widgets) < 2:

                return

            model_name = str(
                widgets[0]
            )

            strength = str(
                widgets[1]
            )

            parameters[
                "loras"
            ].append({

                "name":
                    model_name,

                "strength":
                    strength
            })

        except Exception:

            pass

    def extract_controlnet(
        self,
        widgets,
        parameters
    ):

        try:

            if (
                not isinstance(
                    widgets,
                    list
                )
            ):

                return

            if len(widgets) < 1:

                return

            model_name = str(
                widgets[0]
            )

            strength = None

            if (
                len(widgets) > 1
            ):

                strength = str(
                    widgets[1]
                )

            parameters[
                "controlnets"
            ].append({

                "name":
                    model_name,

                "strength":
                    strength
            })

        except Exception:

            pass