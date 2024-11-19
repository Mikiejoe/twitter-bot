from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "oauth/callback/",
        views.callback,
        name="oauth_callback",
    ),
]
