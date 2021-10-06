
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')    
def mentalhealth(request):
    return render(request, 'mentalhealth.html')
def findnearby(request):
    return render(request, 'findnearby.html')
def miniblogs(request):
    return render(request, 'miniblogs.html')
def organisations(request):
    return render(request, 'organisations.html')
def definitions(request):
    return render(request, 'definitions.html')
def pridesection(request):
    return render(request, 'pridesection.html')