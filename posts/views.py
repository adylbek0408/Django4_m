from django.shortcuts import HttpResponse

# Create your views here.

def main(request):
    if request.method == 'GET':
        return HttpResponse('Hello! its my project')

def main1(request):
    if request.method == 'GET':
        return HttpResponse('13.01.2023')

def main2(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')