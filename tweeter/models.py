from django.db import models


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
        ordering = ("-created_at",)

    def __str__(self):
        return self.text


class Token(models.Model):
    name = models.CharField(max_length=140, primary_key=True)
    token = models.CharField(max_length=140)

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def __str__(self):
        return self.token
