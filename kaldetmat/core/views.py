from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .functions import *

# Create your views here.


@require_http_methods(['GET', ])
def index(request):

    return render(request, 'core/index.html')


@require_http_methods(['POST', ])
def calculate(request):

    pass
