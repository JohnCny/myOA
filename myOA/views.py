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
        except my_user.DoesNotExist:
            return render_to_response('login.html',{'notExist':True},context_instance=RequestContext(request))

        if myUser is not None:
            request.session['login_name']=myUser.login_name
            request.session['real_name']=myUser.real_name
            request.session['position_grade']=myUser.position.position_grade
            request.session['department_id']=myUser.department_id
            return HttpResponseRedirect('/account_manage/account/list')
    if request.method == 'GET':
        login_flag=True
        return render_to_response('login.html',locals(),context_instance=RequestContext(request))

def logout(request):
    try:
        del request.session['login_name']
    except KeyError:
        pass
    return HttpResponseRedirect("/login/")

def error(request):
    return render_to_response('error.html',{},context_instance=RequestContext(request))
