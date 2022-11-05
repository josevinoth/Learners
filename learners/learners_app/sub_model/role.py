from django.db import models

class roles_info(models.Model):
    roles = models.CharField(max_length=30,null=True,default=1)

    def __str__(self):
        return self.roles