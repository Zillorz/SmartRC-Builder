import SMRCBuilder

server = SMRCBuilder.Comms.comms("127.0.0.1", 8080)
server.setgroup("Server")
server.server.start()
server.server.sendmsg("Hello")