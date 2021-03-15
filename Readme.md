# SmartRC - Builder Library

A Library To Help Build Interfaces For Hardware Systems

The builder library is broken down into separate modules.

Communications
Input
Logs

This library is currently in development.
More modules will be added later.

## Install

```terminal
pip install SMRCBuilder
```
or
```
python3 -m pip install SMRCBuilder
```

## Communications Module

Like the regular socket module, you will need 2
Python files. One for the client, and the other for the server.

Here is how to host a socket connection

```python
#First, you import the variable
#We will only import the Comms Library
from SMRCBuilder import Comms

#Then, you will need to define a variable
#You need to pass in 2 arguments
#The IP address, and port
#For now, we will use the localhost ip
myserver = Comms.comms("127.0.0.1", 8080)

#Now, you need to declare the type
#It can only be "Server" Or "Client"
myserver.setgroup("Server")

#Now you can start the connection
myserver.server.start()

#Here is how to send a message
#There are 2 arguments you can to pass in
#The message is required
#If you want to, you can leave the encoding blank
#The program will default to utf8
myserver.server.sendmsg()
```