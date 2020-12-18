from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('todos/', views.TodoCreateList.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),

    path('signup', views.signup),
]