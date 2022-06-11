from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def main(request):
    print(request.body)
    
    return JsonResponse({'message':"query successful"})