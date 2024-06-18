from django.urls import path
from .import views
urlpatterns = [
    path('', views.allAPIView),
    path('list/', views.ProjectListView.as_view()),
    path('create/', views.ProjectCreateView.as_view()),
    path('detail/<int:pk>/', views.ProjectDetailView.as_view()),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view()),
    path('delete/<int:pk>/', views.ProjectDeleteView.as_view()),
]
