from django.shortcuts import render,redirect
from foodmanageapp.forms import StudentForm,PersonalDetailsForm,BreakfastAgreementForm,LunchAgreementForm,DinnerAgreementForm,PgMenuForm
from foodmanageapp.models import PgMenu,BreakfastAgreement,LunchAgreement,DinnerAgreement,PersonalDetails
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout
import datetime
from django import forms
# Create your views here.
def home_view(request):
    return render(request,'foodmanageapp/home.html')
def registration_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/p_info')
    return render(request,'foodmanageapp/registration.html',{'form':form})
@login_required
def menu_view(request):
    menu=PgMenu.objects.all()
    form=PersonalDetailsForm()
    if request.method=='POST':
        form=PersonalDetailsForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
    return render(request,'foodmanageapp/menu.html',{'menu':menu,'form':form})
def breakfast_view(request):
    today=datetime.date.today()
    date=datetime.datetime.now()
    bform=BreakfastAgreementForm()
    if request.method=='POST':
        bform=BreakfastAgreementForm(request.POST)
        if bform.is_valid():
            bform.save()
            return HttpResponseRedirect('/')
    return render(request,'foodmanageapp/breakfast.html',{'today':today,'bform':bform})

def lunch_view(request):
    today=datetime.date.today()
    date=datetime.datetime.now()
    lform=LunchAgreementForm()
    if request.method=='POST':
        lform=LunchAgreementForm(request.POST)
        if lform.is_valid():
            lform.save()
            return HttpResponseRedirect('/')
    return render(request,'foodmanageapp/lunch.html',{'today':today,'lform':lform})



def dinner_view(request):
    today=datetime.date.today()
    date=datetime.datetime.now()
    dform=DinnerAgreementForm()
    if request.method=='POST':
        dform=DinnerAgreementForm(request.POST)
        if dform.is_valid():
            dform.save()
            return HttpResponseRedirect('/')
    return render(request,'foodmanageapp/dinner.html',{'today':today,'dform':dform})


def personal_info_view(request):
    form=PersonalDetailsForm()
    if request.method=='POST':
        form=PersonalDetailsForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/accounts/login')
        # else:
        #    return HttpResponse('<h1> form is invalid</h1>')
    return render(request,'foodmanageapp/info.html',{'form':form})
def logout_view(request):
    logout(request)
    return render(request,'foodmanageapp/logout.html')
def booked_members_view(request):
        bfdel=BreakfastAgreement.objects.filter(date__lt=datetime.date.today())
        for object in bfdel:
            object.delete()
        bf_qs=BreakfastAgreement.objects.filter(breakfast__iexact='yes')
        bf_no=bf_qs.count()
        lunchdel=LunchAgreement.objects.filter(date__lt=datetime.date.today())
        for object in lunchdel:
            object.delete()
        lunch_qs=LunchAgreement.objects.filter(lunch__iexact='yes')
        lunch_no=lunch_qs.count()
        dinnerdel=DinnerAgreement.objects.filter(date__lt=datetime.date.today())
        for object in dinnerdel:
            object.delete()
        dinner_qs=DinnerAgreement.objects.filter(dinner__iexact='yes')
        dinner_no=dinner_qs.count()
        return render(request,'foodmanageapp/booked_members.html',{'bf_no':bf_no,'lunch_no':lunch_no,'dinner_no':dinner_no})
@login_required
def update_view(request,id):
    item=PgMenu.objects.get(id=id)
    if request.method=='POST':
        form=PgMenuForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/menu')
    return render(request,'foodmanageapp/update.html',{'item':item})
