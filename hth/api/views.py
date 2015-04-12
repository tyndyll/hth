from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render

from resources.models import Entry, Category, CategoryAbstractLanguage, EntryAbstractLanguage, \
                                EntryDescriptionLanguage, EntryPhone

# Create your views here.
def get_entries(request):
    category = get_object_or_404(Category, name=request.GET['category'])
    results = []
    for entry in Entry.objects.filter(category=category):
        obj = {
                "title": entry.title,
                "abstract": {
                    "gb": entry.abstract
                    },
                "description": {
                    "gb": entry.description
                    },
                "address": entry.address,
                "opening": entry.opening,
                "phone": []
            }
        for language in EntryAbstractLanguage.objects.filter(entry=entry):
            obj["abstract"][language.language] = language.abstract
        for language in EntryDescriptionLanguage.objects.filter(entry=entry):
            obj["description"][language.language] = language.description
        for phone in EntryPhone.objects.filter(entry=entry):
            obj["phone"].append({
                    "number": phone.number,
                    "available": phone.available
                    })
        results.append(obj)
    return JsonResponse(results, safe=False)

def get_categories(request):
    results = []
    for category in Category.objects.all().order_by('name'):
        obj = {
                "name": category.name,
                "abstract": {
                        "gb": category.abstract
                    },
                "background_image": category.background_image,
                "fa_class": category.fa_class,
            }
        for language in CategoryAbstractLanguage.objects.filter(category=category):
            obj["abstract"][language.language] = language.abstract
        results.append(obj)
    return JsonResponse(results, safe=False)
