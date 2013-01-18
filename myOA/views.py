#coding:utf8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from system_avalibe.models import my_user
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        mlogin_name=request.POST['login_name']
        mlogin_password=request.POST['login_password']
        try:
            myUser = my_user.objects.get(login_name=mlogin_name,login_password=mlogin_password)
        except:
            return render_to_response('login.html',{},context_instance=RequestContext(request))

        if myUser is not None:
            request.session['login_name']=myUser.login_name
            return HttpResponseRedirect('/account_manage/account/list')
    if request.method == 'GET':
        return render_to_response('login.html',{},context_instance=RequestContext(request))

def logout(request):
    try:
        del request.session['login_name']
    except KeyError:
        pass
    return HttpResponseRedirect("/login/")

def error(request):
    return HttpResponseRedirect('/error/')
