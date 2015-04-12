from django.contrib import admin

from .models import Category, CategoryAbstractLanguage, Entry, EntryAbstractLanguage, EntryDescriptionLanguage, EntryPhone

# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryAbstractLanguage)
admin.site.register(Entry)
admin.site.register(EntryAbstractLanguage)
admin.site.register(EntryDescriptionLanguage)
admin.site.register(EntryPhone)
