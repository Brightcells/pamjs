#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


class CreateUpdateMixin(models.Model):
    create_at = models.DateTimeField(_('create_at'), blank=True, null=True, auto_now_add=True, help_text=u'创建时间')
    update_at = models.DateTimeField(_('update_at'), blank=True, null=True, auto_now=True, help_text=u'更新时间')

    class Meta:
        abstract = True
