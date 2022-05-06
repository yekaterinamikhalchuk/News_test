import datetime

from celery import shared_task
import time

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


from .models import Post, Category


@shared_task()
def send_weekly_mail():
    from_date = datetime.datetime.now() - datetime.timedelta(days=7)

    for category in Category.objects.all():
        recent_posts = Post.objects.filter(categories=category).filter(creation_date__gte=(from_date))
        if recent_posts.exists():
            html_content = render_to_string('account/email/weekly_mailing.html',
                                            {'posts': recent_posts, 'categories': category}, )
            msg = EmailMultiAlternatives(
                subject=f'"Have you seen new posts of the interesting categories this week?"',
                body="NewsList",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=category.get_subscribers_emails())
            msg.attach_alternative(html_content, "text/html")
            msg.send()


@shared_task
def news_mail(subject, from_email, recipients, html_content):
    msg = EmailMultiAlternatives(
                subject=subject,
                from_email=from_email,
                to=recipients
            )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

