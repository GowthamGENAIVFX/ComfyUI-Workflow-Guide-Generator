class ModelExplanationEngine:

    def explain(
        self,
        model_name
    ):

        if not model_name:

            return (
                "Model detected."
            )

        name = (
            str(model_name)
            .lower()
        )

        #
        # FLUX
        #

        if (
            "flux"
            in name
        ):

            return (
                "Creates the final image from your prompt."
            )

        #
        # QWEN
        #

        if (
            "qwen"
            in name
        ):

            return (
                "Understands prompts and converts them into AI instructions."
            )

        #
        # CLIP
        #

        if (
            "clip"
            in name
        ):

            return (
                "Processes prompt text for image generation."
            )

        #
        # VAE
        #

        if (
            "vae"
            in name
        ):

            return (
                "Converts generated latent data into a visible image."
            )

        #
        # CONTROLNET
        #

        if (
            "controlnet"
            in name
        ):

            return (
                "Provides reference guidance during generation."
            )

        #
        # LORA
        #

        if (
            "lora"
            in name
        ):

            return (
                "Adds style or subject-specific knowledge."
            )

        return (
            "AI model used by this workflow."
        )

    def build(
        self,
        discovered_models
    ):

        results = []

        for model in discovered_models.get(
            "main_models",
            []
        ):

            results.append({

                "type":
                    "Main AI Model",

                "name":
                    model,

                "purpose":
                    self.explain(
                        model
                    )
            })

        for model in discovered_models.get(
            "text_encoders",
            []
        ):

            results.append({

                "type":
                    "Text Understanding Model",

                "name":
                    model,

                "purpose":
                    self.explain(
                        model
                    )
            })

        for model in discovered_models.get(
            "vaes",
            []
        ):

            results.append({

                "type":
                    "Image Decoder",

                "name":
                    model,

                "purpose":
                    self.explain(
                        model
                    )
            })

        return results
