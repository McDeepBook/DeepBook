from django.db import models
from django.conf import settings

class Deep(models.Model):
    image = models.ImageField()
    result = models.TextField()
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={
                        'username' : self.user.username,
                        'pk' : self.pk
        })
        
    class Meta:
        ordering = ['-time']  # 최신글이 가장 위로 올라오도록 역순으로 지정