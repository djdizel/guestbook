from django.db import models

# Create your models here.
class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100) # Имя Гостя
    message = models.TextField() # Сообщение
    created_at = models.DateTimeField(auto_now_add=True) #Автомат отметка времени
def __str__(self):
    return f"{self.name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
