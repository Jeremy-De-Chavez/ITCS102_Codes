n = int(input(" what size? --> "))
z = 0
for x in range(n):
    if z != n:
        for y in range(x + 1):
            if z != n:
                z= z+1
                print(z, end =" ")
            elif z == n:
                print(" ", end = " ")
        print(" ")
