from django.contrib import admin
from .models import NewsletterSubscriber, Newsletter

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed', 'is_active')
    list_filter = ('is_active', 'date_subscribed')
    search_fields = ('email',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created_at', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('subject', 'content')
    readonly_fields = ('sent_at',)