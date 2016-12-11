class DjangoMiddlewareInProject(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print('proj: one-time cofiguration')

    def __call__(self, request):
        print('proj: before request')
        response = self.get_response(request)
        print('proj: after request')
        
        return response
        