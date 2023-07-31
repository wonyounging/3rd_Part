from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from konlpy.tag import Okt
import joblib

app = Flask(__name__)

def review_predict(new_sentence):
    model = load_model('C:/workspace3/230731/RNN_model.h5')
#           신경망 모형
    tokenizer = joblib.load('C:/workspace3/230731/tokenizer.h5')
#                      토크나이저
    okt = Okt()
    new_sentence = okt.morphs(new_sentence, stem=True)  # 토큰화
    stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']
    new_sentence = [word for word in new_sentence if not word in stopwords]  # 불용어 제거
    encoded = tokenizer.texts_to_sequences([new_sentence])  # 정수 인코딩
    max_len = 53
    pad_new = pad_sequences(encoded, maxlen=max_len)  # 패딩
    score = float(model.predict(pad_new))  # 예측
    return score

@app.route('/')     # url 패턴
def home():         # 함수
    return render_template('text/index.html')

@app.route('/text_result', methods=['POST'])
def result():
    text = request.form['text']
    score = review_predict(text)
    if (score > 0.5):
        result = f"{score * 100:.2f}% 확률로 긍정 리뷰입니다."
    else:
        result = f"{(1 - score) * 100:.2f}% 확률로 부정 리뷰입니다."
    return render_template('text/result.html', result=result, review=text)
#                                                 변수=값         변수=값

if __name__ == '__main__':
    app.run(port=8888, threaded=False)
    #   플라스크 앱 실행, port=포트번호(0~65535)