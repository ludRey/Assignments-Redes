from socket import *
import ssl
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

msg_text = "I love computer networks!"

# Create a MIME object for the message
msg = MIMEMultipart()
msg.attach(MIMEText(msg_text))

#Image path
image_path = 'carita.jpg'
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
    image = MIMEImage(image_data, name='carita.jpg')
    msg.attach(image)

endmsg = "\r\n.\r\n"

mailserver = 'smtp.gmail.com'
mailserver_port = 587
username = 'twipzcuba@gmail.com'
password = 'uufs ndnb ijxh fckt'

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailserver_port))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

ehloCommand = 'EHLO Alice\r\n'
clientSocket.send(ehloCommand.encode())
recv_ehlo = clientSocket.recv(1024).decode()
print(recv_ehlo)
if recv_ehlo[:3] != '250':
    print('250 reply not received after EHLO command.')

starttlsCommand = 'STARTTLS\r\n'
clientSocket.send(starttlsCommand.encode())
recv_starttls = clientSocket.recv(1024).decode()
print(recv_starttls)
if recv_starttls[:3] != '220':
    print('220 reply not received after STARTTLS command.')

context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname=mailserver)

ehloCommand = 'EHLO Alice\r\n'
clientSocket.send(ehloCommand.encode())
recv_ehlo_tls = clientSocket.recv(1024).decode()
print(recv_ehlo_tls)
if recv_ehlo_tls[:3] != '250':
    print('250 reply not received after EHLO command (TLS).')

authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(authCommand.encode())
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)
if recv_auth[:3] != '334':
    print('334 reply not received after AUTH LOGIN command.')

# Send the base64-encoded username
clientSocket.send(base64.b64encode(username.encode()) + b'\r\n')
recv_username = clientSocket.recv(1024).decode()
print(recv_username)
if recv_username[:3] != '334':
    print('334 reply not received after sending username.')

# Send the base64-encoded password
clientSocket.send(base64.b64encode(password.encode()) + b'\r\n')
recv_password = clientSocket.recv(1024).decode()
print(recv_password)
if recv_password[:3] != '235':
    print('235 reply not received after sending password. Authentication failed.')

# Send MAIL FROM command and print server response.
mailFromCommand = f'MAIL FROM: <{username}>\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptToCommand = 'RCPT TO: <kristenludd9802@gmail.com>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')

# Send the MIME-formatted message
clientSocket.send(msg.as_bytes())

clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')

clientSocket.close()
