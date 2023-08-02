from django.db import models

class Member(models.Model):
#   필드명  = 자료형
    userid = models.CharField(max_length=50, null=False, primary_key=True)
    passwd = models.CharField(max_length=500, null=False)
    name = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=False)
    tel = models.CharField(max_length=20, null=True)

class Chat(models.Model):   # 대화내용 저장
#   필드명 = 자료형
    idx = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50, null=False)
    query = models.CharField(max_length=500, null=False)    # 질문
    answer = models.CharField(max_length=1000, null=False)  # 답
    intent = models.CharField(max_length=50, null=False)    # 의도