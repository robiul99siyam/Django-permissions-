from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/",views.api_views.as_view()),
    path("",views.List_views.as_view()),
    path("create/",views.create_view.as_view())

]