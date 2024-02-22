from django.db import models
from django.contrib.auth.models import User 


class Category(models.Model):
    name=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class scenario(models.Model):
    category=models.ForeignKey(Category, related_name='scenarios', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    #possible optins for the scenario
    created_by=models.ForeignKey(User,related_name='scenarios',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='scenario_images',blank=True,null=True)
    def __str__(self):
        return self.name
