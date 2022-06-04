
# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [StartApp] 〕≜╠《_⋐⫸⊱¤⥑⌘
Aca estaran las otras vistas las vistas 
secudarias...

# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [Contacto] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# Contacto: 
    
    django-admin startapp contacto

## contacto/views.py: 

    from django.shortcuts import render
    from django.views.generic import View


    class ContactoView(View):
        def get(self,request, *args, **kwargs):
            context={
                
            }
            return render(request,'contacto/contacto.html', context)
    
## contacto/urls.py:

    from django.urls import path
    from .views import ContactoView

    app_name="contacto"

    urlpatterns = [
        path('', ContactoView.as_view(), name="home"),

    ]

## core/urls.py:

    path('contacto/', include('contacto.urls',namespace='contacto')),

## core/settings.py:

*INSTALLED_APPS*

    'contacto',

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 

# templates
crear carpeta contacto y dentro de ella contacto.html

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗