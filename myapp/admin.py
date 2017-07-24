# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post ,Box,Profile
# Register your models here.

#admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Post._meta.fields]
admin.site.register(Post,PostAdmin)

class BoxAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Box._meta.fields]
	list_editable=("temp","humi")
admin.site.register(Box,BoxAdmin)

class ProgramAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Profile._meta.fields]
admin.site.register(Profile,ProgramAdmin)
	