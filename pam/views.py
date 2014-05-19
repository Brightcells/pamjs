#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render

from pam.form import PictureInfoModelForm
from pam.models import PictureInfo


def home(request):
    return render(request, 'pam/index.html')


def pic(request):
    form = PictureInfoModelForm()
    pic_list = PictureInfo.objects.filter(status=True)[:6]
    pic_list = [pic.data for pic in pic_list]

    if request.method == "POST":
        form = PictureInfoModelForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.status = True
            f.save()
            form = PictureInfoModelForm()

    return render(request, 'pam/p.html', dict(form=form, pics=pic_list))


def aud(request):
    return render(request, 'pam/a.html')


def mov(request):
    return render(request, 'pam/m.html')