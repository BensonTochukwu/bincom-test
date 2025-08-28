from django.contrib import admin
from .models import State, LGA, Ward, PollingUnit, AnnouncedPUResults, AnnouncedLGAResults

admin.site.register(State)
admin.site.register(LGA)
admin.site.register(Ward)
admin.site.register(PollingUnit)
admin.site.register(AnnouncedPUResults)
admin.site.register(AnnouncedLGAResults)
