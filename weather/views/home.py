"""Module contains home page routes."""
import fastapi
from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates

from weather import TEMPLATES_PATH
from weather.services import report

templates = Jinja2Templates(directory=TEMPLATES_PATH)
router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
async def home(request: Request) -> Response:
    """Returns a route to home page."""
    return templates.TemplateResponse(
        name='home/index.html',
        context={'request': request, 'events': await report.reports()},
    )
