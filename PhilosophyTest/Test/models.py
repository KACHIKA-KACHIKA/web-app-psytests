from django.db import models
from django.contrib.auth.models import User


class UserPersonalInfo(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=45)
    user_second_name = models.CharField(max_length=45)
    user_father = models.CharField(max_length=45)
    user_group = models.CharField(max_length=45)
    
    def __str__(self):
        return f"{self.user_second_name}, {self.user_name}, {self.user_group}"
    
    def answers_list(self):
        answers = Answers.objects.filter(userInfo=self)
        return [(answer.user_answer, answer.id_questions) for answer in answers]
    class Meta:
        verbose_name = 'Ответы пользователей'
        verbose_name_plural = 'Ответы пользователей'

class Test(models.Model):
    id_test = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name
        
class Questions(models.Model):
    id_question = models.AutoField(primary_key=True)
    id_test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.question_text
    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'
        
class Answers(models.Model):    
    id_ans = models.AutoField(primary_key=True)
    id_questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
    userInfo = models.ForeignKey(UserPersonalInfo, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=45)
    
    def __str__(self):
        return self.user_answer
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = verbose_name