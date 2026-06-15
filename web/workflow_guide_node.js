import { app } from "../../scripts/app.js";

function removeExistingPanels() {

    const nodes =
        app.graph._nodes || [];

    const panels =
        nodes.filter(
            n =>
                n.type ===
                "WorkflowDocumentationPanelNode"
        );

    for (const panel of panels) {

        app.graph.remove(
            panel
        );
    }
}

function getPanelPosition() {

    const nodes =
        app.graph._nodes || [];

    if (!nodes.length) {

        return [100, 100];
    }

    let minX = Infinity;
    let minY = Infinity;

    for (const node of nodes) {

        if (
            node.type ===
            "WorkflowDocumentationPanelNode"
        ) {
            continue;
        }

        if (!node.pos) {
            continue;
        }

        minX = Math.min(
            minX,
            node.pos[0]
        );

        minY = Math.min(
            minY,
            node.pos[1]
        );
    }

    return [

        minX - 1150,

        minY
    ];
}

function createPanel(
    documentation
) {

    const panel =
        LiteGraph.createNode(
            "WorkflowDocumentationPanelNode"
        );

    if (!panel) {

        console.error(
            "WorkflowDocumentationPanelNode not found"
        );

        return;
    }

    panel.title =
        "🎨 Artist Workflow Guide";

    panel.pos =
        getPanelPosition();

    panel.size = [
        1100,
        2200
    ];

    panel.properties =
        panel.properties || {};

    panel.properties.documentation = {

        //
        // OVERVIEW
        //

        workflow_type:
            documentation.workflow_type || "",

        purpose:
            documentation.purpose || "",

        overview:
            documentation.overview || "",

        difficulty:
            documentation.difficulty || "",

        estimated_vram:
            documentation.estimated_vram || "",

        //
        // MODELS
        //

        main_models:
            documentation.main_models || [],

        text_encoders:
            documentation.text_encoders || [],

        vaes:
            documentation.vaes || [],

        loras:
            documentation.loras || [],

        controlnets:
            documentation.controlnets || [],

        upscalers:
            documentation.upscalers || [],

        //
        // MODEL ANALYSIS
        //

        model_parameters:
            documentation.model_parameters || {},

        model_explanations:
            documentation.model_explanations || [],

        //
        // NODE EXPLANATIONS
        //

        node_purposes:
            documentation.node_purposes || [],

        //
        // SETTINGS
        //

        sampler:
            documentation.sampler || "Not Detected",

        scheduler:
            documentation.scheduler || "Not Detected",

        steps_count:
            documentation.steps_count || "Not Detected",

        cfg:
            documentation.cfg || "Not Detected",

        resolution:
            documentation.resolution || "Not Detected",

        seed:
            documentation.seed || "Random",

        denoise:
            documentation.denoise || "Not Detected",

        flux_guidance:
            documentation.flux_guidance || null,

        //
        // FLOW
        //

        workflow_flow:
            documentation.workflow_flow || [],

        workflow_diagram:
            documentation.workflow_diagram || [],

        //
        // OUTPUT
        //

        output:
            documentation.output || "Generated Output",

        //
        // PERFORMANCE
        //

        performance_tips:
            documentation.performance_tips || [],

        //
        // ARTIST INFORMATION
        //

        recommended_users:
            documentation.recommended_users || [],

        required_inputs:
            documentation.required_inputs || [],

        produced_outputs:
            documentation.produced_outputs || [],

        use_cases:
            documentation.use_cases || [],

        //
        // WORKFLOW ANALYSIS
        //

        input_nodes:
            documentation.input_nodes || [],

        output_nodes:
            documentation.output_nodes || [],

        complexity:
            documentation.complexity || "",

        workflow_stages:
            documentation.workflow_stages || [],

        branch_count:
            documentation.branch_count || 0,

        dependency_count:
            documentation.dependency_count || 0,

        unused_nodes:
            documentation.unused_nodes || [],

        missing_inputs:
            documentation.missing_inputs || []
    };

    app.graph.add(
        panel
    );

    app.graph.setDirtyCanvas(
        true,
        true
    );

    console.log(
        "[Workflow Guide Panel Data]",
        panel.properties.documentation
    );
}

app.registerExtension({

    name:
        "WorkflowGuideGenerator",

    async beforeRegisterNodeDef(
        nodeType,
        nodeData
    ) {

        if (
            nodeData.name !==
            "WorkflowGuideNode"
        ) {

            return;
        }

        const original =
            nodeType.prototype.onNodeCreated;

        nodeType.prototype.onNodeCreated =
            function () {

                if (original) {

                    original.apply(
                        this,
                        arguments
                    );
                }

                this.size = [
                    320,
                    140
                ];

                this.addWidget(

                    "button",

                    "Generate Artist Guide",

                    null,

                    async () => {

                        try {

                            const workflow =
                                app.graph.serialize();

                            const response =
                                await fetch(
                                    "/workflow-guide/generate",
                                    {
                                        method:
                                            "POST",

                                        headers:
                                        {
                                            "Content-Type":
                                                "application/json"
                                        },

                                        body:
                                            JSON.stringify(
                                                workflow
                                            )
                                    }
                                );

                            const result =
                                await response.json();

                            console.log(
                                "[Workflow Guide Result]",
                                result
                            );

                            if (
                                !result.success
                            ) {

                                console.error(
                                    result
                                );

                                alert(
                                    "Guide generation failed."
                                );

                                return;
                            }

                            removeExistingPanels();

                            createPanel(
                                result
                            );

                            app.graph.setDirtyCanvas(
                                true,
                                true
                            );

                            console.log(
                                "[Workflow Guide] Generated Successfully"
                            );
                        }
                        catch (
                            error
                        ) {

                            console.error(
                                error
                            );

                            alert(
                                "Guide generation failed."
                            );
                        }
                    }
                );

                console.log(
                    "[Workflow Guide Generator] Ready"
                );
            };
    }
});