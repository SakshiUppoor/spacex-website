from django.contrib import admin
from .models import *

# Register your models here.

class LaunchesAdmin(admin.ModelAdmin):
    list_display = ('flight_number' , 'rocket_name')

class MissionAdmin(admin.ModelAdmin):
    list_display = ('mission_id' , 'mission_name')

class CoreAdmin(admin.ModelAdmin):
    list_display = ('core_serial' , 'mission_name')

class RocketAdmin(admin.ModelAdmin):
    list_display = ('rocket_number' , 'rocket_name')


admin.site.register(Launches, LaunchesAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Core, CoreAdmin)
admin.site.register(Rocket, RocketAdmin)