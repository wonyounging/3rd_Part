import time
from django.db import transaction
from django.shortcuts import render
from transaction.models import Emp

def home(request):
    return render(request, 'transaction/index.html')

@transaction.atomic()       # 트랙잭션 처리(실행도중 오류시 rollback)
def insert(request):
    start = time.time()     # 시작 측정 시작
    Emp.objects.all().delete()      # 모든 레코드 삭제
    for i in range(1, 1001):
        emp = Emp(empno=i, ename='name' + str(i), deptno=i)
        emp.save()
    end = time.time()       # 시간 측정 종료
    runtime = end - start
    cnt = Emp.objects.count()   # 레코드수 카운트
    return render(request, 'transaction/index.html',
                  {'cnt': cnt, 'runtime': f'{runtime:.2f}초'})

def list(request):
    empList = Emp.objects.all().order_by('empno')
    return render(request, 'transaction/list.html', {'empList': empList, 'empCount': len(empList)})