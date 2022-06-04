# WEB.CHON.Django.6.0
 Version-Alfa.6.0

# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [Ambiente] 〕≜╠《_⋐⫸⊱¤⥑⌘

# Ambiente:

## Instalar:

    pip install virtualenv env

## Crear:

    virtualenv env
                     
## Activar:

    cd env/Scripts
    activate
    cd../..

### Activar en Linux y mac:

    source env/bin/activate

## requirements.txt:
Creamos un archivo con el nombre requirements.txt

Ejecutamos en la terminal

    pip install -r requirements.txt

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 

# ⌘⥏¤⊰⫷⋑_》╣≜ 〔 [Core] 〕≜╠《_⋐⫸⊱¤⥑⌘

# Startproject:

## Crear:

### Opcion 1:

    django-admin startproject core .

## core:

### core/settings.py:

*INSTALLED_APPS*

    'core',

*importamos*
    
    import os
    import environ

*instalamos environ*

    env    = environ.Env()
    environ.Env.read_env()

*cortamos SECRET_KEY y DEBUG y creamos una archivo .env luego lo sustituimos* 
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG')

*Permitirá cualquier nombre de host que venga en un encabezado de Host*
    
    ALLOWED_HOSTS  = ['*']

### Tailwind:

*INSTALLED_APPS*
    
    'tailwind',

*TERMINAL*

    python manage.py tailwind init

*INSTALLED_APPS*
    
    'theme',
    
*TAILWIND_APP_NAME*

    TAILWIND_APP_NAME = 'theme'
    INTERNAL_IPS = ["127.0.0.1",]

*TERMINAL*

    python manage.py tailwind install

### core/settings.py:

    NPM_BIN = "/usr/bin/npm"

*TEMPLATES*

    'DIRS': [os.path.join(BASE_DIR, 'templates')],

*añadimos estos urls al final*

    STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')] 
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_root') 
    MEDIA_URL  = '/media/' 
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media_static')

#### core/.env:
pegamos  

    SECRET_KEY=)@nuc8mylev)5mo&@h3#e602*b%7yb#()pxhkuxz=k8@_mytlz
    DEBUG=True

### Imagenes:
Para ello debemos de crear nustra carpeta static y media

### core/views.py:

    from django.shortcuts import render
    from django.views.generic import View

    class HomeView(View):
        def get(self,request, *args, **kwargs):
            context={
                
            }
            return render(request,'index.html', context)

### core/urls.py:

    from django.conf import settings 
    from django.conf.urls.static import static
    from .views import HomeView


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', HomeView.as_view(), name="home"),
        
    ]

    if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

## Migraciones:

    python manage.py migrate

## Carpetas:
 crear templates :agregar base y iondex html
 Crear  static y media

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗

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
        path('', aboutView.as_view(), name="home"),

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

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 

# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [Usuario] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# Usuario:
Para crear un usuario simple:

    python createsuperuser

si queremos un super usuario personalizado
instalamos el Django-allauth

luego:

## core/settings.py:

    AUTHENTICATION_BACKENDS = [
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    ]


    SITE_ID = 1

*INSTALLED_APPS*

    'django.contrib.sites',
    'allauth','allauth.account',
    'allauth.socialaccount',

## core/urls.py:

    path('accounts/', include('allauth.urls')),

## Migrar:

    python manage.py migrate

despues de esto podemos configurar 
al usuario dentro de una aplicacion
por ejemplo en bitacora...
jajaja...

Y para eso nos vamos a los modelos


# ⌘⥏¤∵∴┊⊰⫷⋑_》╣≜ 〔 [Configurar] 〕≜╠《_⋐⫸⊱┊∴∵¤⥑⌘

# Configurar:
solo importamos esto

## bitacora/models.py:

    from django.contrib.auth.models import AbstractUser
creamos esta clase

    class User(AbstractUser):
        pass

        def __str__(self):
            return self.username


## core\settings.py:
final

    AUTH_USER_MODEL = 'bitacora.User'

migraciones:
deberiamos de borrar la migracion en posts y tambien la base de datos crear

nota me salia unmensajito para rellenar un valor inexisten o algo asi pero despues no xd

    python manage.py makemigrations bitacora
migrar

    python manage.py migrate

crear el super user:

    python manage.py createsuperuser

qwerty852as46df79

## bitacora\admin.py:

    from .models import User

    admin.site.register(User)

# ⋖⥐⋗○_⫷█░⫸Δ⋖_⋗》¬﹝⍨﹞⌐《⋖_⋗Δ⫷░█⫸_○⋖⥐⋗ 