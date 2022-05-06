from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import mail_managers, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post, Category
from django.conf import settings
from .tasks import news_mail


@receiver(m2m_changed, sender=Post.categories.through)
def notify_subscribers(instance, action, pk_set, *args, **kwargs):
    if action == 'post_add':
        html_content = render_to_string(
            'account/email/send.html',
            {'my_post': instance}
        )
        for pk in pk_set:
            category = Category.objects.get(pk=pk)
            recipients = [user.email for user in category.subscribers.all()]
            subject = f'New post of {category} category on the NewsChannel'
            from_email = settings.DEFAULT_FROM_EMAIL
            news_mail.delay(subject, from_email, recipients, html_content)



