import random

from .models import Post, PostCategory, Category, Comment, Author
from django.contrib.auth.models import User
from .articles import *


def launch():
    user1 = User.objects.create_user('Mike Smith', email='mikes@gmail.com', password='5432112345')
    user2 = User.objects.create_user('Elizabeth Baldwin', email='lizaa@gmail.com', password='1234554321')
    user3 = User.objects.create_user('Ashleigh Crowter', email='Ashleigh@gmail.com', password='1234554321')
    user4 = User.objects.create_user('Tom Espiner', email='Tom@gmail.com', password='1234554321')

    author1 = Author.objects.create(user=user1)
    author2 = Author.objects.create(user=user2)
    author3 = Author.objects.create(user=user3)
    author4 = Author.objects.create(user=user4)

    category1 = Category.objects.create(category_name='Business')
    category2 = Category.objects.create(category_name='Economy')
    category3 = Category.objects.create(category_name='Ecology')
    category4 = Category.objects.create(category_name='Sport')

    post1 = Post.objects.create(post_title=post_title1, post_text=post_text1, author=author1)
    post2 = Post.objects.create(post_title=post_title2, post_text=post_text2, author=author1)
    post3 = Post.objects.create(news_type='N', post_title=post_title3, post_text=post_text3, author=author2)
    post4 = Post.objects.create(news_type='N', post_title=post_title4, post_text=post_text4, author=author2)
    post5 = Post.objects.create(news_type='A', post_title=post_title5, post_text=post_text5, author=author3)
    post6 = Post.objects.create(news_type='A', post_title=post_title6, post_text=post_text6, author=author3)
    post7 = Post.objects.create(news_type='A', post_title=post_title7, post_text=post_text7, author=author4)
    post8 = Post.objects.create(news_type='N', post_title=post_title8, post_text=post_text8, author=author4)
    post9 = Post.objects.create(news_type='A', post_title=post_title9, post_text=post_text9, author=author4)
    post10 = Post.objects.create(news_type='A', post_title=post_title10, post_text=post_text10, author=author2)
    post11 = Post.objects.create(news_type='N', post_title=post_title11, post_text=post_text11, author=author1)

    PostCategory.objects.create(post=post1, category=category1)
    PostCategory.objects.create(post=post1, category=category2)
    PostCategory.objects.create(post=post2, category=category4)
    PostCategory.objects.create(post=post3, category=category3)
    PostCategory.objects.create(post=post3, category=category2)
    PostCategory.objects.create(post=post4, category=category4)
    PostCategory.objects.create(post=post5, category=category1)
    PostCategory.objects.create(post=post5, category=category2)
    PostCategory.objects.create(post=post6, category=category2)
    PostCategory.objects.create(post=post7, category=category2)
    PostCategory.objects.create(post=post7, category=category3)
    PostCategory.objects.create(post=post8, category=category2)
    PostCategory.objects.create(post=post9, category=category3)
    PostCategory.objects.create(post=post9, category=category2)
    PostCategory.objects.create(post=post10, category=category2)
    PostCategory.objects.create(post=post10, category=category1)
    PostCategory.objects.create(post=post10, category=category3)
    PostCategory.objects.create(post=post11, category=category2)
    PostCategory.objects.create(post=post11, category=category1)

    comment1 = Comment.objects.create(comment_post=post2, comment_user=user2,
                                  comment_text='Sport really is a great part of our lives that provides opportunities to many things except good physical form. Sport and team work make us only better and develop our best characteristics!')
    comment2 = Comment.objects.create(comment_post=post2, comment_user=user1,
                                  comment_text='Thank you for your opinion!')
    comment3 = Comment.objects.create(comment_post=post1, comment_user=user2,
                                  comment_text='It is a very difficult time for me and my bakery business. I hope we will manage. Thank you for such an informative article')
    comment4 = Comment.objects.create(comment_post=post1, comment_user=user1,
                                  comment_text='I have the same situation, planning to cut ' \
                                               'expenses where it is possible')
    comment5 = Comment.objects.create(comment_post=post1, comment_user=user1,
                                  comment_text='I am glad that you find this article to be usefull, ' \
                                               'hope everything will be good')
    comment6 = Comment.objects.create(comment_post=post3, comment_user=user3,
                                  comment_text='Nothing will save the environment!')
    comment7 = Comment.objects.create(comment_post=post4, comment_user=user3,
                                  comment_text='Cafu, Lothar Matthaus, Didier Deschamps. And Jermaine Jenas. ' \
                                               'So many footballing giants assembled together.')
    comment8 = Comment.objects.create(comment_post=post4, comment_user=user4,
                                  comment_text='Cafu looked like he could still play at the top level - legend !!')
    comment9 = Comment.objects.create(comment_post=post11, comment_user=user4,
                                  comment_text='Stop war')
    comment10 = Comment.objects.create(comment_post=post6,
                                   comment_user=user1,
                                   comment_text='So interesting story. World lacks such conscientious men')
    comment11 = Comment.objects.create(comment_post=post7,
                                   comment_user=user1,
                                   comment_text=('Meanwhile, Shell only pay homeowners 3.5p per kWh generated by ' \
                                                 'solar ' \
                                                 'when the wholesale rate is 20p and they made ' \
                                                 '£12bn profit last year. Time to make this solar thing work ' \
                                                 'for everyone.'))
    comment12 = Comment.objects.create(comment_post=post7,
                                   comment_user=user2,
                                   comment_text=('Octopus offer an outgoing tariff ' \
                                                 'where rates they pay you change ' \
                                                 'every half hour based on wholesale rates.' \
                                                 'At 5.30pm today for example they will pay 32p/kwh for 30 ' \
                                                 'mins. Admittedly you might not be generating much ' \
                                                 'solar at 530pm today, but still, we need more ' \
                                                 'innovative tariffs like this to encourage ' \
                                                 'greater take up of solar.'))

    comment13 = Comment.objects.create(comment_post=post9,
                                   comment_user=user3,
                                   comment_text=("I’m sure if we can manage to update " \
                                                 "instantaneously instagram and tik tok " \
                                                 "globally we can certainly rise to the challenge!"))
    comment14 = Comment.objects.create(comment_post=post9,
                                   comment_user=user2,
                                   comment_text=("We will need these warning systems as " \
                                                 "Net Zero policies will make us more vulnerable " \
                                                 "to extreme weather."))
    list_for_rating = [
        post1, post2, post3,
        post11, post4, post5,
        post6, post7, post8,
        post9, post10,
        comment1, comment2, comment3,
        comment4, comment5, comment6,
        comment7, comment8, comment9,
        comment10, comment11, comment12,
        comment13, comment14
    ]

    for i in range(100):
        random_obj = random.choice(list_for_rating)
        if i % 2:
            random_obj.like()
        else:
            random_obj.dislike()

    Author.objects.get(pk=1).update_rating()
    Author.objects.get(pk=2).update_rating()
    Author.objects.get(pk=3).update_rating()
    Author.objects.get(pk=4).update_rating()

    best_author = Author.objects.all().order_by('-user_rating')[0].user.username
    print('The best author is', best_author)

    best_article = Post.objects.filter(news_type='A').order_by('-post_rating')[0]
    best_article_rating = best_article.post_rating
    best_article_time = best_article.creation_date
    best_article_author = best_article.author.user.username
    best_article_preview = best_article.preview()
    best_article_title = best_article.post_title

    print(f'The best article with overall rating {best_article_rating} points is entitled {best_article_title}. \n'
          f'It is written by {best_article_author} at {best_article_time}.\n'
          f'Preview: {best_article_preview}')

    for comment in Comment.objects.filter(comment_post=best_article):
        print(
            f'Comment id: {comment.id}, \n'
            f'Data: {comment.creation_date_comment}, \n'
            f'Username: {comment.comment_user.username}, \n'
            f'Rating: {comment.comment_rating}, \n'
            f'Comment: {comment.comment_text}'
        )
