from django.contrib import admin
from django.urls import path
from tracker import views

urlpatterns = [
    path("", views.get_data, name="tracker"),
    path('admin/', admin.site.urls),
]
