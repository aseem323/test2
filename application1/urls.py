from django.urls import path
from .import views

urlpatterns = [
    path('test',views.testfn,name='test'),
    path('test2',views.test2fn,name='test2'),
]
