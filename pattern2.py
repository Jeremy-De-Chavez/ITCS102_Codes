for i in range(5):
    for o in range(5):
        if i == 0 or i == 4 or i+o == 4:
            print("*", end= "")
        else:
            print(" ", end= "")
    print()
