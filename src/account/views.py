from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from asgiref.sync import sync_to_async, async_to_sync

# Create your views here.
from .forms import CustomUserCreationForm
from .models import CustomUser

async def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/home.html')
#:

async def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if await form.ais_valid():
            await form.asave()
            return HttpResponse('Utilizador registrado')
    else:
        form = CustomUserCreationForm()

    context = {'register_form': form}
    return render(request, 'account/register.html', context)
#:

async def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/login.html')

#:

