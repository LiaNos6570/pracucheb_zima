from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')  # Используйте только существующие поля
    list_filter = ('submitted_at',)  # Поля, которые можно фильтровать
    ordering = ('-submitted_at',)  # Поле для сортировки (убедитесь, что оно существует)

admin.site.register(Feedback, FeedbackAdmin)

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),  # Добавляем поле phone, если оно есть в вашей модели
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone',)}),
    )