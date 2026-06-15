import { app } from "../../scripts/app.js";

function wrapText(
    ctx,
    text,
    maxWidth
) {

    if (!text) {
        return [""];
    }

    const words =
        String(text)
        .split(" ");

    const lines = [];

    let current = "";

    for (const word of words) {

        const test =
            current
                ? current + " " + word
                : word;

        if (
            ctx.measureText(
                test
            ).width > maxWidth
        ) {

            if (current) {
                lines.push(
                    current
                );
            }

            current = word;
        }
        else {

            current = test;
        }
    }

    if (current) {
        lines.push(
            current
        );
    }

    return lines;
}

app.registerExtension({

    name:
        "WorkflowDocumentationPanel",

    async beforeRegisterNodeDef(
        nodeType,
        nodeData
    ) {

        if (
            nodeData.name !==
            "WorkflowDocumentationPanelNode"
        ) {

            return;
        }

        nodeType.prototype.onNodeCreated =
            function () {

                this.size = [
                    850,
                    900
                ];
            };

        nodeType.prototype.onDrawForeground =
            function (
                ctx
            ) {

                const doc =
                    this.properties
                        ?.documentation;

                if (!doc) {
                    return;
                }

                const WIDTH =
                    this.size[0];

                const CARD_X = 15;
                const CARD_W =
                    WIDTH - 30;

                let y = 15;

                const BG =
                    "#1c1c1c";

                const CARD =
                    "#252525";

                const BORDER =
                    "#3d3d3d";

                const TITLE =
                    "#ffffff";

                const LABEL =
                    "#f4c542";

                const TEXT =
                    "#d0d0d0";

                const drawCard =
                (
                    title,
                    contentLines
                ) => {

                    const wrappedLines = [];

                    ctx.font =
                        "15px Arial";

                    for (
                        const line
                        of contentLines
                    ) {

                        const wrapped =
                            wrapText(
                                ctx,
                                String(line),
                                CARD_W - 50
                            );

                        wrappedLines.push(
                            ...wrapped
                        );
                    }

                    const height =
                        70 +
                        (
                            wrappedLines.length
                            * 24
                        );

                    ctx.fillStyle =
                        CARD;

                    ctx.strokeStyle =
                        BORDER;

                    ctx.lineWidth = 1;

                    ctx.beginPath();

                    ctx.roundRect(
                        CARD_X,
                        y,
                        CARD_W,
                        height,
                        10
                    );

                    ctx.fill();
                    ctx.stroke();

                    ctx.fillStyle =
                        LABEL;

                    ctx.font =
                        "bold 18px Arial";

                    ctx.fillText(
                        title,
                        CARD_X + 15,
                        y + 28
                    );

                    ctx.fillStyle =
                        TEXT;

                    ctx.font =
                        "15px Arial";

                    let textY =
                        y + 55;

                    for (
                        const line
                        of wrappedLines
                    ) {

                        ctx.fillText(
                            line,
                            CARD_X + 20,
                            textY
                        );

                        textY += 22;
                    }

                    y +=
                        height + 15;
                };

                ctx.fillStyle =
                    BG;

                ctx.fillRect(
                    0,
                    0,
                    this.size[0],
                    this.size[1]
                );

                ctx.fillStyle =
                    TITLE;

                ctx.font =
                    "bold 22px Arial";

                ctx.fillText(
                    "🎨 Artist Workflow Guide",
                    20,
                    y + 25
                );

                y += 50;

                drawCard(
                    "🎯 WORKFLOW PURPOSE",
                    wrapText(
                        ctx,
                        doc.purpose ||
                        "Not Available",
                        CARD_W - 40
                    )
                );

                drawCard(
                    "📋 OVERVIEW",
                    wrapText(
                        ctx,
                        doc.overview ||
                        "",
                        CARD_W - 40
                    )
                );

                drawCard(
                    "📥 MODELS USED",
                    [

                        `Main Model: ${
                            doc.main_models?.[0]
                            || "Not Detected"
                        }`,

                        `Text Encoder: ${
                            doc.text_encoders?.[0]
                            || "Not Detected"
                        }`,

                        `Image Decoder: ${
                            doc.vaes?.[0]
                            || "Not Detected"
                        }`
                    ]
                );

                drawCard(
                    "⚙️ MAIN SETTINGS",
                    [

                        `Sampler: ${doc.sampler}`,
                        `Scheduler: ${doc.scheduler}`,
                        `Steps: ${doc.steps_count}`,
                        `CFG: ${doc.cfg}`,
                        `Resolution: ${doc.resolution}`,
                        `VRAM: ${doc.estimated_vram}`
                    ]
                );

                drawCard(
                    "🗺️ WORKFLOW FLOW",
                    (
                        doc.workflow_flow
                        || []
                    )
                );

                drawCard(
                    "🖼 OUTPUT",
                    [
                        doc.output
                        || "Generated Output"
                    ]
                );

                drawCard(
                    "🚀 PERFORMANCE TIPS",
                    (
                        doc.performance_tips
                        || []
                    )
                );

                const nodeLines =
                    [];

                for (
                    const node
                    of (
                        doc.node_purposes
                        || []
                    ).slice(
                        0,
                        12
                    )
                ) {

                    nodeLines.push(
                        `${node.title}: ${node.purpose}`
                    );
                }

                drawCard(
                    "📋 KEY NODES USED",
                    nodeLines
                );

                const newHeight =
                    Math.max(
                        y + 20,
                        700
                    );

                if (
                    Math.abs(
                        this.size[1]
                        - newHeight
                    ) > 5
                ) {

                    this.size[1] =
                        newHeight;
                }
            };
    }
});