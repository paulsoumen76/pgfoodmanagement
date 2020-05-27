from django.contrib import admin
from foodmanageapp.models import PgMenu,PersonalDetails,BreakfastAgreement,LunchAgreement,DinnerAgreement
# Register your models here.
class PgMenuAdmin(admin.ModelAdmin):
    list_display=['id','day','breakfast','lunch','dinner']
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display=['id','name','room_no','mobile_no']
class BreakfastAgreementAdmin(admin.ModelAdmin):
    list_display=['id','date','breakfast']
class LunchAgreementAdmin(admin.ModelAdmin):
    list_display=['id','date','lunch']
class DinnerAgreementAdmin(admin.ModelAdmin):
    list_display=['id','date','dinner']
admin.site.register(PgMenu,PgMenuAdmin)
admin.site.register(PersonalDetails,PersonalDetailsAdmin)
admin.site.register(BreakfastAgreement,BreakfastAgreementAdmin)
admin.site.register(LunchAgreement,LunchAgreementAdmin)
admin.site.register(DinnerAgreement,DinnerAgreementAdmin)
