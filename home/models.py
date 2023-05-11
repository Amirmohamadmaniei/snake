from django.db import models
from django.conf import settings


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    high_score = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} :{self.high_score}'
