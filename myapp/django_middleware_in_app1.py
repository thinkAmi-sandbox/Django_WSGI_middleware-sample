class DjangoMiddlewareInApp1(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print('app1: one-time cofiguration')

    def __call__(self, request):
        print('app1: before request')
        response = self.get_response(request)
        print('app1: after request')

        return response