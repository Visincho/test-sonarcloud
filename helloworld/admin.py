from django.contrib import admin

# Register your models here.
from helloworld.models import Hello

admin.site.register(Hello, admin.ModelAdmin)