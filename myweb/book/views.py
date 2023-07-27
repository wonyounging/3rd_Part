from django.shortcuts import render, redirect
from book.models import Book

def list(request):
    bookList = Book.objects.order_by('-idx') # - : 내림차순, +(/생략) : 오름차순
    return render(request, 'book/list.html', {'bookList': bookList, 'bookCount': len(bookList)})

def write(request):
    return render(request, 'book/write.html')

def insert(request):
    book = Book(title=request.POST['title'], author=request.POST['author'], price=int(request.POST['price']),
                amount=int(request.POST['amount']))
    book.save()     # 레코드 저장 insert
    return redirect('/book')    # 저장완료 => 목록으로 이동

def edit(request):
    row = Book.objects.get(idx=request.GET['idx'])
    return render(request, 'book/edit.html', {'row': row})

def update(request):
    book = Book(idx=request.POST['idx'], title=request.POST['title'], author=request.POST['author'],
                price=int(request.POST['price']), amount=int(request.POST['amount']))
    book.save()
    return redirect('/book')

def delete(request):
    Book.objects.get(idx=request.POST['idx']).delete()
    return redirect('/book')

#   get 방식 : 데이터 요청
#   post 방식 : 데이터 전달