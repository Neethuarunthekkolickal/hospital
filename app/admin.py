from django.contrib import admin
from . models import Hospital, Doctor,Department

class BookingAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','doctor','date','time','problem')

admin.site.register(Hospital,BookingAdmin)
admin.site.register(Doctor)
admin.site.register(Department)