from django.urls import path
from .views import aboutView

app_name="bitacora"

urlpatterns = [
    path('', aboutView.as_view(), name="home"),

]