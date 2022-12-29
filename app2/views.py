from django.shortcuts import render

# Create your views here.
def user(request):
    d={'name':'yammy'}
    return render(request,'user.html',d)
