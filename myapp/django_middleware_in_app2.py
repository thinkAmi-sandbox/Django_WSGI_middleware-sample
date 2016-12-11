class DjangoMiddlewareInApp2(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print('app2: one-time cofiguration')

    def __call__(self, request):
        print('app2: before request')
        response = self.get_response(request)
        print('app2: after request')
        
        return response