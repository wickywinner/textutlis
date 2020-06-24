# I have created this file-Wicky
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,"home.html",{'name':'wicky winner'})
def add(request):
    val1 = float(request.POST['num1'])
    val2 = float(request.POST['num2'])
    res= val1 + val2
    return render(request,"result.html",{'result':res})    
  