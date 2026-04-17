from django.contrib import admin

from .models import Board, BoardPin


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_private', 'created_at')


@admin.register(BoardPin)
class BoardPinAdmin(admin.ModelAdmin):
    list_display = ('board', 'pin', 'saved_at')
