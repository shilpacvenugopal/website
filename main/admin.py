from django.contrib import admin
from .models import Job, JobApplication,InvestorQuery

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'posted_on')
    list_filter = ('category', 'posted_on')
    search_fields = ('title', 'category')
    ordering = ('-posted_on',)
    list_per_page = 20

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'qualification', 'applied_on')
    search_fields = ('name', 'email', 'role')
    list_filter = ('applied_on', 'qualification')
    ordering = ('-applied_on',)
    list_per_page = 20


@admin.register(InvestorQuery)
class InvestorQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'area_of_interest', 'submitted_at')
    search_fields = ('name', 'email', 'phone', 'area_of_interest')
    list_filter = ('area_of_interest', 'submitted_at')