from django.http import HttpResponse


def basic_hello(request):
    return HttpResponse('Hello, you!')
