from django.db import models

class status_info(models.Model):
    status = models.CharField(max_length=10,null=True,default=1)

    def __str__(self):
        return self.status