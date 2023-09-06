import socket

# 서버의 IP 주소와 포트 번호 설정
SERVER_HOST = '57.140.60.61'  # 서버의 IP 주소
SERVER_PORT = 443       # 서버의 포트 번호

# 서버에 연결
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# 전송할 파일 이름 설정
file_name = "secret.txt"

# 파일 열기
with open(file_name, "rb") as file:
    # 파일 데이터 읽기
    file_data = file.read()

    # 파일 데이터의 크기를 먼저 서버에 전송
    file_size = len(file_data)
    client_socket.send(str(file_size).encode())

    # 서버로 파일 데이터 전송
    client_socket.sendall(file_data)

# 소켓 연결 종료
client_socket.close()