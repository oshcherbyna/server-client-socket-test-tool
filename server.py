import socket

# Ім'я сервера
SERVER_NAME = "MyServer"

def main():
    # Створення сокету
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Прив'язка сокету до адреси та порту
    server_socket.bind(('localhost', 7777)) # ('192.168.1.10', 7777)

    # Почекати на з'єднання
    server_socket.listen(1)
    print("Server started. Listening...")

    while True:
        # Прийняти з'єднання
        client_socket, client_address = server_socket.accept()
        print(f"Client connection: {client_address}")

        # Відправити ім'я сервера клієнту
        client_socket.send(SERVER_NAME.encode())

        # Закрити з'єднання з клієнтом
        client_socket.close()

if __name__ == "__main__":
    main()
