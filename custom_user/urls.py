from django.contrib import admin
from django.urls import path

from myuser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="homepage"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]