from django.shortcuts import redirect, render

#       redirect : 방향 전환, 작업 완료 => 새로운 작업
#       render : 화면(template) 생성

#       urls.py          view.py           templates
#       주소 요청         데이터 준비, 처리    화면

from address.models import Address
def home(request):
#        요청사항 내장객체
    items = Address.objects.order_by("name")
#           테이블   모든 레코드         필드명
    return render(request, 'address/list.html', {'items': items, 'address_count': len(items)})
#          화면으로 이동                              key : value
def write(request):
    return render(request, "address/write.html")
def insert(request):
    addr = Address( name=request.POST['name'], tel=request.POST['tel'], email=request.POST['email'], address=request.POST['address'])
#                                                                                     서버에 보낼때(POST)
    addr.save()
#        레코드 저장
    return redirect("/address")
#          방향 전환 - 목록으로 이동
def detail(request):
    addr=Address.objects.get(idx=request.GET['idx'])
#                        서버에서 읽어올때(GET)
    return render(request, 'address/detail.html', {'addr': addr})
def update(request):
    addr = Address( idx=request.POST['idx'], name=request.POST['name'], tel=request.POST['tel'], email=request.POST['email'], address=request.POST['address'] )
    addr.save()
#        레코드 수정(update)
    return redirect("/address")
def delete(request):
    Address.objects.get(idx=request.POST['idx']).delete()
    return redirect("/address")

#   CRUD (Create / Read / Update / Delete)
