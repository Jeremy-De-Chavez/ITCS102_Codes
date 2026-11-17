loan = float(input("Enter the loan amount: "))
period = int(input("Enter the loan period in years: "))

print("month")
for i in range(1,25,1):
    print(i)


for i in range(6):
    for o in range(7):
        if (i == 0 and o %3 != 0) or (i == 1 and o %3 == 0) or (i-o == 2) or (i+o == 8):
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print()