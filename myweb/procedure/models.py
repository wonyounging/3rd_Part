from django.db import models
from datetime import datetime

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    # 사번             숫자         기본키
    ename = models.CharField(max_length=50, null=False)
    # 이름
    job = models.CharField(max_length=50, null=False)
    # 직급
    hiredate = models.DateTimeField(default=datetime.now)
    # 입사일자           날짜시간        기본값     현재시각
    sal = models.IntegerField(null=False, default=0)
    # 급여

    def update_sal(self, sal):      # 급여인상
        self.sal = sal