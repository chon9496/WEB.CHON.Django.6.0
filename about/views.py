from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.views.generic import View


class aboutView(View):
    def get(self,request, *args, **kwargs):
        context={

        }
        return render(request,'about/about.html', context)