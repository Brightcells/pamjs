from django.contrib import admin
from pam.models import ClassifyInfo, PictureInfo, CacheInfo


class ClassifyInfoAdmin(admin.ModelAdmin):
    list_display = ('classify', 'abbr', 'status', 'priority')


class PictureInfoAdmin(admin.ModelAdmin):
    list_display = ('image', 'url', 'info', 'link', 'md5', 'device', 'classify', 'status', 'priority')


class CacheInfoAdmin(admin.ModelAdmin):
    list_display = ('http_response', 'cache_at', 'ip_addr')


admin.site.register(ClassifyInfo, ClassifyInfoAdmin)
admin.site.register(PictureInfo, PictureInfoAdmin)
admin.site.register(CacheInfo, CacheInfoAdmin)