from flask import Flask, Markup, render_template, request
app = Flask(__name__)
#       플라스크

@app.route('/gugu',methods=['GET'])
#                           get / post
#       url mapping
#       http://localhost/gugu
def main():
    return render_template('gugu/gugu.html')
#           템플릿 => html생성

@app.route('/gugu_result', methods=['POST'])
def gugu_result():
    dan = int(request.form['dan'])
    result=''
    for i in range(1,10):
        result += '{}x{}={}<br>'.format(dan,i,dan*i)
    #html 태그를 인식하게 하는 함수
    result=Markup(result)
    return render_template('gugu/gugu_result.html', result=result)
#                                   변수                  값
#                                 {{변수}}

if __name__ == '__main__':      # 프로그램 시작점
    #threaded를 True로 설정하면 신경망 모형을 불러오는 코드에서 에러가 발생하므로 False로 설정
    app.run(port=8000, threaded=False)  # False -> single / True -> multi
    #       서비스포트   threaded(작업단위), single / multi
    #       0~65535
    #       웹서비스 80
