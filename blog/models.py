from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #models.ForeignKey – this is a link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.CharField – this is how you define text with a limited number of characters
    title = models.CharField(max_length=200)
    #models.TextField – this is for long text without a limit. Sounds ideal for blog post content
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text