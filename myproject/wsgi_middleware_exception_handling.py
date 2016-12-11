class WSGIMiddlewareExceptionHandling(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print("called: WSGIMiddlewareExceptionHandling")

        try:
            return self.app(environ, start_response)
        except:
            print('handled exception by WSGIMiddlewareExceptionHandling')
            start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
            return [b"raised exception."]