from django.urls import path

from authentication.views import home


urlpatterns = [
    path("", home.HomePageView.as_view(), name="home"),
]
