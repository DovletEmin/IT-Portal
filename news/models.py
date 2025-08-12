from django.db import models

class BaseNews(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    class Meta: 
        abstract = True
        ordering = ['-date_posted']


class TextNews(BaseNews):
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class VideoNews(BaseNews):
    video = models.FileField(upload_to='news_videos/', blank=True, null=True)

    def __str_(self):
        return self.title