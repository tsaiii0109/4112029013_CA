
import socket

# 建立一個 TCP 客戶端 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 連接到伺服器的 IP 地址和連接埠
server_address = ('localhost', 3000)
client_socket.connect(server_address)

while True:
    # 讓使用者輸入一條訊息
    message = input("請輸入一條訊息 (輸入 'exit' 來終止連接): ")

    # 將訊息發送到伺服器
    client_socket.send(message.encode('utf-8'))

    if message == 'exit':
        break

    # 接收伺服器的回音
    data = client_socket.recv(1024)
    print("伺服器回音：", data.decode('utf-8'))

# 關閉客戶端連接
client_socket.close()