from django.contrib.auth.models import User
from django.db import models
from django import forms
from foodmanageapp.models import PgMenu,PersonalDetails,BreakfastAgreement,LunchAgreement,DinnerAgreement,Student
import datetime
from django.core.validators import ValidationError

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model=PersonalDetails
        fields='__all__'

class BreakfastAgreementForm(forms.ModelForm):
    class Meta:
        model=BreakfastAgreement
        fields=['breakfast']
    def clean_breakfast(self):
        inputb=self.cleaned_data['breakfast']
        date=datetime.datetime.now()
        h=int(date.strftime("%H"))
        if h>6:
            raise ValidationError('book breakfast before 6:oo am only')
        y='yes'
        n='no'
        if inputb!=y and inputb!=n:
            raise ValidationError('put only yes or no')
        return inputb
class LunchAgreementForm(forms.ModelForm):
    class Meta:
        model=LunchAgreement
        fields=['lunch']
    def clean_lunch(self):
        inputb=self.cleaned_data['lunch']
        date=datetime.datetime.now()
        h=int(date.strftime("%H"))
        if h>10:
            raise ValidationError('book lunch before 10:oo am only')
        y='yes'
        n='no'
        if inputb!=y and inputb!=n:
            raise ValidationError('put only yes or no')
        return inputb
class DinnerAgreementForm(forms.ModelForm):
    class Meta:
        model=DinnerAgreement
        fields=['dinner']
    def clean_dinner(self):
       inputb=self.cleaned_data['dinner']
       date=datetime.datetime.now()
       h=int(date.strftime("%H"))
       if h>18:
           raise ValidationError('book dinner before 6:oo pm only')
       y='yes'
       n='no'
       if inputb!=y and inputb!=n:
           raise ValidationError('put only yes or no')
       return inputb
class PgMenuForm(forms.ModelForm):
    class Meta:
        model=PgMenu
        fields='__all__'
