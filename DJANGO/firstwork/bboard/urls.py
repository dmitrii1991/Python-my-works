
from django.urls import path
from .views import index, by_rubric, BdCreateView

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('add/', BdCreateView.as_view(), name='add'),
    path('', index, name='index'),
    ]