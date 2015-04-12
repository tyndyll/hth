from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render

from resources.models import Entry, Category, CategoryAbstractLanguage

# Create your views here.
def get_entries(request):
    category = get_object_or_404(Category, name=request.GET['category'])
    return HttpResponse(serializers.serialize('json', Entry.objects.filter(category=category)))

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
