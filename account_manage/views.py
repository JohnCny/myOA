
# Create your views here.

from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.db.models import Q
import time
import logging
# app specific files

from models import *
from forms import *
from system_avalibe.models import * 



def create_account(request):
    form = accountForm(request.POST or None)
    if request.method=='POST':     
        if form.is_valid():
            cd=form.cleaned_data
            my_usr=my_user.objects.get(login_name=request.session['login_name'])
            i_account=account(
                user_id=my_usr,
                department=cd['department'],
                type_id=cd['type_id'],
                amount=cd['amount'],
                beg_date=cd['beg_date'],
                modify_date=time.strftime('%Y-%m-%d',time.localtime(time.time())),
                end_date=cd['end_date'],
                status=0,
                approver=my_usr,
                level=0,
                is_paid=0,
            )
            i_account.save()
        return HttpResponseRedirect('account_manage/account/list')

    t = get_template('account_manage/create_account.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_account(request):
    list_items = account.objects.all()
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
        return HttpResponseRedirect('account_manage/account/list')

    t=get_template('account_manage/edit_account.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def check_permission(request):
    if (request.session['login_name'] is None):
        return HttpResponseRedirect('/error/')




