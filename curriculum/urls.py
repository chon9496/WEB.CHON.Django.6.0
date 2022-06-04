from django.urls import path
from .views import CurriView

app_name="curriculum"

urlpatterns = [
    path('', CurriView.as_view(), name="home"),

]