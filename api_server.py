from aiohttp import web

from server import PromptServer

from .backend.workflow_documentation_engine import (
    WorkflowDocumentationEngine
)

routes = PromptServer.instance.routes

documentation_engine = (
    WorkflowDocumentationEngine()
)


@routes.post(
    "/workflow-guide/generate"
)
async def workflow_guide_generate(
    request
):

    try:

        workflow = await request.json()

        documentation = (
            documentation_engine.generate(
                workflow
            )
        )

        return web.json_response(
            documentation
        )

    except Exception as error:

        import traceback

        traceback.print_exc()

        return web.json_response({

            "success": False,

            "error": str(
                error
            )
        })