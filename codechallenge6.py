s = int(input("what size? ---> "))

x = 1
for k in range (5):
    for o in range (k + 1):
        print(x, end = " ")
        x = x + 1
    print()