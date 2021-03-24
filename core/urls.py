from django.urls import path

from .views import IndexView#, NotFoundView, ProcessErrorView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('404/', NotFoundView.as_view(), name='404'),
    #path('500/', ProcessErrorView.as_view(), name='500')
]