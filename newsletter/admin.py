from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import path
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
    
    actions = ['send_selected_newsletters']
    
    def send_selected_newsletters(self, request, queryset):
        """Custom admin action to send selected newsletters"""
        email_count = 0
        newsletter_count = 0
        
        for newsletter in queryset:
            if newsletter.sent_at:
                self.message_user(
                    request, 
                    f'Newsletter "{newsletter.subject}" has already been sent and was skipped.', 
                    messages.WARNING
                )
                continue
                
            try:
                emails_sent = newsletter.send_newsletter()
                email_count += emails_sent
                newsletter_count += 1
                self.message_user(
                    request, 
                    f'Successfully sent "{newsletter.subject}" to {emails_sent} subscribers!', 
                    messages.SUCCESS
                )
            except Exception as e:
                self.message_user(
                    request, 
                    f'Error sending "{newsletter.subject}": {str(e)}', 
                    messages.ERROR
                )
        
        if newsletter_count > 0:
            self.message_user(
                request, 
                f'Sent {newsletter_count} newsletter(s) to a total of {email_count} subscribers.', 
                messages.SUCCESS
            )
    
    send_selected_newsletters.short_description = "Send selected newsletters to subscribers"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('create-newsletter/', self.admin_site.admin_view(self.redirect_to_create_view), 
                 name='create-newsletter'),
        ]
        return custom_urls + urls
    
    def redirect_to_create_view(self, request):
        """Redirect to the custom newsletter creation view"""
        return redirect('create_newsletter')