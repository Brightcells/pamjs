# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClassifyInfo'
        db.create_table(u'pam_classifyinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('update_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('classify', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pam', ['ClassifyInfo'])

        # Adding model 'PictureInfo'
        db.create_table(u'pam_pictureinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('update_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('md5', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('classify', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='pic_classify', null=True, to=orm['pam.ClassifyInfo'])),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'pam', ['PictureInfo'])

        # Adding model 'CacheInfo'
        db.create_table(u'pam_cacheinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('create_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('update_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('http_response', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cache_at', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ip_addr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'pam', ['CacheInfo'])


    def backwards(self, orm):
        # Deleting model 'ClassifyInfo'
        db.delete_table(u'pam_classifyinfo')

        # Deleting model 'PictureInfo'
        db.delete_table(u'pam_pictureinfo')

        # Deleting model 'CacheInfo'
        db.delete_table(u'pam_cacheinfo')


    models = {
        u'pam.cacheinfo': {
            'Meta': {'object_name': 'CacheInfo'},
            'cache_at': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'http_response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_addr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'update_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'pam.classifyinfo': {
            'Meta': {'object_name': 'ClassifyInfo'},
            'classify': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'update_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'pam.pictureinfo': {
            'Meta': {'object_name': 'PictureInfo'},
            'classify': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pic_classify'", 'null': 'True', 'to': u"orm['pam.ClassifyInfo']"}),
            'create_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'md5': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'update_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pam']