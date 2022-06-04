
# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [StartApp] 〕≜╠《_⋐⫸⊱¤⥑⌘
Aca estaran las otras vistas las vistas 
secudarias...

# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [About] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# About: 
    
    django-admin startapp about

## about/views.py: 

    from django.shortcuts import render
    from django.views.generic import View


    class aboutView(View):
        def get(self,request, *args, **kwargs):
            context={
                
            }
            return render(request,'about/about.html', context)
    
## about/urls.py:

    from django.urls import path
    from .views import aboutView

    app_name="about"

    urlpatterns = [
        path('', aboutView.as_view(), name="about"),

    ]

## core/urls.py:

    path('about/', include('about.urls',namespace='about')),

## core/settings.py:

*INSTALLED_APPS*

    'about',

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 

# templates
crear carpeta about y dentro de ella about.html

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 

# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [Bitacora] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# Bitacora: 
    
    django-admin startapp bitacora

## bitacora/views.py: 

    from django.shortcuts import render
    from django.views.generic import View


    class aboutView(View):
        def get(self,request, *args, **kwargs):
            context={
                
            }
            return render(request,'bitacora/bitacora.html', context)
    
## bitacora/urls.py:

    from django.urls import path
    from .views import aboutView

    app_name="bitacora"

    urlpatterns = [
        path('', aboutView.as_view(), name="home"),

    ]

## core/urls.py:

    path('bitacora/', include('bitacora.urls',namespace='bitacora')),

## core/settings.py:

*INSTALLED_APPS*

    'bitacora',

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 

# templates
crear carpeta bitacora y dentro de ella bitacora.html

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐