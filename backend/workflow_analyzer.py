class WorkflowAnalyzer:

    def analyze(
        self,
        workflow
    ):

        nodes = workflow.get(
            "nodes",
            []
        )

        links = workflow.get(
            "links",
            []
        )

        node_types = []

        input_nodes = []

        output_nodes = []

        workflow_stages = []

        unused_nodes = []

        node_ids_with_links = set()

        for link in links:

            try:

                source_id = link[1]
                target_id = link[3]

                node_ids_with_links.add(
                    source_id
                )

                node_ids_with_links.add(
                    target_id
                )

            except Exception:

                pass

        for node in nodes:

            node_type = str(
                node.get(
                    "type",
                    ""
                )
            )

            node_types.append(
                node_type
            )

            lower = (
                node_type.lower()
            )

            #
            # INPUTS
            #

            if (

                "load"
                in lower

                or

                "input"
                in lower

                or

                "video"
                in lower

                or

                "image"
                in lower
            ):

                input_nodes.append(
                    node_type
                )

            #
            # OUTPUTS
            #

            if (

                "save"
                in lower

                or

                "output"
                in lower

                or

                "preview"
                in lower
            ):

                output_nodes.append(
                    node_type
                )

            #
            # UNUSED
            #

            node_id = node.get(
                "id"
            )

            if (
                node_id
                not in
                node_ids_with_links
            ):

                unused_nodes.append(
                    node_type
                )

            workflow_stages.append({

                "node":
                    node_type,

                "description":
                    self.describe_node(
                        node_type
                    )
            })

        workflow_type = (
            self.detect_workflow_type(
                node_types
            )
        )

        return {

            "workflow_type":
                workflow_type,

            "node_count":
                len(nodes),

            "link_count":
                len(links),

            "input_nodes":
                list(
                    dict.fromkeys(
                        input_nodes
                    )
                ),

            "output_nodes":
                list(
                    dict.fromkeys(
                        output_nodes
                    )
                ),

            "workflow_stages":
                workflow_stages,

            "all_node_types":
                node_types,

            "complexity":
                self.calculate_complexity(
                    len(nodes)
                ),

            "unused_nodes":
                list(
                    dict.fromkeys(
                        unused_nodes
                    )
                ),

            "branch_count":
                self.calculate_branch_count(
                    links
                ),

            "dependency_count":
                len(links),

            "missing_inputs":
                []
        }

    def detect_workflow_type(
        self,
        node_types
    ):

        text = " ".join(
            [
                str(n).lower()
                for n in node_types
            ]
        )

        #
        # VIDEO → EXR
        #

        if (

            "vhs_loadvideo"
            in text

            and

            "saveexrframes"
            in text
        ):

            return (
                "Video To EXR Workflow"
            )

        #
        # VIDEO
        #

        if (

            "vhs_loadvideo"
            in text

            or

            "video"
            in text
        ):

            return (
                "Video Workflow"
            )

        #
        # UPSCALE
        #

        if (

            "upscale"
            in text

            or

            "esrgan"
            in text
        ):

            return (
                "Upscale Workflow"
            )

        #
        # INPAINT
        #

        if (

            "mask"
            in text

            or

            "inpaint"
            in text
        ):

            return (
                "Inpainting Workflow"
            )

        #
        # CONTROLNET
        #

        if (
            "controlnet"
            in text
        ):

            return (
                "ControlNet Workflow"
            )

        #
        # FLUX
        #

        if (

            "unetloader"
            in text

            or

            "flux"
            in text
        ):

            return (
                "Flux Workflow"
            )

        #
        # SDXL
        #

        if (
            "checkpointloader"
            in text
        ):

            return (
                "Image Generation Workflow"
            )

        #
        # IMAGE
        #

        if (
            "loadimage"
            in text
        ):

            return (
                "Image Processing Workflow"
            )

        return (
            "Generic Workflow"
        )

    def calculate_complexity(
        self,
        node_count
    ):

        if node_count < 10:

            return "Simple"

        if node_count < 30:

            return "Medium"

        return "Complex"

    def calculate_branch_count(
        self,
        links
    ):

        outputs = {}

        for link in links:

            try:

                source_id = link[1]

                outputs[
                    source_id
                ] = outputs.get(
                    source_id,
                    0
                ) + 1

            except Exception:

                pass

        count = 0

        for value in outputs.values():

            if value > 1:

                count += 1

        return count

    def describe_node(
        self,
        node_type
    ):

        lower = (
            str(node_type)
            .lower()
        )

        if (
            "unetloader"
            in lower
        ):

            return (
                "Loads the AI image generation model."
            )

        if (
            "cliploader"
            in lower
        ):

            return (
                "Loads the text understanding model."
            )

        if (
            "vaeloader"
            in lower
        ):

            return (
                "Loads the image decoder."
            )

        if (
            "ksampler"
            in lower
        ):

            return (
                "Generates the image."
            )

        if (
            "decode"
            in lower
        ):

            return (
                "Builds the final image."
            )

        if (
            "save"
            in lower
        ):

            return (
                "Exports the final result."
            )

        if (
            "vhs_loadvideo"
            in lower
        ):

            return (
                "Loads source video footage."
            )

        if (
            "saveexrframes"
            in lower
        ):

            return (
                "Exports frames as EXR sequence."
            )

        if (
            "loadimage"
            in lower
        ):

            return (
                "Loads an image."
            )

        if (
            "upscale"
            in lower
        ):

            return (
                "Enhances image resolution."
            )

        return (
            "Processes workflow data."
        )