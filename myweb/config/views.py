from django.shortcuts import render

def home(request):
    #     요청처리객체
    #installed_app에 작성한 첫번째 앱인 address의 index.html 페이지로 출력됨
    return render(request, 'index.html')
#          탬플릿 완성 => index.html 화면 출력