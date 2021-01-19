from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
    return HttpResponse("Test-----123")
def fnhome(request):
    return render(request,'index.html')
def fnForm(request):
    return render(request,'form.html')