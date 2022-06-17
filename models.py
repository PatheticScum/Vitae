from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=40)

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Wallpaper(models.Model):
    title = models.CharField(max_length=40)
    photo = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('wallpaper_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


# Anime

class Anime(models.Model):
    title = models.CharField(max_length=40)
    photo = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('anime_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


# NFT

class NFT(models.Model):
    title = models.CharField(max_length=40)
    photo = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('nft_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
