from django.urls import path
from .views import Detail, Homepage, Results, Vote
urlpatterns = [
        path('', Homepage.as_view(), name='index'),
        path('<int:question_id>/', Detail.as_view(), name='detail'),
        path('<int:question_id>/results/', Results.as_view(), name='results'),
        path('<int:question_id>/vote/', Vote.as_view(), name='vote'),
]
