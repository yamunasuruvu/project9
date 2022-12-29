from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'yamuna'}
    return render(request,'jinja_print.html',d)
