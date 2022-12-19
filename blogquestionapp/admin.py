from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import QuestionPost, QuestionTag, QuestionComment

admin.site.register(QuestionPost, MarkdownxModelAdmin)
admin.site.register(QuestionComment)

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


# admin.site.register(QuestionCategory, CategoryAdmin)
admin.site.register(QuestionTag, TagAdmin)