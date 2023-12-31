from sanic import Blueprint

from applications.apps.demo2.views import demo2_view, get_location

router: Blueprint = Blueprint('demo2', url_prefix='demo2')


router.add_route(demo2_view, "/demo2", ('GET',))
router.add_route(get_location, "/location", ('GET',))

