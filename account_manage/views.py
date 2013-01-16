
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


def create_account(request):
    form = accountForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = accountForm()

    t = get_template('account_manage/create_account.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_account(request):
  
    list_items = account.objects.all()
    department=account.department
    paginator = Paginator(list_items ,10)
    

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('account_manage/list_account.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_account(request, id):
    account_instance = account.objects.get(id = id)

    t=get_template('account_manage/view_account.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_account(request, id):

    account_instance = account.objects.get(id=id)

    form = accountForm(request.POST or None, instance = account_instance)

    if form.is_valid():
        form.save()

    t=get_template('account_manage/edit_account.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
