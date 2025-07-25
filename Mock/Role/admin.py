from django.contrib import admin
from .models import Role, Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # Number of blank option forms by default
    min_num = 1  # Require at least one option per question
    verbose_name = "Answer Option"
    verbose_name_plural = "Answer Options"
    # Optional: you can add show_change_link=True if you want inline option links

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text', 'role')
    search_fields = ('text', 'role__name')
    list_filter = ('role',)  # Add filter sidebar by role
    ordering = ('role', 'text')
    # Optional: add readonly_fields, prepopulated_fields, etc. if you have slug or other fields

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Role, RoleAdmin)
admin.site.register(Question, QuestionAdmin)
