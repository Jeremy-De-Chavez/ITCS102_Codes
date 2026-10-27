n = int(input("what size of your x? --> "))
for x in range(n):
    for y in range(n):

        if x + y == n-1 or x == y:
            print("*", end= " ")
        else:
            print(" ", end = " ")
    print()
        