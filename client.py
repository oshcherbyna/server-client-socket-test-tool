import socket

def main():
    # Параметри сервера
    SERVER_ADDRESS = 'localhost' # '192.168.1.10'
    SERVER_PORT = 7777
    print(f"Connection to {SERVER_ADDRESS, SERVER_PORT}...")
    
    # Створення сокету
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Підключення до сервера
        client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
        print(f"Server {SERVER_ADDRESS, SERVER_PORT} - UP")

        # Отримання ім'я сервера
        server_name = client_socket.recv(1024).decode()
        print(f"Get server's name: {server_name}")

    except ConnectionRefusedError:
        print("Error: Cann't connect to server. Check server is running & port is correct.")
    
    except TimeoutError:
        print("Error: Check server firewall rules: netsh firewall show state\n \
            win+r => wf.msc => Inbound rules => New rule => Port.. or \n \
            win+r => cmd => netsh advfirewall firewall add rule name='7777' dir=in action=allow protocol=TCP localport=7777")

    finally:
        # Закриття сокету
        client_socket.close()

if __name__ == "__main__":
    main()
