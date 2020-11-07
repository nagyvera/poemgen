from django.db import models
import datetime

class Poem(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=datetime.date.today)

    def publish(self):
        self.published_date = datetime.date.today()
        self.save()

    def __str__(self):
        return self.title

class PoemDetails(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=450)

    def __str__(self):
        return self.title
        

