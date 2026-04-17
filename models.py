from django.db import models
from django.conf import settings

class Board(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='boards')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    cover_pin = models.ForeignKey('pins.Pin', on_delete=models.SET_NULL, null=True, blank=True, related_name='board_cover')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s {self.name}"

class BoardPin(models.Model):
    """Junction table for Many-to-Many between Boards and Pins with timestamp"""
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board_pins')
    pin = models.ForeignKey('pins.Pin', on_delete=models.CASCADE, related_name='board_pins')
    saved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['board', 'pin']
        ordering = ['-saved_at']