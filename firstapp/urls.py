from django.urls import path
from firstapp import views

app_name = 'firstapp'

urlpatterns = [
    path('', views.index, name='index'),      # /firstapp/
    path('<int:question_id>/', views.detail, name='detail'),       # /firstapp/5/
    path('<int:question_id>/results/', views.results, name='results'),     # /firstapp/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # /firstapp/5/vote/
]