
from modules.routes.common import *
from modules.routes.index_get import index_get_route

routes = [
    Route(
        '/',
        index_get_route,
        methods = ['GET'],
        name = 'index_route'
    ),
    
    Mount(
        '/res',
        app = StaticFiles(
            directory = 'resources'
        ),
        name = 'resouces_route'
    )
]

exception_handlers = {

}

def get_app() -> Starlette:
    return Starlette(
        routes = routes,
        exception_handlers = exception_handlers
    )
