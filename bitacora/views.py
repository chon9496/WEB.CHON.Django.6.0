from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.generic import View


class bitacoraView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'bitacora/bitacora.html', context)
    
    
class webView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'descarcga/bitacora/web.html', context)
class  desktopView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'descarcga/bitacora/desktop.html', context)
class otroView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'descarcga/bitacora/otro.html', context)