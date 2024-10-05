import socket

# nc -u 192.168.0.140 5060
localIP = "192.168.0.140"
localPort = 5060
bufferSize = 1024

# message to send back to the client
# msgFromServer = "Hello UDP Client\n"

msgFromServer = (
    "INVITE sip:T6@192.168.0.140:5060 SIP/2.0\r\n"
    "Priority: normal\r\n"
    "Via: SIP/2.0/UDP 192.168.0.140:5060;branch=z9hG4bK_BuDO6T9YqXtm\r\n"
    "From: S4 <sip:S4@192.168.0.140>;tag=F3928516\r\n"
    "To: <sip:T6@192.168.0.140>\r\n"
    "Call-ID: 5e119ab8-0092-79c9-f742-e4f97850b03a\r\n"
    "CSeq: 2 INVITE\r\n"
    "Allow: INVITE, ACK, CANCEL, BYE, OPTIONS\r\n"
    "Contact: <sip:S4@192.168.0.140:5060>\r\n"
    "Max-Forwards: 70\r\n"
    "User-Agent: PAS Radio\r\n"
    "WG67-Version: radio.01;radio.02\r\n"
    "Subject: radio\r\n"
    "Supported: \r\n"
    "Content-Type: application/sdp\r\n"
    "Content-Length: 332\r\n"
    "\r\n"
    "v=0\r\n"
    "o=S4 0 1 IN IP4 192.168.0.140\r\n"
    "s=Radio Session\r\n"
    "c=IN IP4 192.168.0.140\r\n"
    "t=0 0\r\n"
    "m=audio 5002/1 RTP/AVP 123 8\r\n"
    "a=rtphe:1\r\n"
    "a=sendrecv\r\n"
    "a=rtpmap:123 R2S/8000\r\n"
    "a=rtpmap:8 PCMA/8000\r\n"
    "a=type:Radio-TxRx\r\n"
    "a=txrxmode:TxRx\r\n"
    "a=bss:RSSI\r\n"
    "a=sigtime:1\r\n"
    "a=ptt_rep:2\r\n"
    "a=R2S-KeepAlivePeriod:200\r\n"
    "a=R2S-KeepAliveMultiplier:10\r\n"
    "a=PAS-UA:S4.01\r\n"
)
bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]

    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message.decode())
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)

# import socket

# # Define the SIP INVITE message
# message = (
#     "INVITE sip:T6@192.168.0.140:5060 SIP/2.0\r\n"
#     "Priority: normal\r\n"
#     "Via: SIP/2.0/UDP 192.168.0.140:5060;branch=z9hG4bK_BuDO6T9YqXtm\r\n"
#     "From: S4 <sip:S4@192.168.0.140>;tag=F3928516\r\n"
#     "To: <sip:T6@192.168.0.140>\r\n"
#     "Call-ID: 5e119ab8-0092-79c9-f742-e4f97850b03a\r\n"
#     "CSeq: 2 INVITE\r\n"
#     "Allow: INVITE, ACK, CANCEL, BYE, OPTIONS\r\n"
#     "Contact: <sip:S4@192.168.0.140:5060>\r\n"
#     "Max-Forwards: 70\r\n"
#     "User-Agent: PAS Radio\r\n"
#     "WG67-Version: radio.01;radio.02\r\n"
#     "Subject: radio\r\n"
#     "Supported: \r\n"
#     "Content-Type: application/sdp\r\n"
#     "Content-Length: 332\r\n"
#     "\r\n"
#     "v=0\r\n"
#     "o=S4 0 1 IN IP4 192.168.0.140\r\n"
#     "s=Radio Session\r\n"
#     "c=IN IP4 192.168.0.140\r\n"
#     "t=0 0\r\n"
#     "m=audio 5002/1 RTP/AVP 123 8\r\n"
#     "a=rtphe:1\r\n"
#     "a=sendrecv\r\n"
#     "a=rtpmap:123 R2S/8000\r\n"
#     "a=rtpmap:8 PCMA/8000\r\n"
#     "a=type:Radio-TxRx\r\n"
#     "a=txrxmode:TxRx\r\n"
#     "a=bss:RSSI\r\n"
#     "a=sigtime:1\r\n"
#     "a=ptt_rep:2\r\n"
#     "a=R2S-KeepAlivePeriod:200\r\n"
#     "a=R2S-KeepAliveMultiplier:10\r\n"
#     "a=PAS-UA:S4.01\r\n"
# )

# # Destination IP and port
# dest_ip = "192.168.0.140"
# dest_port = 5060

# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # Send the message
# sock.sendto(message.encode(), (dest_ip, dest_port))

# # Close the socket
# sock.close()

# print("UDP message sent successfully")


