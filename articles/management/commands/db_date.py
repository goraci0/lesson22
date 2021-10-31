from django.core.management.base import BaseCommand

from articles.models import Article, Comment


class Command(BaseCommand):

    def handle(self, *args, **options):

# all articles
        articles = Article.objects.all()
        for art in articles:
            print(art.article_name)

# articles
        art_ = Article.objects.get(article_name='Novorossiysk')
        print(art_,art_.article_text)

# all_comment
        comment = Comment.objects.all()
        for com in comment:
            print(com)

