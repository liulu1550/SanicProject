from sanic import Blueprint

from applications.apps.demo2.views import demo2_view

router: Blueprint = Blueprint('demo2', url_prefix='demo2')


router.add_route(demo2_view, "/demo2", ('GET',))