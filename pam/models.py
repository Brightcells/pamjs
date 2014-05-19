#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from pamjs.basemodels import CreateUpdateMixin
from django.utils.translation import ugettext_lazy as _, ugettext

import os
import time
import datetime


def upload_path(instance, old_filename):
    extension = os.path.splitext(old_filename)[1].lower()
    today = datetime.datetime.today()
    timestamp = str(time.time())
    file_path = 'pamjs/image/{year}{month}/{timestamp}{extension}'.format(
        year=today.year,
        month=today.month,
        timestamp=timestamp,
        extension=extension)
    return file_path


class ClassifyInfo(CreateUpdateMixin):
    classify = models.CharField(_('classify'), max_length=255, blank=True, null=True, help_text=u'资源分类')
    status = models.BooleanField(_('status'), default=True, help_text=u'分类是否显示')
    priority = models.IntegerField(_('priority'), blank=True, null=True, help_text=u'分类展示的优先级')

    class Meta:
        verbose_name = _('classifyinfo')
        verbose_name_plural = _('classifyinfo')

    def __unicode__(self):
        return u'{0.classify}'.format(self)


class PictureInfo(CreateUpdateMixin):
    image = models.ImageField(_('image'), upload_to=upload_path, blank=True, null=True, help_text=u'图片上传')
    url = models.URLField(_('url'), blank=True, null=True, help_text=u'图片链接')
    info = models.TextField(_('info'), blank=True, null=True, help_text=u'图片描述信息')
    link = models.URLField(_('link'), blank=True, null=True, help_text=u'图片查看详情链接')
    md5 = models.CharField(_('md5'), max_length=255, blank=True, null=True, help_text=u'图片 hash 值')
    classify = models.ForeignKey('ClassifyInfo', related_name='pic_classify', blank=True, null=True, help_text=u'图片所属分类')
    status = models.BooleanField(_('status'), default=True, help_text=u'图片是否显示')
    priority = models.IntegerField(_('priority'), blank=True, null=True, help_text=u'图片展示的优先级')

    class Meta:
        verbose_name = _('pictureinfo')
        verbose_name_plural = _('pictureinfo')

    def __unicode__(self):
        return u'{0.md5}'.format(self)

    def _data(self):
        return {
            'pk': self.pk,
            'image': settings.DOMAIN + self.image.url if self.image else self.url,
            'info': self.info,
            'link': self.link
        }

    data = property(_data)


class CacheInfo(CreateUpdateMixin):
    http_response = models.TextField(_('http_response'), blank=True, null=True, help_text=u'缓存的 HttpResponse')
    cache_at = models.CharField(_('cache_at'), max_length=255, blank=True, null=True, help_text=u'缓存时间，精确到年月日')
    ip_addr = models.CharField(_('ip_addr'), max_length=255, blank=True, null=True, help_text=u'缓存 IP')

    class Meta:
        verbose_name = _('cacheinfo')
        verbose_name_plural = _('cacheinfo')

    def __unicode__(self):
        return u'{0.ip_addr}-{0.cache_at}'.format(self)