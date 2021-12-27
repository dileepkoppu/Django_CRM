from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Lead, Agent, UserProfile, Category, FollowUp



class LeadAdmin(admin.ModelAdmin):
    # fields = (
    #     'first_name',
    #     'last_name',
    # )

    list_display = ['first_name', 'last_name', 'age', 'email']
    list_display_links = ['first_name']
    list_editable = ['last_name']
    list_filter = ['category']
    search_fields = ['first_name', 'last_name', 'email']

class CustomUserAdmin(UserAdmin):
    fieldsets=UserAdmin.fieldsets+((None,{'fields':('is_organisor','is_agent')}),)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]

admin.site.register(Category,CategoryAdmin)
admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Agent)
admin.site.register(FollowUp)
