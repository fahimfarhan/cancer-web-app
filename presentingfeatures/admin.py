from django.contrib import admin

# Register your models here.
from presentingfeatures.models import Status, Investigation

admin.site.register(Status)
admin.site.register(Investigation)