from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.home, name="create"),
    path(
        "oauth/callback/",
        views.callback,
        name="oauth_callback",
    ),
]
