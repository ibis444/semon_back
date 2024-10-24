from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email')







admin.site.register(Contact, ContactAdmin)
admin.site.register(HeroSection)
admin.site.register(AboutHomePage)
admin.site.register(ProductHomePage)
admin.site.register(Statistic)
admin.site.register(Partners)
admin.site.register(ProjectHomePage)
admin.site.register(AboutUs)
admin.site.register(Certificate)