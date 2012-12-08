# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from sizetemplatemap.models import CreativeSize
from sizetemplatemap.models import CreativeTemplate

def index(request):
    creative_size_list = CreativeSize.objects.order_by('name')
    context = {'creative_size_list': creative_size_list}
    return render(request, 'sizetemplatemap/index.html', context)

def detail(request, creative_size_id):
    creative_size = get_object_or_404(CreativeSize, pk=creative_size_id)
    #creative_templates = creative_size.CreativeSizeTemplateRel_set.all()

    return render(request, 'sizetemplatemap/detail.html', {'creative_size_obj': creative_size})

def custom_404(request):
    return render(request, 'sizetemplatemap/404.html')
