from django.contrib import admin
from .models import *
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
# Register your models here.
admin.site.register(Events)
admin.site.register(EventTypes)
admin.site.register(Sports)
admin.site.register(EmployeeWellness)
admin.site.register(Donations)
admin.site.register(UserDonation)
admin.site.register(Workshops)
admin.site.register(TimeLines)
admin.site.register(Organizers)
admin.site.register(ExampleFiles)
class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email','id', 'user_name', 'first_name',
                    'is_active', 'is_staff')
    # fieldsets = (
    #     (None, {'fields': ('email', 'user_name', 'first_name',)}),
    #     ('Permissions', {'fields': ('is_staff', 'is_active')}),
    #     ('Personal', {'fields': ('about',)}),
    # )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
    #      ),
    # )


admin.site.register(NewUser, UserAdminConfig)