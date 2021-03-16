from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class Tag(models.Model):
    tag_name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.tag_name