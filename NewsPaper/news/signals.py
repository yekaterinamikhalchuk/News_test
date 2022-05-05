from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import mail_managers, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post
from django.conf import settings


# @receiver(m2m_changed, sender=Post.categories.through)
# def notify_subscribers(sender, instance, action, **kwargs):
#     if action == 'post_add':
#         html_content = render_to_string('news/send.html', {'my_post': instance}, )
#         cats = instance.categories.all()
#         sendto_set = set()
#         # формируем список для рассылки
#         for cat in cats:
#             sendto_set |= cat.get_subscribers_emails()
#         # if len(cats) == 1:
#         msg = EmailMultiAlternatives(
#             subject=f'{instance.post_title}',
#             body=f'{instance.post_text}',
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             to=sendto_set)
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
from .tasks import send_when_post_created

def create_post():
    send_when_post_created.delay()
