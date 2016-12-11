from django.conf.urls import url
from .views import MyAppView, MyExceptionView

urlpatterns = [
    url(r'^$',
        MyAppView.as_view(),
        name='index',
    ),
    url(r'^exception$',
        MyExceptionView.as_view(),
        name='exception',
    )
]