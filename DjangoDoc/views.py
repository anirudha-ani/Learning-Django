from django.http import HttpResponse

def root(request):
    return HttpResponse("This is the landing page")