from django.db import models

# Create your models here.
class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100) 
    message = models.TextField() # Сообщение
    created_at = models.DateTimeField(auto_now_add=True) 
def __str__(self):
    return f"{self.name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
