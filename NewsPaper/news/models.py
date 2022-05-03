from django.contrib.auth.models import User
from django.db import models

from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.all().aggregate(Sum('post_rating')).get('post_rating__sum', 0) * 3
        comment_rating = self.user.comment_set.all().aggregate(Sum('comment_rating')).get('comment_rating__sum', 0)
        news_comments = Post.objects.filter(author=self).values('comment__comment_rating')
        news_comments_rating = sum(rate['comment__comment_rating'] for rate in news_comments)
        self.user_rating = post_rating + comment_rating + news_comments_rating
        self.save()

        return f'{self.user_rating}'

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    category_name = models.CharField(
        max_length=255,
        unique=True
    )

    subscribers = models.ManyToManyField(User, through='UserCategory')

    def __str__(self):
        return f'{self.category_name}'

    def get_subscribers_emails(self):
        result = set()
        for user in self.subscribers.all():
            result.add(user.email)
        return


class Post(models.Model):

    news_type = models.CharField(
        max_length=2,
        choices=[
    ('A', 'Article'),
    ('N', 'News')
],
        default='A'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True
    )
    post_title = models.CharField(
        max_length=255
    )
    post_text = models.TextField(

    )
    post_rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        pre_text = 124 if len(self.post_text) > 124 else len(self.post_text)
        return self.post_text[:pre_text]+'...'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date_comment = models.DateTimeField(
        auto_now_add=True
    )
    comment_text = models.CharField(
        max_length=255
    )
    comment_rating = models.FloatField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

class UserCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='user_category')


