import socket
import threading

HOST = '0.0.0.0'
PORT = 8080

clients = []

def broadcast(date, exclude_socket=None):
    for client in clients:
        if client != exclude_socket:
            try:
                client.sendall(date)
            except:
                pass

def handle_client(client_socket):
    while True:
        try:
            date = client_socket.recv(4096)
            if not date:
                break
            broadcast(date, exclude_socket=client_socket)
        except:
            break
    if client_socket in clients:
        clients.remove(client_socket)
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREA)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Сервер запущено на якомусь {HOST}:{PORT}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Підключився ще якись тіп: {addr}")
        clients_append(client_socket)

        t = threading.Thread(target=handle_client, args=(client_socket))
        t.start()
main()