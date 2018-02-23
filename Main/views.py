from django.shortcuts import render, HttpResponse

from models import TimePoint, UploadImg
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


def image(request):
    return render(request, 'image.html')


def get_image(request):
    ui = UploadImg.get_path_by_id(1)
    rtu = {
        'id': ui.id,
        'title': ui.title,
        'desc': ui.describe,
        'path': ui.path
    }
    return HttpResponse(json.dumps(rtu))
