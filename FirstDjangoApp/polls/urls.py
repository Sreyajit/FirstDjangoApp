from django.urls import path
from .views import Response 
urlpatterns = [
        path('', Response.as_view(), name='index'),
]
