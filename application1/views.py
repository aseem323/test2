from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def testfn(request):
    # print('helooo worl')
    return HttpResponse('hello baabtra')


def test2fn(request):
    return render(request,'new.html')    
