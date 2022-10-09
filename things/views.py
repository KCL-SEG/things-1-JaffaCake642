from django.shortcuts import render

def things(request):
    return render(request,'things.html')