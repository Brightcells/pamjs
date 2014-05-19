#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.forms.widgets import Textarea, ClearableFileInput, URLInput, Select
from django.utils.translation import ugettext_lazy as _

from pam.models import ClassifyInfo, PictureInfo

import hashlib


class ClassifyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.classify


class PictureInfoModelForm(ModelForm):
    image = forms.ImageField(
        widget=ClearableFileInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': _('image')}),
        required=False
    )

    url = forms.URLField(
        widget=URLInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': _('url')}),
        required=False
    )

    info = forms.CharField(
        widget=Textarea(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': _('info')}),
        required=False
    )

    link = forms.URLField(
        widget=URLInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': _('link')}),
        required=False
    )

    md5 = forms.CharField(
        required=False
    )

    classify = ClassifyModelChoiceField(
        queryset=ClassifyInfo.objects.filter(status=True),
        widget=Select(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': _('classify')}),
        required=False
    )

    class Meta:
        model = PictureInfo
        exclude = ('status', 'priority')

    def clean(self):
        image = self.cleaned_data['image']
        url = self.cleaned_data['url']
        if not image and url == u'':
            raise forms.ValidationError(_('Must uploda an image or input an image\'s url'))
        else:
            image_md5 = hashlib.md5(image.read()).hexdigest()
            if PictureInfo.objects.filter(md5=image_md5).exists():
                raise forms.ValidationError(_('This image has already exists'))
            else:
                self.cleaned_data['md5'] = image_md5
                return self.cleaned_data