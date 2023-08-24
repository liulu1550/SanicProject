from sanic import Blueprint

from applications.apps.demo1.views import demo1_view, DemoAPIView

router: Blueprint = Blueprint('demo1', url_prefix='demo1')


router.add_route(demo1_view, "/demo1", ('GET',))

router.add_route(DemoAPIView.as_view(), '/demo')