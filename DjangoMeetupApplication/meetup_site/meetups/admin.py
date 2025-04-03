from django.contrib import admin

from .models import Meetup, Location, Participant


# Register your models here.
class MeetupAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
    ]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["title", "date", "location"]


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
