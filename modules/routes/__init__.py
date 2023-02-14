
from modules.routes.common import *
from modules.routes.index import index_get_route
from modules.routes.auth import login_get_route, logout_get_route
from modules.routes.profile import profile_self_get_route

routes = [
    Route(
        '/',
        index_get_route,
        methods = ['GET'],
        name = 'index_get_route'
    ),
    
    Route(
        '/login',
        login_get_route,
        methods = ['GET'],
        name = 'login_get_route'
    ),   
    
    Route(
        '/logout',
        logout_get_route,
        methods = ['GET'],
        name = 'logout_get_route'
    ),  
    
    Route(
        '/profile',
        profile_self_get_route,
        methods = ['GET'],
        name = 'profile_self_get_route'
    ),

   # Route(
    #    '/login',
   #     login_post_route,
  #      methods = ['POST'],
 #       name = 'login_post_route'
#    ),


    Mount(
        '/res',
        app = StaticFiles(
            directory = 'resources'
        ),
        name = 'resouces_route'
    )
]

middleware = [
    Middleware( SessionMiddleware, secret_key = 'topsecret', max_age = None )
]

exception_handlers = {
    
}

def get_app( config_data: dict ) -> Starlette:
    return Starlette(
        routes = routes,
        middleware = middleware,
        exception_handlers = exception_handlers
    )
