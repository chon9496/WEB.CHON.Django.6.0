
# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [StartApp] 〕≜╠《_⋐⫸⊱¤⥑⌘
Aca estaran las otras vistas las vistas 
secudarias...

# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [Curriculum] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# Curriculum: 
    
    django-admin startapp curriculum

## curriculum/views.py: 
    
    from django.views.generic import View

    class CurriView(View):
        def get(self,request, *args, **kwargs):
            context={
                
            }
            return render(request,'curriculum/curriculum.html', context)

## curriculum/urls.py:

    from django.urls import path
    from .views import CurriView

    app_name="curriculum"

    urlpatterns = [
        path('', CurriView.as_view(), name="home"),

    ]

## core/urls.py:

    path('curriculum/', include('curriculum.urls',namespace='curriculum')),

## core/settings.py:

*INSTALLED_APPS*

    'curriculum',
    
# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 

# templates
crear carpeta curriculum y dentro de ella curriculum.html

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 