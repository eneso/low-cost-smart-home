from datetime import datetime

from django.http.response import JsonResponse
from django.http.response import Http404
from django.http import HttpRequest
from django.shortcuts import render

from mainpi.models import Peripheral, SubordinatePi

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    peripherals = Peripheral.objects.all()
    subordinates = SubordinatePi.objects.all()

    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'peripherals': peripherals,
            'subordinates': subordinates
        }
    )


def toggle_light(request):
    assert isinstance(request, HttpRequest)

    response_data = {}
    response_data['is_success'] = False

    if request.method == 'GET':
        raise Http404('Page not found')
    else:
        light_id = request.POST['light_id']
        check = bool(request.POST['checked'])
        print('Received request with id={} and checked value={}'.format(light_id, check))
        #Here we check for light id and checked value. Foward request to child node if needed
        response_data['is_success'] = True
        return JsonResponse(response_data)
    