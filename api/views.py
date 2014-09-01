from django.shortcuts import render, HttpResponse

from pam.models import PictureInfo, CacheInfo

import json
import random
from datetime import datetime


def get_pic_httpresponse(callback, num, device, classify):
    pic_queryset = PictureInfo.objects.filter(status=True, device=device)
    if classify != '':
        pic_queryset = pic_queryset.filter(classify__abbr=classify)
    else:
        pass
    pic_queryset = random.sample(pic_queryset, num) if pic_queryset.count() > num else pic_queryset
    pic_list = [pic.data for pic in pic_queryset]
    return callback + '([' + str(json.dumps(pic_list)) + '])'


def pic(request):
    site = request.GET.get('site', '')
    usr = request.GET.get('usr', '')
    num = int(request.GET.get('num', '5'))
    callback = request.GET.get('callback', '')
    cache = request.GET.get('cache', 'true')
    device = request.GET.get('device', 'C')
    classify = request.GET.get('classify', '')

    if cache == 'true':
        ip_addr = request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']
        cache_at = datetime.today().strftime('%Y-%m-%d')
        hr, created = CacheInfo.objects.get_or_create(
            site=site,
            usr=usr,
            ip_addr=ip_addr,
            cache_at=cache_at,
            defaults={'http_response': get_pic_httpresponse(callback, num, device, classify)}
        )
        httpresponse = hr.http_response
    else:
        httpresponse = get_pic_httpresponse(callback, num, device, classify)

    return HttpResponse(httpresponse)