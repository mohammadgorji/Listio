from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("list/<int:id>", views.todolist, name="list"),
    path('delete/<list_id>', views.delete, name='delete'),
]