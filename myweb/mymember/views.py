from django.shortcuts import render, redirect
from mymember.models import Member
import hashlib

#       비연결성
#       세션, 쿠키
#       서버 클라이언트

def home(request):
    if 'userid' not in request.session.keys():
#       변수명                    세션
        return render(request, 'mymember/login.html')
    else:
        return render(request, 'mymember/main.html')

def login(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        passwd = request.POST['passwd']
        passwd = hashlib.sha256(passwd.encode()).hexdigest()
#                        비번 암호화
        row = Member.objects.filter(userid=userid, passwd=passwd)
#                               검색
        if len(row)>0:     # 로그인 성공
            row = Member.objects.filter(userid=userid, passwd=passwd)[0]
            request.session['userid'] = userid  # 세션에 등록
            request.session['name'] = row.name
            return render(request, 'mymember/main.html')
        else:                   # 로그인 실패
            return render(request, 'mymember/login.html',
                          {'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})   # 로그인 화면
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
#                 세션    [key]
        return render(request, 'mymember/main.html')
    else:
        return render(request, 'mymember/join.html')    # 회원가입 양식

def logout(request):
    request.session.clear()     # 세션 초기화
    return redirect('/mymember')    # 메인 페이지