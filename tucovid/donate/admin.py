from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Item._meta.fields]

@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Donate._meta.fields]
    list_editable = ('status',)
    list_filter = ('status',)

@admin.register(Receive)
class ReceiveAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Receive._meta.fields]
    list_filter = ('hospital', 'status')
    list_editable = ('shipping_id',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields]

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Job._meta.fields]

@admin.register(DonateItem)
class DonateItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DonateItem._meta.fields]
    list_editable = ('show_item',)
    list_filter = ('show_item',)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hospital._meta.fields]