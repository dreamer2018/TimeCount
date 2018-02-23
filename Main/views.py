from django.shortcuts import render, HttpResponse

from models import TimePoint
# Create your views here.
import json


def get_timestamp(request):
    tp = TimePoint.get_timestamp_by_id(1)
    rtu = {
        'id': tp.id,
        'title': tp.title,
        'desc': tp.describe,
        'timestamp': int(tp.timestamp * 1000)
    }
    return HttpResponse(json.dumps(rtu))


def index(request):
    return render(request, 'index.html')
