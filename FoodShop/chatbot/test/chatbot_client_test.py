import socket
import json

# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서버 IP 주소
port = 5050  # 챗봇 엔진 서버 통신 포트

# 클라이언트 프로그램 시작
while True:
    print("질문 : ")
    query = input()  # 질문 입력
    if(query == "exit"):
        exit(0) # 프로그램 강제 종료
    print("-" * 40)

    # 챗봇 엔진 서버 연결
    mySocket = socket.socket()
    #               접속용 소켓 생성
    mySocket.connect((host, port))
    #                   서버에 접속

#      json    javascript object notation    <data>
#              자바스크립트  객체   표기법                <name>김철수</name>
#                                                     <age>20</age>
#                                                     <tel>02-222-2222</tel>
#                                            </data>
#       xml
#                                            {"data":{"name":"김철수", "age":"20", "tel":"02-222-2222"}}

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotType': "MyService"
    }

    message = json.dumps(json_data)
#                         json으로 변환
    mySocket.send(message.encode())
#           서버에 전달

#           원문 ==> 인코딩 ==> 디코딩
#           한글    바이트배열

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    print("답변 : ")
    print(ret_data['Answer'])
    print(ret_data)
    print(type(ret_data))
    print("\n")

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()