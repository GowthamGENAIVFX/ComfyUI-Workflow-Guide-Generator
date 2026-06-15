class NodePurposeEngine:

    def __init__(self):

        self.node_database = {

            #
            # MODEL LOADERS
            #

            "UNETLoader": {
                "title":
                    "Main AI Model",
                "purpose":
                    "Loads the primary image generation model."
            },

            "CheckpointLoaderSimple": {
                "title":
                    "AI Checkpoint",
                "purpose":
                    "Loads a Stable Diffusion checkpoint model."
            },

            "CheckpointLoader": {
                "title":
                    "AI Checkpoint",
                "purpose":
                    "Loads a Stable Diffusion checkpoint model."
            },

            "CLIPLoader": {
                "title":
                    "Text Encoder",
                "purpose":
                    "Converts prompts into AI-understandable instructions."
            },

            "DualCLIPLoader": {
                "title":
                    "Dual Text Encoder",
                "purpose":
                    "Loads multiple text encoders for advanced models."
            },

            "TripleCLIPLoader": {
                "title":
                    "Triple Text Encoder",
                "purpose":
                    "Loads three text encoders used by some Flux workflows."
            },

            "VAELoader": {
                "title":
                    "Image Decoder",
                "purpose":
                    "Converts latent data into visible images."
            },

            #
            # PROMPTS
            #

            "CLIPTextEncode": {
                "title":
                    "Prompt Encoder",
                "purpose":
                    "Encodes prompt text for image generation."
            },

            "ConditioningZeroOut": {
                "title":
                    "Conditioning Cleanup",
                "purpose":
                    "Removes conditioning information before reuse."
            },

            "ReferenceLatent": {
                "title":
                    "Reference Guidance",
                "purpose":
                    "Transfers information from a reference latent."
            },

            #
            # IMAGE GENERATION
            #

            "KSampler": {
                "title":
                    "Image Generator",
                "purpose":
                    "Creates images through diffusion sampling."
            },

            "KSamplerAdvanced": {
                "title":
                    "Advanced Generator",
                "purpose":
                    "Provides advanced image generation controls."
            },

            "SamplerCustomAdvanced": {
                "title":
                    "Custom Sampler",
                "purpose":
                    "Performs image generation using custom settings."
            },

            #
            # LATENTS
            #

            "EmptyLatentImage": {
                "title":
                    "Latent Canvas",
                "purpose":
                    "Creates an empty latent image for generation."
            },

            "EmptyFlux2LatentImage": {
                "title":
                    "Flux Latent Canvas",
                "purpose":
                    "Creates a Flux latent image at the desired resolution."
            },

            "VAEEncode": {
                "title":
                    "Image Encoder",
                "purpose":
                    "Converts images into latent space."
            },

            "VAEDecode": {
                "title":
                    "Image Builder",
                "purpose":
                    "Converts generated latents into visible images."
            },

            #
            # IMAGE INPUT
            #

            "LoadImage": {
                "title":
                    "Image Input",
                "purpose":
                    "Loads an image into the workflow."
            },

            "AILab_LoadImage": {
                "title":
                    "Image Input",
                "purpose":
                    "Loads an image for processing."
            },

            "GetImageSize": {
                "title":
                    "Resolution Reader",
                "purpose":
                    "Reads image dimensions."
            },

            #
            # VIDEO
            #

            "VHS_LoadVideo": {
                "title":
                    "Video Input",
                "purpose":
                    "Loads a video and extracts frames."
            },

            "LoadVideo": {
                "title":
                    "Video Input",
                "purpose":
                    "Loads a video file."
            },

            #
            # CONTROLNET
            #

            "ControlNetLoader": {
                "title":
                    "ControlNet Model",
                "purpose":
                    "Loads ControlNet guidance models."
            },

            "ApplyControlNet": {
                "title":
                    "ControlNet Guidance",
                "purpose":
                    "Applies reference guidance during generation."
            },

            #
            # LORA
            #

            "LoraLoader": {
                "title":
                    "LoRA Loader",
                "purpose":
                    "Adds style or subject-specific knowledge."
            },

            #
            # UPSCALE
            #

            "UpscaleModelLoader": {
                "title":
                    "Upscale Model",
                "purpose":
                    "Loads an image upscaling model."
            },

            "ImageUpscaleWithModel": {
                "title":
                    "Image Upscaler",
                "purpose":
                    "Increases image resolution and detail."
            },

            #
            # MASKING
            #

            "RMBG": {
                "title":
                    "Background Removal",
                "purpose":
                    "Separates foreground subjects from background."
            },

            "ImageCompositeMasked": {
                "title":
                    "Image Compositor",
                "purpose":
                    "Combines images using masks."
            },

            "InpaintModelConditioning": {
                "title":
                    "Inpainting Setup",
                "purpose":
                    "Prepares masked regions for editing."
            },

            #
            # OUTPUT
            #

            "SaveImage": {
                "title":
                    "Image Export",
                "purpose":
                    "Saves generated images to disk."
            },

            "SaveEXRFrames": {
                "title":
                    "EXR Export",
                "purpose":
                    "Exports frames as professional EXR sequences."
            },

            #
            # UTILITIES
            #

            "Image Comparer (rgthree)": {
                "title":
                    "Image Comparison",
                "purpose":
                    "Compares generated images side by side."
            }
        }

    def explain(
        self,
        node_type
    ):

        if (
            node_type
            in
            self.node_database
        ):

            return self.node_database[
                node_type
            ]

        return {

            "title":
                node_type,

            "purpose":
                "Processes workflow data."
        }

    def build(
        self,
        workflow
    ):

        nodes = workflow.get(
            "nodes",
            []
        )

        results = []

        seen = set()

        for node in nodes:

            node_type = node.get(
                "type",
                ""
            )

            if (
                not node_type
                or
                node_type in seen
            ):
                continue

            seen.add(
                node_type
            )

            info = self.explain(
                node_type
            )

            results.append({

                "node":
                    node_type,

                "title":
                    info["title"],

                "purpose":
                    info["purpose"]
            })

        return results