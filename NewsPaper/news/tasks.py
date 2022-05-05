import datetime

from celery import shared_task
import time

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


from .models import Post, Category


@shared_task()
def send_weekly_mail():
    time_delta = datetime.timedelta(7)
    start_date = datetime.datetime.utcnow() - time_delta
    end_date = datetime.datetime.utcnow()
    recent_posts = Post.objects.filter(creation_date__range=(start_date, end_date))

    for category in Category.objects.all():
        html_content = render_to_string('account/email/weekly_mailing.html',
                                        {'posts': recent_posts, 'categories': category}, )
        msg = EmailMultiAlternatives(
            subject=f'"Have you seen new posts of the interesting categories this week?"',
            body="NewsList",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=category.get_subscribers_emails())
        msg.attach_alternative(html_content, "text/html")
        msg.send()