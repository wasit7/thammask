from django.contrib import admin
from django.shortcuts import render, redirect
from .models import *
import datetime
import time
# Register your models here.
def print(modeladmin, request, queryset):
    queryset.update(status='กำลังบรรจุ')
    d = datetime.datetime.today()
    day = d.strftime("%d")
    month = d.strftime("%m")
    year = d.strftime("%Y")
    count_order = Order.objects.all().count()
    count_order += 1
    order_name = str(day)+'/'+str(month)+'/'+str(year)+' (ครั้งที่ '+str(count_order)+')'
    order = Order.objects.create(order_name=order_name)
    for data in queryset:
        OrderItem.objects.create(order=order, receive=data)

    return redirect('donate:printing')

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
    actions = [print]

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

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]