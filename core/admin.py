from django import forms
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(AboutHomePage)
class AboutHomePageAdmin(TranslationAdmin):
    """About Home Page"""
    fields = ('title', 'description')
    list_display = ('title', 'description')

@admin.register(ProductHomePage)
class ProductHomePageAdmin(TranslationAdmin):
    """Product Home Page"""
    fields = ('title', 'description')
    list_display = ('title', 'description')

@admin.register(ProjectHomePage)
class ProjectHomePageAdmin(TranslationAdmin):
    """Project Home Page"""
    fields = ('title',)
    list_display = ('title',)

@admin.register(Statistic)
class StatisticAdmin(TranslationAdmin):
    """Statistics"""
    fields = ('description',)
    list_display = ('description',)

@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    """About Us"""
    fields = ('title_1', 'title_2', 'description_1', 'description_2')
    list_display = ('title_1', 'title_2', 'description_1', 'description_2')

class ContactAdmin(admin.ModelAdmin):
    """Contact Messages"""
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register(HeroSection)
admin.site.register(Partners)
admin.site.register(Certificate)
admin.site.site_title = "Your Site Title"
admin.site.site_header = "Your Site Header"
