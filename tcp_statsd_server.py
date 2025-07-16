import socket


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 8125))
    print("Сервер запущен")
    while True:
        data, addr = sock.recvfrom(1024)

        print(f"Recieved from {addr}: {data.decode()}")


if __name__ == "__main__":
    server()
