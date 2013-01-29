
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

# app specific files

from models import *
from forms import *


def create_warehouse(request):
    form = warehouseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = warehouseForm()

    t = get_template('warehouse/create_warehouse.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_warehouse(request):
  
    list_items = warehouse.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('warehouse/list_warehouse.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_warehouse(request, id):
    warehouse_instance = warehouse.objects.get(id = id)

    t=get_template('warehouse/view_warehouse.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_warehouse(request, id):

    warehouse_instance = warehouse.objects.get(id=id)

    form = warehouseForm(request.POST or None, instance = warehouse_instance)

    if form.is_valid():
        form.save()

    t=get_template('warehouse/edit_warehouse.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
