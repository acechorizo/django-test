# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from sizetemplatemap.models import CreativeSize
from sizetemplatemap.models import CreativeTemplate

def index(request):
    creative_size_list = CreativeSize.objects.order_by('name')
    context = {'creative_size_list': creative_size_list}
    return render(request, 'sizetemplatemap/index.html', context)

def detail(request, creative_size_id):
    creative_size = get_object_or_404(CreativeSize, pk=creative_size_id)
    return render(request, 'sizetemplatemap/detail.html', {'creative_size_obj': creative_size})

def custom_404(request):
    return render(request, 'sizetemplatemap/404.html')

  
def creative_size_edit(request, creative_size_id):
    cs = get_object_or_404(CreativeSize, pk=creative_size_id)
    try:
        selected_creative_size = cs.get(pk=request.POST['creative_size_id'])
    except (KeyError, CreativeTemplate.DoesNotExist):
        # Redisplay the creative size edit form.
        return render(request, 'sizetemplatemap/detail.html', {
            'creative_size_obj': cs,
            'error_message': "You didn't select a template.",
        })
    else:
        selected_creative_size.name = request.POST['cs_name'] 
        selected_creative_size.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('sizetemplatemap:results', args=(cs.id,)))    
