from django.shortcuts import render
from django.http import HttpResponse

def test(request,testid):
    return HttpResponse("lol{}".format(testid))
