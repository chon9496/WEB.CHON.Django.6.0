from django.urls import path
from .views import bitacoraView,descargar,noticiasLista,noticiasDetail,noticiasCreate,noticiasUpdate,noticiasDelete

app_name="bitacora"

urlpatterns = [
    path('', bitacoraView.as_view(), name="home"),
    
    path('descargar/', descargar.as_view(), name="descargar"),
    
    path('noticias/', noticiasCreate.as_view(), name="noticias"),
    path('lista/', noticiasLista.as_view(), name="list"),
    path('detalle/', noticiasDetail.as_view(), name="detail"),
    path('actualizacion/', noticiasUpdate.as_view(), name="update"),
    path('elininar/', noticiasDelete.as_view(), name="delete"),
]


