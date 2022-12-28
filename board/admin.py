from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Board, Board_Comment

# Register your models here.
admin.site.register(Board, MarkdownxModelAdmin)
admin.site.register(Board_Comment)