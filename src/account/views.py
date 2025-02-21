from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
from .forms import CustomUserCreationForm
from .models import CustomUser

async def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/home.html')
#:

async def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Utilizador registrado')
    else:
        form = CustomUserCreationForm()

    context = {'register_form': form}
    return render(request, 'account/register.html', context)
#:

async def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'account/login.html')

#:

