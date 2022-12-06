from django.db import models


class Options(models.Model):
    answer = models.CharField(max_length=200, verbose_name='ответ')
    score = models.PositiveIntegerField(verbose_name='балл')

    def __str__(self):
        return f"{self.answer}"

class Questions(models.Model):
    question = models.CharField(max_length=250,verbose_name='вопрос')

    def __str__(self):
        return f"{self.question}"

class Result(models.Model):
    min_score = models.PositiveIntegerField(verbose_name='от')
    max_score = models.PositiveIntegerField(verbose_name='до')
    recommendation = models.TextField(verbose_name='рекомендация')

class Answer(models.Model):
    """Ответ пользователя"""
    question = models.CharField(max_length=250,verbose_name='вопрос')
    score = models.PositiveIntegerField(verbose_name='балл')
