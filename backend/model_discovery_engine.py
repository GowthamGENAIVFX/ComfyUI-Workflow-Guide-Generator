class ModelDiscoveryEngine:

    def discover(
        self,
        workflow
    ):

        results = {

            "main_models": [],
            "text_encoders": [],
            "vaes": [],
            "loras": [],
            "controlnets": [],
            "upscalers": []
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

            try:

                self.process_node(
                    node_type,
                    widgets,
                    results
                )

            except Exception:

                pass

        #
        # REMOVE DUPLICATES
        #

        for key in results:

            cleaned = []

            for item in results[key]:

                if (
                    item
                    and
                    item not in cleaned
                ):

                    cleaned.append(
                        item
                    )

            results[key] = cleaned

        return results

    def process_node(
        self,
        node_type,
        widgets,
        results
    ):

        node_type_lower = (
            node_type.lower()
        )

        #
        # =====================================
        # FLUX / UNET LOADERS
        # =====================================
        #

        if node_type in [

            "UNETLoader",
            "UNETLoaderGGUF",
            "LoadDiffusionModel",
            "DiffusionModelLoader"
        ]:

            if widgets:

                results[
                    "main_models"
                ].append(
                    str(
                        widgets[0]
                    )
                )

            return

        #
        # =====================================
        # CHECKPOINT LOADERS
        # =====================================
        #

        if node_type in [

            "CheckpointLoader",
            "CheckpointLoaderSimple",
            "CheckpointLoaderNF4",
            "CheckpointLoaderGGUF"
        ]:

            if widgets:

                results[
                    "main_models"
                ].append(
                    str(
                        widgets[0]
                    )
                )

            return

        #
        # =====================================
        # CLIP LOADERS
        # =====================================
        #

        if node_type in [

            "CLIPLoader",
            "DualCLIPLoader",
            "TripleCLIPLoader"
        ]:

            if widgets:

                results[
                    "text_encoders"
                ].append(
                    str(
                        widgets[0]
                    )
                )

            return

        #
        # =====================================
        # T5 / QWEN
        # =====================================
        #

        if (

            "clip"
            in node_type_lower

            or

            "textencoder"
            in node_type_lower

            or

            "encoder"
            in node_type_lower
        ):

            if widgets:

                first = str(
                    widgets[0]
                )

                if (
                    ".safetensors"
                    in first.lower()
                ):

                    results[
                        "text_encoders"
                    ].append(
                        first
                    )

            return

        #
        # =====================================
        # VAE
        # =====================================
        #

        if node_type in [

            "VAELoader",
            "LoadVAE"
        ]:

            if widgets:

                results[
                    "vaes"
                ].append(
                    str(
                        widgets[0]
                    )
                )

            return

        #
        # =====================================
        # LORA
        # =====================================
        #

        if (
            "lora"
            in node_type_lower
        ):

            if widgets:

                results[
                    "loras"
                ].append(
                    str(
                        widgets[0]
                    )
                )

            return

        #
        # =====================================
        # CONTROLNET
        # =====================================
        #

        if (
            "controlnet"
            in node_type_lower
        ):

            if widgets:

                results[
                    "controlnets"
                ].append(
                    str(
                        widgets[0]
                    )
                )

            return

        #
        # =====================================
        # UPSCALERS
        # =====================================
        #

        if (

            "upscale"
            in node_type_lower

            or

            "esrgan"
            in node_type_lower

            or

            "realesrgan"
            in node_type_lower
        ):

            if widgets:

                results[
                    "upscalers"
                ].append(
                    str(
                        widgets[0]
                    )
                )

            return

        #
        # =====================================
        # GENERIC MODEL DETECTION
        # =====================================
        #

        if not widgets:

            return

        for value in widgets:

            if not isinstance(
                value,
                str
            ):

                continue

            lower = value.lower()

            if (
                ".safetensors"
                not in lower
            ):

                continue

            #
            # VAE
            #

            if (
                "vae"
                in lower
            ):

                results[
                    "vaes"
                ].append(
                    value
                )

                continue

            #
            # QWEN / T5 / CLIP
            #

            if (

                "qwen"
                in lower

                or

                "t5"
                in lower

                or

                "clip"
                in lower
            ):

                results[
                    "text_encoders"
                ].append(
                    value
                )

                continue

            #
            # CONTROLNET
            #

            if (
                "controlnet"
                in lower
            ):

                results[
                    "controlnets"
                ].append(
                    value
                )

                continue

            #
            # LORA
            #

            if (
                "lora"
                in lower
            ):

                results[
                    "loras"
                ].append(
                    value
                )

                continue

            #
            # DEFAULT
            #

            results[
                "main_models"
            ].append(
                value
            )