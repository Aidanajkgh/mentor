from django.db import models
from django.utils import timezone
from users.models import User


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


class Ads(models.Model):
    LEARN = "I want to learn"
    TEACH = "I can teach" 
    TYPE_OF_ADS = [
        (LEARN, "I want to learn"),
        (TEACH, "I can teach")
    ]
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='ads', null=True, blank=True)
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(default="")
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="images/ads/", default="images.jpg")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', null=True, blank=True)
    type = models.CharField(max_length=100, choices=TYPE_OF_ADS, default=LEARN)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Ads"
        verbose_name_plural = "Ads"
