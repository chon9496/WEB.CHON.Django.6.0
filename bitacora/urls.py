from django.urls import path
from .views import bitacoraView

app_name="bitacora"

urlpatterns = [
    path('', bitacoraView.as_view(), name="home"),

]