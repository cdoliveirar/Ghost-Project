from django.contrib import admin

# Register your models here.
from .models import Topic, Note

class TopicAdmin(admin.ModelAdmin):
    fields = ['topic']

class NoteAdmin(admin.ModelAdmin):
    fields = ['text','pup_date']

admin.site.register(Topic)
admin.site.register(Note)

