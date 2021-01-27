from django.contrib import admin

from .models import Work, TypeWork, Initiator, Employee, Researched_objects, Rank, Position, Subdivision, Type_Objects

class WorkAdmin(admin.ModelAdmin):
    list_display = ('number', 'serial_number', 'receipt_date', 'initiator')


admin.site.register(Work, WorkAdmin)
admin.site.register(TypeWork)
admin.site.register(Initiator)
admin.site.register(Employee)
admin.site.register(Researched_objects)
admin.site.register(Rank)
admin.site.register(Position)
admin.site.register(Subdivision)
admin.site.register(Type_Objects)
