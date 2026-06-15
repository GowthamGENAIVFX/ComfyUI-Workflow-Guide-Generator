from .workflow_analyzer import (
    WorkflowAnalyzer
)

from .workflow_purpose_engine import (
    WorkflowPurposeEngine
)

from .workflow_diagram_engine import (
    WorkflowDiagramEngine
)

from .workflow_insights_engine import (
    WorkflowInsightsEngine
)

from .model_discovery_engine import (
    ModelDiscoveryEngine
)

from .model_parameter_engine import (
    ModelParameterEngine
)

from .model_explanation_engine import (
    ModelExplanationEngine
)

from .workflow_flow_engine import (
    WorkflowFlowEngine
)

from .node_purpose_engine import (
    NodePurposeEngine
)


class WorkflowDocumentationEngine:

    def __init__(self):

        self.analyzer = (
            WorkflowAnalyzer()
        )

        self.purpose_engine = (
            WorkflowPurposeEngine()
        )

        self.diagram_engine = (
            WorkflowDiagramEngine()
        )

        self.insights_engine = (
            WorkflowInsightsEngine()
        )

        self.model_discovery = (
            ModelDiscoveryEngine()
        )

        self.model_parameter_engine = (
            ModelParameterEngine()
        )

        self.model_explanation_engine = (
            ModelExplanationEngine()
        )

        self.flow_engine = (
            WorkflowFlowEngine()
        )

        self.node_purpose_engine = (
            NodePurposeEngine()
        )

    def generate(
        self,
        workflow
    ):

        analysis = (
            self.analyzer.analyze(
                workflow
            )
        )

        purpose_info = (
            self.purpose_engine.generate(
                analysis[
                    "workflow_type"
                ],
                analysis
            )
        )

        workflow_diagram = (
            self.diagram_engine.generate(
                workflow,
                analysis.get(
                    "workflow_stages",
                    []
                )
            )
        )

        insights = (
            self.insights_engine.generate(
                workflow
            )
        )

        discovered_models = (
            self.model_discovery.discover(
                workflow
            )
        )

        model_parameters = (
            self.model_parameter_engine.extract(
                workflow
            )
        )

        model_explanations = (
            self.model_explanation_engine.build(
                discovered_models
            )
        )

        workflow_flow = (
            self.flow_engine.generate(
                workflow
            )
        )

        node_purposes = (
            self.node_purpose_engine.build(
                workflow
            )
        )

        return {

            #
            # STATUS
            #

            "success":
                True,

            #
            # OVERVIEW
            #

            "workflow_type":
                analysis.get(
                    "workflow_type",
                    "Unknown Workflow"
                ),

            "overview":
                self.generate_overview(
                    analysis,
                    purpose_info
                ),

            "purpose":
                purpose_info.get(
                    "purpose",
                    ""
                ),

            "difficulty":
                purpose_info.get(
                    "difficulty",
                    "Unknown"
                ),

            "estimated_vram":
                purpose_info.get(
                    "estimated_vram",
                    "Unknown"
                ),

            #
            # MODELS
            #

            "main_models":
                discovered_models.get(
                    "main_models",
                    []
                ),

            "text_encoders":
                discovered_models.get(
                    "text_encoders",
                    []
                ),

            "vaes":
                discovered_models.get(
                    "vaes",
                    []
                ),

            "loras":
                discovered_models.get(
                    "loras",
                    []
                ),

            "controlnets":
                discovered_models.get(
                    "controlnets",
                    []
                ),

            "upscalers":
                discovered_models.get(
                    "upscalers",
                    []
                ),

            #
            # MODEL DETAILS
            #

            "model_parameters":
                model_parameters,

            "model_explanations":
                model_explanations,

            #
            # NODE DETAILS
            #

            "node_purposes":
                node_purposes,

            #
            # SETTINGS
            #

            "sampler":
                insights.get(
                    "sampler",
                    "Not Detected"
                ),

            "scheduler":
                insights.get(
                    "scheduler",
                    "Not Detected"
                ),

            "steps_count":
                insights.get(
                    "steps",
                    "Not Detected"
                ),

            "cfg":
                insights.get(
                    "cfg",
                    "Not Detected"
                ),

            "resolution":
                insights.get(
                    "resolution",
                    "Not Detected"
                ),

            "output":
                insights.get(
                    "output",
                    "Generated Output"
                ),

            #
            # FLOW
            #

            "workflow_flow":
                workflow_flow,

            "workflow_diagram":
                workflow_diagram,

            #
            # PERFORMANCE
            #

            "performance_tips":
                insights.get(
                    "performance_tips",
                    []
                ),

            #
            # ARTIST INFO
            #

            "recommended_users":
                purpose_info.get(
                    "recommended_users",
                    []
                ),

            "required_inputs":
                purpose_info.get(
                    "required_inputs",
                    []
                ),

            "produced_outputs":
                purpose_info.get(
                    "produced_outputs",
                    []
                ),

            "use_cases":
                purpose_info.get(
                    "use_cases",
                    []
                ),

            #
            # ANALYSIS
            #

            "input_nodes":
                analysis.get(
                    "input_nodes",
                    []
                ),

            "output_nodes":
                analysis.get(
                    "output_nodes",
                    []
                ),

            "complexity":
                analysis.get(
                    "complexity",
                    "Unknown"
                ),

            "workflow_stages":
                analysis.get(
                    "workflow_stages",
                    []
                ),

            "branch_count":
                analysis.get(
                    "branch_count",
                    0
                ),

            "dependency_count":
                analysis.get(
                    "dependency_count",
                    0
                ),

            "unused_nodes":
                analysis.get(
                    "unused_nodes",
                    []
                ),

            "missing_inputs":
                analysis.get(
                    "missing_inputs",
                    []
                )
        }

    def generate_overview(
        self,
        analysis,
        purpose_info
    ):

        workflow_type = (
            analysis.get(
                "workflow_type",
                "Workflow"
            )
        )

        node_count = (
            analysis.get(
                "node_count",
                0
            )
        )

        link_count = (
            analysis.get(
                "link_count",
                0
            )
        )

        purpose = (
            purpose_info.get(
                "purpose",
                ""
            )
        )

        return (

            f"{purpose} "

            f"This {workflow_type.lower()} "

            f"contains "

            f"{node_count} nodes "

            f"and "

            f"{link_count} connections."
        )