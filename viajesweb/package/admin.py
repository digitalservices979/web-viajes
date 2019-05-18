from django.contrib import admin
from .models import *
# Register your models here.

class InternacionaleAdmin(admin.ModelAdmin):
	readonly_fields = ('created',)

admin.site.register(Nacionale)
admin.site.register(Internacionale, InternacionaleAdmin)