"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()

# addition
from .wsgi_middleware_raise_exception import WSGIMiddlewareRaiseException
application = WSGIMiddlewareRaiseException(application)

from .wsgi_middleware_exception_handling import WSGIMiddlewareExceptionHandling
application = WSGIMiddlewareExceptionHandling(application)

from wsgi_lineprof.middleware import LineProfilerMiddleware
application = LineProfilerMiddleware(application)

