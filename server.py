
# Iporta o módulo socket
from socket import *
import sys # Necessário para encerrar o programa

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket para o servidor

# Bind + listen
serverSocket.bind(('', 8080))     
serverSocket.listen(1)

while True:
    # Estabele a conexão
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        # Recv
        message = connectionSocket.recv(1024).decode()

        filename = message.split()[1]
        f = open(filename[1:], 'r')

        outputdata = f.read()

        # ENvia estado
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Envia o conteúdo do arquivo ao cliente
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        # Fecha a conexão com o cliente
        connectionSocket.close()

    except IOError:
        # Enviar 404
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())

        # Fechar socket do cliente
        connectionSocket.close()

serverSocket.close()
sys.exit() #Encerra o programa