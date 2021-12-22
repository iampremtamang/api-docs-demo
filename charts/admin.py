from django.contrib import admin
from charts.models import Editor


@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ('id', 'editor_name')
