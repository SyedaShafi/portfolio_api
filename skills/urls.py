from django.urls import path
from . import views
urlpatterns = [
    path('', views.allAPIView),
    path('list/', views.SkillListView.as_view()),
    path('create/', views.SkillsCreateView.as_view()),
    path('detail/<int:pk>/', views.SkillsDetailView.as_view()),
    path('update/<int:pk>/', views.SkillsUpdateView.as_view()),
    path('delete/<int:pk>/', views.SkillsDeleteView.as_view()),
]
