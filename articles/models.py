from django.db import models

# Create your models here.

class Article(models.Model):
    article_name = models.CharField(max_length = 100)
    article_text = models.TextField(max_length = 10000)
    article_date = models.DateTimeField('date published', null=True)
    article_img = models.ImageField(upload_to='articles', null=True, blank=True)

    def __str__(self):
        return f'{self.article_name}, published: {self.article_date}'

class Comment(models.Model):
    comment_autr = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment_autor = models.CharField(max_length = 50, null=True)
    comment_text = models.CharField(max_length = 1000)
    comment_artc = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment_autr}-{self.comment_text}'