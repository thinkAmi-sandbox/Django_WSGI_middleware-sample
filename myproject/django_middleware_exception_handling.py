class DjangoMiddlewareExceptionHandling(object):
    def __init__(self, get_response):
        self.get_response = get_response
        print('django_middleware: one-time cofiguration')

    def __call__(self, request):
        print('django_middleware: before request')

        try:
            response = self.get_response(request)
            print('Django response data:{}'.format(response))
        except:
            print('handled exception by DjangoMiddlewareExceptionHandling')

        print('django_middleware: after request')
        return response

    def process_exception(self, request, exception):
        print('handled exception by process_exception in DjangoMiddlewareExceptionHandling')