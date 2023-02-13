
from modules.routes.common import *

async def login_get_route( request: Request ):
    if 'username' in request.query_params:
        request.session['username'] = request.query_params.get('username')
    return RedirectResponse( url = '/' )

async def logout_get_route( request: Request ):
    request.session.clear()
    return RedirectResponse( url = '/' )
