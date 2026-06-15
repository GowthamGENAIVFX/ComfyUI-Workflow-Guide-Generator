class WorkflowPurposeEngine:

    def generate(
        self,
        workflow_type,
        analysis
    ):

        nodes = analysis.get(
            "all_node_types",
            []
        )

        node_text = " ".join(
            [
                str(n).lower()
                for n in nodes
            ]
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

            return {

                "purpose":

                    "Convert video footage into EXR image sequences.",

                "difficulty":
                    "Beginner",

                "estimated_vram":
                    "Low",

                "recommended_users": [

                    "Compositors",
                    "VFX Artists",
                    "Pipeline TDs"
                ],

                "required_inputs": [

                    "Video File"
                ],

                "produced_outputs": [

                    "EXR Sequence"
                ],

                "use_cases": [

                    "Nuke Compositing",
                    "CG Integration",
                    "HDR Workflows",
                    "VFX Pipelines"
                ]
            }

        #
        # VIDEO PROCESSING
        #

        if (

            "vhs_loadvideo"
            in node_text

            or

            "video"
            in node_text
        ):

            return {

                "purpose":

                    "Process video footage and generate transformed outputs.",

                "difficulty":
                    "Intermediate",

                "estimated_vram":
                    "Medium",

                "recommended_users": [

                    "Video Editors",
                    "Motion Designers",
                    "AI Creators"
                ],

                "required_inputs": [

                    "Video File"
                ],

                "produced_outputs": [

                    "Video Sequence"
                ],

                "use_cases": [

                    "Video Processing",
                    "Frame Extraction",
                    "AI Video Workflows"
                ]
            }

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

            return {

                "purpose":

                    "Increase image resolution while preserving visual quality.",

                "difficulty":
                    "Beginner",

                "estimated_vram":
                    "Medium",

                "recommended_users": [

                    "Artists",
                    "Photographers",
                    "Designers"
                ],

                "required_inputs": [

                    "Image"
                ],

                "produced_outputs": [

                    "Upscaled Image"
                ],

                "use_cases": [

                    "Print",
                    "High Resolution Delivery",
                    "Image Enhancement"
                ]
            }

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

            return {

                "purpose":

                    "Modify selected regions of an image while preserving surrounding details.",

                "difficulty":
                    "Intermediate",

                "estimated_vram":
                    "Medium",

                "recommended_users": [

                    "Concept Artists",
                    "Retouchers",
                    "Designers"
                ],

                "required_inputs": [

                    "Image",
                    "Mask"
                ],

                "produced_outputs": [

                    "Edited Image"
                ],

                "use_cases": [

                    "Object Removal",
                    "Image Editing",
                    "Content Replacement"
                ]
            }

        #
        # CONTROLNET
        #

        if (
            "controlnet"
            in node_text
        ):

            return {

                "purpose":

                    "Generate images using reference guidance such as pose, depth or edge maps.",

                "difficulty":
                    "Intermediate",

                "estimated_vram":
                    "Medium",

                "recommended_users": [

                    "AI Artists",
                    "Character Artists"
                ],

                "required_inputs": [

                    "Reference Image",
                    "Prompt"
                ],

                "produced_outputs": [

                    "Guided Image"
                ],

                "use_cases": [

                    "Pose Transfer",
                    "Composition Control",
                    "Character Consistency"
                ]
            }

        #
        # FLUX
        #

        if (

            "unetloader"
            in node_text

            or

            "flux"
            in node_text
        ):

            return {

                "purpose":

                    "Generate high quality Flux images from text prompts.",

                "difficulty":
                    "Beginner",

                "estimated_vram":
                    "High",

                "recommended_users": [

                    "AI Artists",
                    "Concept Artists",
                    "Designers"
                ],

                "required_inputs": [

                    "Text Prompt"
                ],

                "produced_outputs": [

                    "Generated Image"
                ],

                "use_cases": [

                    "Concept Art",
                    "Illustration",
                    "Marketing Images",
                    "Creative Design"
                ]
            }

        #
        # SDXL
        #

        if (
            "checkpointloader"
            in node_text
        ):

            return {

                "purpose":

                    "Generate high quality images from text prompts.",

                "difficulty":
                    "Beginner",

                "estimated_vram":
                    "Medium",

                "recommended_users": [

                    "Artists",
                    "Designers"
                ],

                "required_inputs": [

                    "Text Prompt"
                ],

                "produced_outputs": [

                    "Generated Image"
                ],

                "use_cases": [

                    "Illustration",
                    "Concept Art",
                    "Advertising"
                ]
            }

        #
        # IMAGE PROCESSING
        #

        if (
            "loadimage"
            in node_text
        ):

            return {

                "purpose":

                    "Process images and generate enhanced outputs.",

                "difficulty":
                    "Beginner",

                "estimated_vram":
                    "Low",

                "recommended_users": [

                    "Artists",
                    "Editors"
                ],

                "required_inputs": [

                    "Image"
                ],

                "produced_outputs": [

                    "Processed Image"
                ],

                "use_cases": [

                    "Image Editing",
                    "Image Enhancement"
                ]
            }

        #
        # FALLBACK
        #

        return {

            "purpose":

                "Process input data and generate output results.",

            "difficulty":
                "Beginner",

            "estimated_vram":
                "Unknown",

            "recommended_users": [

                "ComfyUI Users"
            ],

            "required_inputs": [

                "Workflow Inputs"
            ],

            "produced_outputs": [

                "Workflow Outputs"
            ],

            "use_cases": [

                "General Processing"
            ]
        }