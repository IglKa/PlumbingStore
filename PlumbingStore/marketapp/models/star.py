from django.db import models


class Star(models.Model):
    value = models.SmallIntegerField()

    def __str__(self):
        return f'{self.value}'
