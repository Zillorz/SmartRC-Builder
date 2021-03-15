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

# Server

### Import

We will only import the Comms Library

```python
from SMRCBuilder import Comms
```

Then, you will need to define a variable

You need to pass in 2 arguments

The IP address, and port

For now, we will use the localhost ip

```python
myserver = Comms.comms("127.0.0.1", 8080)
```

### Declare The Type

It can only be "Server" Or "Client"

```python
myserver.setgroup("Server")
```

### Start The Connection

```python
myserver.server.start()
```

### Sending A Message

There are 2 arguments you can to pass in

The message is required

If you want to, you can leave the encoding blank

The program will default to utf8

You DO NOT need to include `bytes()`

```python
myserver.server.sendmsg("Hello World!")
```

### Recieving A Message
Like the sendmsg function, there are 2 parameters you can pass in

The default buffer size is 1024 bytes

And the default encoding is utf8

```python
buffer = 1024 #Default
encoding = "utf8" #Default
recv = myserver.server.recvmsg(buffer, encoding)
print(recv)
```
# Client

Like the server, you need to

Define a variable and set the type to "Client"

```python
from SMRCBuilder import Comms
myclient = Comms.comms("127.0.0.1", 8080)
myclient.setgroup("Client")
```

### Attempt Connection
```python
myclient.client.connect()
```

### Sending and Receiving A Message
Like the server, the client class has 2 parameters to pass in

The message (Which is required)

and the encoding (which again, is utf8 by default)

```python
myclient.client.sendmsg("Hello World", "utf8")

recv = myclient.client.recvmsg(1024, "utf8")
print(recv)
```

## Input
This part of the library allows you to detect keyboard and mouse inputs

It is probably best to use this module on another thread or process

The code structure is relatively the same as the Comms module.

# Keyboard

### Defining And Setting The Type

This time, the setgroup argument can only be keyboard or mouse

```python
from SMRCBuilder import Input

keyboard = Input.input_()
keyboard.setgroup("keyboard")
```

### Start The Keyboard Detection
The start method takes 2 parameters

on_press function

and an on_release function

If you don't need to use these, you can leave them blank

```python
def on_press(key):
  print("{0}".format(key))
  
def on_release(key):
  print("{0}".format(key))
  
keyboard.keyboard.start(on_press=on_press, on_release=on_release)
```

# Mouse

### Defining A Variable And Setting Type

```python
from SMRCBuilder import Input

mouse = Input.input_()
mouse.setgroup("Mouse")
```

The start method takes 3 optional parameters

on_move

on_click

and on_scroll

```python
def on_move(x,y):
    print("{0}".format((x,y)))
    
mouse.mouse.start(on_move=on_move)
```
