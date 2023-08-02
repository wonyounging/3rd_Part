# 챗봇 소켓통신 서버

import threading
import json

from chatbot.db.DatabaseConfig import *
from chatbot.db.Database import Database
from chatbot.server.BotServer import BotServer
from chatbot.Preprocess2 import Preprocess2
from chatbot.IntentModel import IntentModel
from chatbot.NerModel import NerModel
from chatbot.FindAnswer import FindAnswer

# 전처리 객체 생성
p = Preprocess2(word2index_dic='c:/workspace3/FoodShop/data/chatbot_dict.bin',
               userdic='c:/workspace3/FoodShop/data/user_dic.tsv')

# 의도 파악 모델
intent = IntentModel(model_name='c:/workspace3/FoodShop/model/intent_model.h5', proprocess=p)

# 개체명 인식 모델
ner = NerModel(model_name='c:/workspace3/FoodShop/model/ner_model.h5', proprocess=p)

def to_client(conn, addr, params):
    db = params['db']
    try:
        db.connect()  # 디비 연결
        # 데이터 수신
        read = conn.recv(2048)  # 수신 데이터가 있을 때 까지 블로킹
#              클라이언트 메시지 수신
        print('===========================')
        print('Connection from: %s' % str(addr))

        if read is None or not read:
            # 클라이언트 연결이 끊어지거나, 오류가 있는 경우
            print('클라이언트 연결 끊어짐')
            exit(0)

        # json 데이터로 변환
        recv_json_data = json.loads(read.decode())

#               클라이언트       ==>     서버
#               원문 => 인코딩           디코딩 => 원문

        print("데이터 수신 : ", recv_json_data)
        query = recv_json_data['Query']
#                         질문 내용

        # 의도 파악
        intent_predict = intent.predict_class(query)
        intent_name = intent.labels[intent_predict]

        # 개체명 파악
        ner_predicts = ner.predict(query)
        ner_tags = ner.predict_tags(query)

        # 답변 검색
        try:
            f = FindAnswer(db)
            answer_text, answer_image = f.search(intent_name, ner_tags)
            answer = f.tag_to_word(ner_predicts, answer_text)

        except:
            answer = "죄송합니다. 질문하신 내용을 이해하지 못했습니다."
            answer_image = None

        send_json_data_str = {
            "Query": query,
            "Answer": answer,
            "AnswerImageUrl": answer_image,
            "Intent": intent_name,
            "NER": str(ner_predicts)
        }

        message = json.dumps(send_json_data_str)

        conn.send(message.encode())

    except Exception as ex:
        print(ex)

    finally:
        if db is not None: # db 연결 끊기
            db.close()
        conn.close()

if __name__ == '__main__':
    # 질문/답변 학습 디비 연결 객체 생성
    db = Database(
        host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db_name=DB_NAME
    )

    print("DB 접속")

    port = 5050
    listen = 100

    # 봇 서버 동작
    bot = BotServer(port, listen)
    bot.create_sock()
    print("bot start")

    while True:
        conn, addr = bot.ready_for_client()
#                        클라이언트 접속 대기
        params = {
            "db": db
        }

        client = threading.Thread(target=to_client, args=(
#                멀티스래드              함수
            conn,
            addr,
            params
        ))

        client.start()  # 스레드 시작