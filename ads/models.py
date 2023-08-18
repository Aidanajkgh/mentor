from django.db import models
from django.utils import timezone
from users.models import User

class Ads(models.Model):
    LEARN = "I want to learn"
    TEACH = "I can teach" 
    TYPE_OF_ADS = [
        (LEARN, "I want to learn"),
        (TEACH, "I can teach")
    ]


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Subcategory(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self) -> str:
        return self.title


subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='ads', null=True, blank=True)
title = models.CharField(max_length=150)
description = models.TextField()
price = models.FloatField()
owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
type = models.CharField(max_length=100, choices=Ads.TYPE_OF_ADS, default=Ads.LEARN)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
    
class Meta:
    verbose_name = "Ads"
    verbose_name_plural = "Ads"

    def __str__(self) -> str:
        return self.title