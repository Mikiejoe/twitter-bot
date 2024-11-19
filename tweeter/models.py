from django.db import models


class Tweet(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"
        ordering = ("-created_at",)

    def __str__(self):
        return self.text


class Token(models.Model):
    name = models.CharField(max_length=300, primary_key=True)
    token = models.TextField()

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"

    def __str__(self):
        return self.token
