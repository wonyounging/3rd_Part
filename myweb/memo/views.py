from django.shortcuts import render, redirect
from memo.models import Memo

def home(request):
    memoList = Memo.objects.order_by("-idx")
    #                       필드명 => 내림차순 정렬
    return render(request, 'memo/list.html', {'memoList': memoList, 'memoCount': len(memoList)})
#               템플릿 생성

def insert_memo(request):
    memo = Memo( writer=request.POST['writer'], memo=request.POST['memo'] )
    memo.save()
    return redirect("/memo")
#       레코드 저장완료, 목록으로

def detail_memo(request):
    row=Memo.objects.get(idx=request.GET['idx'])
    #                           글번호

    return render(request, 'memo/detail.html', {'row': row})
    #               select * from memo_memo where idx=?

def update_memo(request):
    memo = Memo( idx=request.POST['idx'],
                                 writer=request.POST['writer'],
                                 memo=request.POST['memo'] )
    memo.save()
    return redirect("/memo")
#           목록으롤 이동

def delete_memo(request):
    Memo.objects.get(idx=request.POST['idx']).delete()
    #                   삭제할 글번호
    return redirect("/memo")
#               목록으로 이동

#       urls.py         views.py              templates
#       url-function    화면 준비, 데이터 처리    화면 출력