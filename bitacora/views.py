from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post


class bitacoraView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'bitacora/bitacora.html', context)
    
    
class descargar(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'bitacora/descarcga/descarga.html', context)


class noticiasLista(ListView):
    model = Post
class noticiasDetail(DetailView):
    model = Post
class noticiasCreate(CreateView):
    model = Post
class noticiasUpdate(UpdateView):
    model = Post
class noticiasDelete(DeleteView):
    model = Post