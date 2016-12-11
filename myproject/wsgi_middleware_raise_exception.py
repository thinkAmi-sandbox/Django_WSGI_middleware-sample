class WSGIMiddlewareRaiseException(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print('called: WSGIMiddlewareRaiseException')
        raise AssertionError

        self.app(environ, start_response)