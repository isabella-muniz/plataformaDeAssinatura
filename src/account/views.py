from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

async def home(request: HttpRequest) -> HttpResponse:
    """..."""
    return HttpResponse("Estamos na home da app de account")
#:

async def register(request: HttpRequest) -> HttpResponse:
    """..."""
    return HttpResponse("Estamos no register da app de account")
#:

async def login(request: HttpRequest) -> HttpResponse:
    """..."""
    return HttpResponse("Estamos no login da app de account")
#:

