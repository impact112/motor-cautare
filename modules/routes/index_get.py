
from modules.routes.common import *

async def index_get_route( request: Request ):
    return HTMLResponse( 'TEST' )
