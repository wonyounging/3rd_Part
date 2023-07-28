from django.db import models

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    #   사번          정수형
    ename = models.CharField(max_length=50, null=False)
    #   이름          문자형
    deptno = models.IntegerField(null=False)
    #   부서