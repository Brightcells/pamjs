from django.shortcuts import render, HttpResponse

from pam.models import PictureInfo, CacheInfo

import json
import random
from datetime import datetime


def get_pic_httpresponse(callback, num):
    pic_queryset = PictureInfo.objects.filter(status=True)
    pic_queryset = random.sample(pic_queryset, num) if pic_queryset.count() > num else pic_queryset
    pic_list = [pic.data for pic in pic_queryset]
    return callback + '([' + str(json.dumps(pic_list)) + '])'


def pic(request):
    num = int(request.GET.get('num', '5'))
    callback = request.GET.get('callback', '')
    cache = request.GET.get('cache', 'true')

    if cache == 'true':
        ip_addr = request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']
        cache_at = datetime.today().strftime('%Y-%m-%d')
        hr, created = CacheInfo.objects.get_or_create(ip_addr=ip_addr, cache_at=cache_at, defaults={'http_response': get_pic_httpresponse(callback, num)})
        httpresponse = hr.http_response
    else:
        httpresponse = get_pic_httpresponse(callback, num)

    return HttpResponse(httpresponse)