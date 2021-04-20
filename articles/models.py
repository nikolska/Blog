from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-pub_date']


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	author_name = models.CharField(max_length=100)
	comment_text = models.TextField()
	pub_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.author_name

	class Meta:
		ordering = ['article']
