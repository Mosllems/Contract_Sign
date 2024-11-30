from django.contrib.auth.models import User
from accounts.models import CustomUser
from django.db import models


class Contract(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="Lorem ipsum ...")
    full_name_signer_1 = models.CharField(max_length=200, null=True, blank=True)
    full_name_signer_2 = models.CharField(max_length=200, null=True, blank=True)
    signer_1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='signed_contracts')
    signer_2 = models.EmailField()
    Is_signed_by_1 = models.BooleanField(default=False)
    Is_signed_by_2 = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

