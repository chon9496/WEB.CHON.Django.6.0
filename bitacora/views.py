from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.generic import View


class bitacoraView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'bitacora/bitacora.html', context)
    
    
