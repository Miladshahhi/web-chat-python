from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'{self.user.username}: {self.content}'
