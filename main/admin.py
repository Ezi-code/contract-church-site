from django.contrib import admin
from .models import *

class AdminAnnoucements(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    ordering = ["-date"]


class AdminEvents(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    ordering = ["-date"]

class AdminSermons(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    ordering = ["-date"]

class AdminPrayerRequests(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    ordering = ["-date"]

class AdminVideoSermons(admin.ModelAdmin):
    list_display = ["preacher"]
    search_fields = ["preacher"]
    ordering = ["-date"]

class AdminAudioSermons(admin.ModelAdmin):
    list_display = ["preacher"]
    search_fields = ["preacher"]
    ordering = ["-date"]


class AdminNewsLetterSubscription(admin.ModelAdmin):
    list_display = ["email"]
    search_fields = ["email"]
    ordering = ["-date"]

class AdminContact(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]
    search_fields = ["name", "email", "subject"]
    ordering = ["-date"]


admin.site.register(Announcement, AdminAnnoucements)
admin.site.register(Event, AdminEvents)
admin.site.register(Sermon, AdminSermons)
admin.site.register(PrayerRequest, AdminPrayerRequests)
admin.site.register(VideoSermon, AdminVideoSermons)
admin.site.register(AudioSermon, AdminAudioSermons)
admin.site.register(NewsLetterSubscription, AdminNewsLetterSubscription)
admin.site.register(Contact, AdminContact)
# Compare this snippet from main/views.py: