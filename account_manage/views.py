#coding:utf8
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
import logging,traceback, pprint
import codecs

# app specific files

from models import *
from forms import *
from system_avalibe.models import * 



def create_account(request):
    if not check_permission(request):
        return HttpResponseRedirect('/error/')
    form = accountForm(request.POST or None)
    
    if request.method=='POST':     
        if form.is_valid():
            cd=form.cleaned_data
            my_usr=my_user.objects.get(login_name=request.session['login_name'] or None)
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
                company=my_usr.company,
            )
            i_account.save()
        return HttpResponseRedirect('account_manage/account/list/')

    t = get_template('account_manage/create_account.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_account(request):

    if not check_permission(request):
        return HttpResponseRedirect('/error/')
    my_usr=my_user.objects.get(login_name=request.session['login_name'] or None)
    if (request.method=='GET'):
        list_items = account.objects.filter(user_id=my_usr,is_paid=0)

        paginator = Paginator(list_items ,10)
         
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            list_items = paginator.page(page)
        except :
            list_items = paginator.page(paginator.num_pages)
        
        return render_to_response('account_manage/list_account.html',locals(),context_instance=RequestContext(request))
    elif (request.method=="POST"):
        beg_date=None
        end_date=None
        try:
            beg_date=request.POST['beg_date']           
            end_date=request.POST['end_date']
            
        except:        
            stack = pprint.pformat(traceback.extract_stack())
            logging.error('An error occurred: %s' % stack)          
            list_items =account.objects.filter(user_id=my_usr)
        if beg_date:
            beg_date=beg_date.encode("utf-8")
            beg_date=time.strptime(beg_date,"%m/%d/%Y")
            beg_date=time.strftime('%Y-%m-%d',beg_date)
        if end_date:
            end_date=end_date.encode("utf-8")
            end_date=time.strptime(end_date,"%m/%d/%Y")
            end_date=time.strftime('%Y-%m-%d',end_date)
        

        if (beg_date and end_date):
            list_items=account.objects.filter(user_id=my_usr,modify_date__lte=end_date,modify_date__gte=beg_date)
        elif beg_date:
            list_items=account.objects.filter(user_id=my_usr,modify_date__gte=beg_date)
        elif end_date:
            list_items=account.objects.filter(user_id=my_usr,modify_date__lte=end_date)
        else:
            list_items =account.objects.filter(user_id=my_usr)
        
        paginator = Paginator(list_items ,10)
        
        
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            list_items = paginator.page(page)
        except :
            list_items = paginator.page(paginator.num_pages)
        
        return render_to_response('account_manage/list_account.html',locals(),context_instance=RequestContext(request))        



def view_account(request, id):
    if not check_permission_by_grade(request,1):
        return HttpResponseRedirect('/error/')
    if request.method=='GET':
        account_instance = account.objects.get(id = id)
        return render_to_response('account_manage/view_account.html',locals(),context_instance=RequestContext(request))    
   
def check_account(request, id):
    if not check_permission_by_grade(request,1):
        return HttpResponseRedirect('/error/')
    my_usr=my_user.objects.get(login_name=request.session['login_name'] or None)
    if (my_usr):
        account_instance = account.objects.get(id = id)
        account_instance.status=2
        account_instance.approver=my_usr
        account_instance.save()

    return HttpResponseRedirect('account_manage/account/check_account')


def edit_account(request, id):
    if not check_permission(request):
        return HttpResponseRedirect('/error/')
    account_instance = account.objects.get(id=id)

    form = accountForm(request.POST or None, instance = account_instance)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('account_manage/account/list')
    
    return render_to_response('account_manage/edit_account.html',locals(),context_instance=RequestContext(request))

def list_pay_account(request):
    if not check_permission_by_depid(request,2):
        return HttpResponseRedirect('/error/')
    pay_flag=True
    my_usr=my_user.objects.get(login_name=request.session['login_name'] or None)
    if (request.method=='GET'):
       
        list_items = account.objects.filter(status=2,is_paid=0,company=my_usr.company)
        paginator = Paginator(list_items ,10)
        
        
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            list_items = paginator.page(page)
        except :
            list_items = paginator.page(paginator.num_pages)
        
        return render_to_response('account_manage/pay_account.html',locals(),context_instance=RequestContext(request))
    elif (request.method=='POST'):
        if (request.POST.has_key("pay")):
            pay_flag=True
            cb_list=request.POST.getlist('cb_field')
            for u_id in cb_list:
                account_instance=account.objects.get(id=u_id)
                account_instance.is_paid=1
                account_instance.pay_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
                account_instance.save()
            return render_to_response('account_manage/pay_account.html',locals(),context_instance=RequestContext(request))
        elif (request.POST.has_key("showall")):
            list_items = account.objects.filter(status=2,company=my_usr.company)
            paginator = Paginator(list_items ,10)
            pay_flag=False
            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            try:
                list_items = paginator.page(page)
            except :
                list_items = paginator.page(paginator.num_pages)
            
            return render_to_response('account_manage/pay_account.html',locals(),context_instance=RequestContext(request))

def delete_account(request, id):
    if not check_permission(request):
        return HttpResponseRedirect('/error/')
    account_instance= account.objects.get(id=id)
    account_instance.delete()
    return HttpResponseRedirect('account_manage/account/list')

def list_check_account(request):

    if not check_permission_by_grade(request,1):
        return HttpResponseRedirect('/error/')
    my_usr=my_user.objects.get(login_name=request.session['login_name'] or None)
    if (request.method=='GET'):
        if (my_usr.position.position_grade==1): #总监
            list_items = account.objects.filter(department=my_usr.department,is_paid=0,status=0,company=my_usr.company)
        elif (my_usr.position.position_grade==2):#总经理
            list_items = account.objects.filter(is_paid=0,company=my_usr.company)   
        paginator = Paginator(list_items ,10)

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            list_items = paginator.page(page)
        except :
            list_items = paginator.page(paginator.num_pages)
        
        return render_to_response('account_manage/check_account.html',locals(),context_instance=RequestContext(request))
    elif (request.method=="POST"):
        beg_date=None
        end_date=None
        try:
            beg_date=request.POST['beg_date']           
            end_date=request.POST['end_date']
            
        except:        
            stack = pprint.pformat(traceback.extract_stack())
            logging.error('An error occurred: %s' % stack)          
            list_items =account.objects.filter(user_id=my_usr)
        if beg_date:
            beg_date=beg_date.encode("utf-8")
            beg_date=time.strptime(beg_date,"%m/%d/%Y")
            beg_date=time.strftime('%Y-%m-%d',beg_date)
        if end_date:
            end_date=end_date.encode("utf-8")
            end_date=time.strptime(end_date,"%m/%d/%Y")
            end_date=time.strftime('%Y-%m-%d',end_date)
        
        if my_usr.position.position_grade==1:
            if (beg_date and end_date):
                list_items=account.objects.filter(department=my_usr.department,modify_date__lte=end_date,modify_date__gte=beg_date,company=my_usr.company)
            elif beg_date:
                list_items=account.objects.filter(department=my_usr.department,modify_date__gte=beg_date,company=my_usr.company)
            elif end_date:
                list_items=account.objects.filter(department=my_usr.department,modify_date__lte=end_date,company=my_usr.company)
            else:
                list_items =account.objects.filter(department=my_usr.department,company=my_usr.company)
        elif my_usr.position.position_grade==2:
            if (beg_date and end_date):
                list_items=account.objects.filter(modify_date__lte=end_date,modify_date__gte=beg_date,company=my_usr.company)
            elif beg_date:
                list_items=account.objects.filter(modify_date__gte=beg_date,company=my_usr.company)
            elif end_date:
                list_items=account.objects.filter(modify_date__lte=end_date,company=my_usr.company)
            else:
                list_items =account.objects.filter(company=my_usr.company)
        
        paginator = Paginator(list_items ,10)
        
        
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            list_items = paginator.page(page)
        except :
            list_items = paginator.page(paginator.num_pages)
        
        return render_to_response('account_manage/check_account.html',locals(),context_instance=RequestContext(request))

def check_permission(request):
    login=request.session.get('login_name',None)
    if not login:
        return False
    return True

def check_permission_by_depid(request,depid):
    login=request.session.get('login_name',None)
    if not login:
        return False
    else:
        my_usr=my_user.objects.get(login_name=request.session['login_name'] or None)
        if my_usr.department.id!=depid:
            return False
        else:
            return True

def check_permission_by_grade(request,grade):
    login=request.session.get('login_name',None)
    if not login:
        return False
    else:
        my_usr=my_user.objects.get(login_name=request.session['login_name'] or None)
        logging.error(my_usr.position.position_grade)
        if str(my_usr.position.position_grade)<=grade:
            return False
        else:
            return True

