from django.urls import path
from . import views

urlpatterns = [

    # ex: /training_app/
    path('', views.index, name='index'),
    # ex: /training_app/next_depth
    path('next_depth', views.next_depth, name='next_depth'),
    # ex: /training_app/5/
    path('<int:training_id>/', views.detail, name='detail'),
    # ex: /training_app/5/results/
    path('<int:training_id>/results/', views.results, name='results'),
    # ex: /training_app/5/vote/
    path('<int:training_id>/vote/', views.vote, name='vote'),
]
