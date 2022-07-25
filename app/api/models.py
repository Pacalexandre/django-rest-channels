from django.db import models


class Processo(models.Model):
    processo = models.CharField(max_length=20, blank=False)
    ativo = models.BooleanField(default=True, blank=False)

    def __str__(self) -> str:
        return str(self.processo)

    class Meta:
        ordering = ['id']
