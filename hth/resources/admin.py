from django.contrib import admin

from .models import EntrySet, Entry, EntrySetRelationship

# Register your models here.
admin.site.register(EntrySet)
admin.site.register(Entry)
admin.site.register(EntrySetRelationship)
