from django.conf import settings
from django.db import models
from django.utils import timezone

# define model
# models => Post가 table이라고 인식하게 해줌.
class Post(models.Model):
    id = models.BigIntegerField().primary_key
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # for limit text
    title = models.CharField(max_length=200)
    # for limitless text
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title