from django.db import models
from django.conf import settings
import binascii
import os

# Create your models here.
class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not  self.key:
            self.key = self.generate_key()
        return super(Token,self).save(*args,**kwargs)

    def generate_key(self):
        return  binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key