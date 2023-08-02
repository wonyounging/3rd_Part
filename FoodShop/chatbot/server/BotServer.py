#   소켓통신
#   socket 논리적인 회선
#   서버측               클라이언트측
#   server socket       socket
#   ip, port
#   2.2.2.2  5000        2.2.2.2  5000

#                                                               stream(스트림) : 데이터의 흐름
#   접속대기                                     A            B
#   접속화면                                        =======>      보내는 데이터 - 출력 스트림
#   허가                                           <=======      받는 데이터 - 입력 스르림
#   통신                 통신

# 소켓통신 클래스

import socket

class BotServer:
    def __init__(self, srv_port, listen_num):
        self.port = srv_port
        self.listen = listen_num
        self.mySock = None

    # socket 생성
    def create_sock(self):
        self.mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySock.bind(("0.0.0.0", int(self.port)))
#                          0.0.0.0 : 내 컴퓨터의 ip
#                          127.0.0.1
#                          cmd => ipconfig => private ip 외부에서 접속 X

        self.mySock.listen(int(self.listen))
#                   기다리는 상태
        return self.mySock

    # client 대기, 접속 승인
    def ready_for_client(self):
        return self.mySock.accept()

    # socket 반환
    def get_sock(self):
        return self.mySock