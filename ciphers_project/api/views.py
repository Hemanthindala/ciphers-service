from django.shortcuts import render
from django.http import JsonResponse
from .ciphers import ceaser_encode

# Create your views here.
def greetings(request):
    result = {"message": "Welcome to ciphers service!"}
    return JsonResponse(result)


def encode(request, plain_text, shift):
    parameters = dict(request.GET)
    print(parameters)
    cipher = ceaser_encode(plain_text, shift)
    return JsonResponse({"cipher": cipher})



