from django.contrib import admin

from .models import Tweet, Token


class TweetAdmin(admin.ModelAdmin):
    list_display = ("text", "created_at")
    search_fields = ("text",)
    list_filter = ("created_at",)


class TokenAdmin(admin.ModelAdmin):
    list_display = ("name", "token")
    search_fields = ("name",)
    list_filter = ("name",)


admin.site.register(Tweet, TweetAdmin)
admin.site.register(Token, TokenAdmin)
