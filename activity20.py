islogin = True

while islogin == True:
    username = input("what is your username? -- ")
    password = input("what is your password? -- ")

    if username == "12345" and password == "54321":
        print("succesful!")
        islogin = False
    else:
        print("wrong username or password")
        islogin = False