from django.contrib import admin
from .models import Question
from .models import Book, BorrowHistory

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Book)
admin.site.register(BorrowHistory)