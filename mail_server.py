from socket import *

# Mensaje a enviar
msg = "\r\nI love computer networks!"
endmsg = "\r\n.\r\n"

# Elegir un servidor de correo (p. ej. servidor de Google) y definirlo como mailserver
mailserver = 'smtp.gmail.com'  # You need to replace 'smtp.example.com' with the actual mail server

# Crear un socket llamado clientSocket y establecer una conexión TCP con el mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))  # El número 25 es el puerto de SMTP

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Enviar el comando HELO y mostrar la respuesta del servidor.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
starttls_command = "STARTTLS\r\n"
clientSocket.send(starttls_command.encode())
recv_tls = clientSocket.recv(1024).decode()
print(recv_tls)

fromaddress = "twipzcuba@gmail.com"  # Replace with the actual email address
toaddress = "kristenludd9802@gmail.com"      # Replace with the actual email address

# Enviar el comando MAIL FROM y mostrar la respuesta del servidor.
mailfromcommand = f"MAIL FROM: <{fromaddress}>\r\n"
clientSocket.send(mailfromcommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Enviar el comando RCPT TO y mostrar la respuesta del servidor.
rcpttocommand = f"RCPT TO: <{toaddress}>\r\n"
clientSocket.send(rcpttocommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Enviar el comando DATA y mostrar la respuesta del servidor.
datacommand = "DATA\r\n"
clientSocket.send(datacommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Enviar datos del mensaje.
clientSocket.send(f"Subject: Testing SMTP Mail Client\r\n{msg}".encode())

# Mensaje termina con un solo punto.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Enviar comando QUIT y obtener la respuesta del servidor.
quitcommand = "QUIT\r\n"
clientSocket.send(quitcommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()
