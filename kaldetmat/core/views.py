from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from . import functions

# Create your views here.


@require_http_methods(['GET', ])
def index(request):

    return render(request, 'core/index.html')


@require_http_methods(['GET', 'POST', ])
def calculate(request, result=[]):

    if request.method == "POST":

        data = request.POST
        result = functions.find_determinant(data)

        if len(result) == 0:
            return HttpResponseBadRequest()

        return redirect("calculate", result=result)

    elif request.method == "GET":

        return render(request, 'core/calculate.html', {
            'result': result
        })
