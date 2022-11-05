from django.contrib.auth.models import User
from django.db import models
from ..models import status_info,roles_info

class User_extInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    emp_contact = models.CharField(max_length=10,null=True,default='')
    emp_job_title = models.CharField(max_length=10,null=True,default='')
    emp_no_of_employees = models.CharField(max_length=10,null=True,default='')
    emp_interest = models.CharField(max_length=10,null=True,default='')
    emp_free_text = models.CharField(max_length=10,null=True,default='')
    emp_country = models.CharField(max_length=10,null=True,default='')
    emp_status =models.ForeignKey(status_info, on_delete=models.CASCADE,null=True, default=1)
    emp_role =models.ForeignKey(roles_info, on_delete=models.CASCADE, null=True,default=1)
    # def __str__(self):
    #     return self.user.username