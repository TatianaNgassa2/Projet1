from django.urls import path
from django.conf.urls import include, url
from . import views
from .views import LoginUserView

app_name = "EquipementSportif"


urlpatterns = [

    path("home", views.homepage, name="home"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login/",  view=LoginUserView.as_view(), name="login"),


]