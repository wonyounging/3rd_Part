from django.shortcuts import render, redirect
from shop.models import Member,Chat
import hashlib
from shop.mychatbot import getMessage

def home(request):
    if 'userid' not in request.session.keys():  # 로그아웃 상태
#               포함 X            세션   키 집합
        return render(request, 'shop/login.html')
#               로그인 상태
    else:
        return render(request, 'shop/main.html')

def login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        passwd = request.POST['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest()
        row = Member.objects.filter(userid=userid, passwd=passwd)

        if len(row)>0:
            row = Member.objects.filter(userid=userid, passwd=passwd)[0]
            request.session['userid'] = userid
            request.session['name'] = row.name
            return render(request, 'mymember/main.html')
        else:
            return render(request, 'mymember/login.html',
                          {'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, 'mymember/login.html')

def join(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        passwd = request.POST['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest()
        name = request.POST['name']
        address = request.POST['address']
        tel = request.POST['tel']
        Member(userid=userid, passwd=passwd, name=name, address=address, tel=tel).save()
        request.session['userid'] = userid
        request.session['name'] = name
        return render(request, 'shop/main.html')
    else:
        return render(request, 'shop/join.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def order(request):
    return render(request, 'shop/order.html')

def query(request):
    question = request.GET["question"]
#                       질문
    msg = getMessage(question)
#            {key:value}
    query=msg['Query']
    answer=msg['Answer']
    intent=msg['Intent']
    Chat(userid=request.session['userid'], query=query, intent=intent).save()
    Chat(userid=request.session['userid'], answer=answer, intent=intent).save()
    items=Chat.objects.filter(userid=request.session['userid']).order_by('-idx')
#                                                                         내림차순(-) / 오름차순(+)
    return render(request, 'shop/result.html', {'items':items})

def delete_chat(request):
    Chat.objects.filter(userid=request.session['userid']).delete()
    return redirect('/order')