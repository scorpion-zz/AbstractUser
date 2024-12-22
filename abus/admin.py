from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from abus.models import MyAbUser
class MyAbUserAdmin(UserAdmin):
    model = MyAbUser # кастомный пользователь
    # Указывание полей, которые вы хотите отображать в админке
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cender', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('cender', 'birth_date')}),
    )
admin.site.register(MyAbUser, MyAbUserAdmin)