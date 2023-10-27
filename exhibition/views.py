from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("이 부분은 없애주시면 되요!")


