import SMRCBuilder

client = SMRCBuilder.Comms.comms("127.0.0.1", 8080)
client.setgroup("Client")
client.client.connect()
while True:
    recv = client.client.recvmsg()
    print(recv)