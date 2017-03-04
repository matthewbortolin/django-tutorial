from django.contrib import admin

# Register your models here.

from.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
