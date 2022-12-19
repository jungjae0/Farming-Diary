from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os


class QuestionTag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blogquestion/tag/{self.slug}/'


# class QuestionCategory(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return f'/blogquestion/category/{self.slug}/'
#
#     class Meta:
#         verbose_name_plural = 'categories'


class QuestionPost(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()

    head_image = models.ImageField(upload_to='blogquestion/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blogquestion/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    # category = models.ForeignKey(QuestionCategory, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(QuestionTag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blogquestion/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)


class QuestionComment(models.Model):
    post = models.ForeignKey(QuestionPost, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
