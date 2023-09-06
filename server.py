import socket

# 호스트와 포트 번호 설정
HOST = '0.0.0.0'  # 서버의 IP 주소
PORT = 443       # 사용할 포트 번호

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 호스트와 포트에 바인딩
server_socket.bind((HOST, PORT))

# 클라이언트의 연결을 기다림
server_socket.listen()

print(f"서버가 {HOST}:{PORT}에서 대기 중입니다...")

while True:
    # 클라이언트의 연결 요청 수락
    client_socket, addr = server_socket.accept()
    print(f"{addr}에서 연결됨")

    # 클라이언트로부터 데이터 받기
    data = client_socket.recv(1024)  # 최대 1024바이트 데이터 받기
    if not data:
        break

    # 받은 데이터 출력
    print(f"수신된 데이터: {data.decode('utf-8')}")

    # 클라이언트에게 데이터 다시 보내기 (예: 에코 서버)
    client_socket.send(data)

# 소켓 연결 종료
client_socket.close()

# 서버 소켓 닫기
server_socket.close()