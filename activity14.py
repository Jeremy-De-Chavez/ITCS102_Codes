age = int(input("what is your age? "))
is_employed = bool(input("are you employ? "))
credit_score = int(input("credit score ---> "))
annual_income = float(input("annual income --> "))
has_collateral = bool(input("do you have any collateral? "))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("accept")
    if credit_score >= 750:
        print("base interest rate: 5.0% ")
        if annual_income >= 100000:
            print("you have high annual salary")
            base_rate = 4.5
            print("your base rate is",base_rate)
        else:
            base_rate = 5.0
            print("your base rate is", base_rate)       
    elif credit_score <= 600 and credit_score > 750:
        print("your credit score is less than 750") 
        if has_collateral == True:
            print("you have collateral")
            base_rate = 7.0
            print("your base rate is",base_rate) 
    elif annual_income < 40000:
        print("low annual income")
        base_rate = 9.5
    elif credit_score < 600:
        print("Rejected: Credit score too low")
else:
    print("Rejected: Fails baseline criteria ")


