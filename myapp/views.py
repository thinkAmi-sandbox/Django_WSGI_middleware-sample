from django.views import View
from django.http import HttpResponse

class MyAppView(View):
    def get(self, request, *args, **kwargs):
        print('called: MyAppView')
        return HttpResponse('Hello world')


class MyExceptionView(View):
    def get(self, request, *args, **kwargs):
        print('called: MyExceptionView')
        raise AssertionError(request)

        return HttpResponse('raised exception')