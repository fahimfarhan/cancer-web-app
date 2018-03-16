from django.contrib import admin

# Register your models here.
from patientbasicinfo.models import Identity, Comorbidity

admin.site.register(Identity)
# admin.site.register(Medicine)
# admin.site.register(Dose)
# admin.site.register(Timetable)
# admin.site.register(Bangla)
#admin.site.register(Profile)
admin.site.register(Comorbidity)