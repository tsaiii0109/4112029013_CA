
import socket

# 建立一個 TCP 伺服器端 socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 綁定伺服器的 IP 地址和連接埠
server_address = ('localhost', 3000)
server_socket.bind(server_address)

# 監聽客戶端的連接
server_socket.listen(1)
print("等待客戶端連接...")

# 等待客戶端連線
client_socket, client_address = server_socket.accept()
print("已連接到客戶端：", client_address)

while True:
    # 接收從客戶端傳來的資料
    data = client_socket.recv(1024)
    if not data:
        break  # 如果客戶端關閉連接，則停止接收資料

    print("接收到的訊息：", data.decode('utf-8'))

    # 將接收到的資料傳送回客戶端 (Echo)
    client_socket.send(data)

# 關閉伺服器和客戶端的連接
client_socket.close()
server_socket.close()