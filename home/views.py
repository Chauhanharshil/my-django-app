from django.shortcuts import render
from .models import Harsh
# Create your views here.
def index(request):
    data = Harsh.objects.all()
    context={
        'datas':data
        }
    return render(request,'homeindex.html',context)