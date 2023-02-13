
from modules.routes.common import *

async def profile_self_get_route( request: Request ):
    return HTMLResponse('Username: ' + request.session['username'])
