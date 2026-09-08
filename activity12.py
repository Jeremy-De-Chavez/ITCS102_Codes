import getpass

username = "lamok"
password = 'aysyaka'

u = input("Enter username -->")
p = getpass.getpass("Enter password -->")

if username == u and password == p :
	print("ACCESS GRANTED")
else:
	print("ACCESS DINIED")