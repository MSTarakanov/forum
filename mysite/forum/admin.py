from django.contrib import admin

from .models import Users, Sex, Messages

admin.site.register(Sex)

admin.site.register(Messages)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'sex_id', 'date_joined')
    search_fields = ('username', 'email')


admin.site.register(Users, UsersAdmin)
