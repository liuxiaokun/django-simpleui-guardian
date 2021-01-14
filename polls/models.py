import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='问题内容')
    pub_date = models.DateTimeField(verbose_name='发布日期')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        #db_table = 'polls_question'
        verbose_name = '问题'
        verbose_name_plural = verbose_name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='选项内容')
    votes = models.IntegerField(default=0, verbose_name='得票数')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = verbose_name
