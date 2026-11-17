loan = float(input(" Enter amount: "))
years = int(input(" Enter years: "))

month = years * 12
principal = loan / month
rem_bal = loan
print("|MONTH\t| MONTHLY PAYMENT\t|INTEREST| \t PRINCIPLE| \tREMAINING LOAN|")
for x in range(1,month + 1):
    rem_bal -= principal
    loani = rem_bal * 0.00256
    monthp = loani + principal
    print(f"|{x} \t|\t{round(monthp,2)}\t\t|\t{round(loani, 2)}\t|\t{round(principal, 2)}\t|\t{round(rem_bal,2)}|")