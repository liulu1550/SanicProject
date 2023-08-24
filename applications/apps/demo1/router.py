from sanic import Blueprint

from applications.apps.demo1.views import demo1_view

router: Blueprint = Blueprint('demo1', url_prefix='apps/demo1')


router.add_route(demo1_view, "/demo1", ('GET',))