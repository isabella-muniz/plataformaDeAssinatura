from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

async def home(request: HttpRequest) -> HttpResponse:
    """..."""
    #return HttpResponse("Estamos na home da app de account")
    return render(request, 'account/home.html', {'x': 33})
#:

async def register(request: HttpRequest) -> HttpResponse:
    """..."""
    #return HttpResponse("Estamos no register da app de account")
    return render(request, 'account/register.html')

#:

async def login(request: HttpRequest) -> HttpResponse:
    """..."""
    #return HttpResponse("Estamos no login da app de account")
    return render(request, 'account/login.html')

#:

