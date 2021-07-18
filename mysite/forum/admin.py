from django.contrib import admin

from .models import SiteUser, Sex, Messages

admin.site.register(Sex)

admin.site.register(Messages)


class SiteUserAdmin(admin.ModelAdmin):
    ordering = ('-start_date',)
    list_display = ('username', 'sex', 'email', 'start_date')
    search_fields = ('username', 'email', 'first_name', 'second_name', 'fathers_name')
    list_filter = ('sex',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password', 'photo', 'start_date')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('first_name', 'second_name', 'fathers_name', 'sex', 'birth_date', 'about')})
    )

admin.site.register(SiteUser, SiteUserAdmin)
