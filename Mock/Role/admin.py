from django.contrib import admin
from .models import Role, Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4  # Number of options shown by default

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text', 'role')
    search_fields = ('text',)

admin.site.register(Role)
admin.site.register(Question, QuestionAdmin)
