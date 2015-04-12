from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, render

from resources.models import Entry, EntrySet

# Create your views here.
def get_entries(request):
    entry_set = get_object_or_404(EntrySet, name='shelter')
    return HttpResponse(serializers.serialize('json', Entry.objects.filter(entry_set=entry_set)))
