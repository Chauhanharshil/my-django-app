from django.shortcuts import render

# Create your views here.
def index(request):
    print('here')
    context={
        }
    return render(request,'tutorialindex.html',context)