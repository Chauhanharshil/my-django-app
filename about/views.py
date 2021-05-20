from django.shortcuts import render
from .models import photos
# Create your views here.
 

# Create your views here.
def index(request):
    photo = photos.objects.all()
    context={'photos':photo
        }
    return render(request,'aboutindex.html',context)