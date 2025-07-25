from django.contrib import admin
from .models import Role, Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # Default number of empty option forms displayed
    min_num = 1  # Require at least one option per question
    verbose_name = "Answer Option"
    verbose_name_plural = "Answer Options"
    # Optional: show_change_link=True can be added to enable direct links to option editing

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text', 'role')
    search_fields = ('text', 'role__name')
    list_filter = ('role',)
    ordering = ('role', 'text')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Role, RoleAdmin)
admin.site.register(Question, QuestionAdmin)
# Optionally, register Option as standalone if you want direct admin access:
# admin.site.register(Option)
