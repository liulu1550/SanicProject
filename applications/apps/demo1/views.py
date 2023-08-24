from sanic import Request, HTTPResponse
from sanic.views import HTTPMethodView

from core.response import response_ok


async def demo1_view(request: Request) -> HTTPResponse:
    """
    测试视图
    :param request:
    :return:123
    """

    return response_ok()


class DemoAPIView(HTTPMethodView):
    """
    Demo类视图
    """

    async def get(self, request: Request) -> HTTPResponse:
        """
        This is the endpoint description.
        ---
        parameters:
          - name: name
            description: Your name
            in: query
            required: true
            type: string
        responses:
          200:
        description: OK
        """
        name = request.args.get('name', None)
        age = int(request.args.get('age', 18))

        result = {
            "name": name,
            "age": age
        }
        return response_ok(result)

    async def post(self, request: Request) -> HTTPResponse:
        name = request.json.get('name', None)
        age = int(request.json.get('age', 18))

        result = {
            "name": name,
            "age": age
        }
        return response_ok(result)
