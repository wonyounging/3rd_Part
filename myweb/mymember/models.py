from django.db import models

class Member(models.Model):
#     클래스 => 테이블
    userid = models.CharField(max_length=50, null=False, primary_key=True)
#    필드명 = 자료형
    passwd = models.CharField(max_length=500, null=False)
    name = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=True)
    tel = models.CharField(max_length=20, null=True)