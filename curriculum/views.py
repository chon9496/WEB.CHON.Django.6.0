from django.shortcuts import render
# Create your views here.
from django.views.generic import View

class CurriView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'curriculum/curriculum.html', context)