age = int(input("age --> "))
monthly = float(input('revenue --> '))
cc = int(input(" credit score --> "))
years = float(input(" years in business --> "))
has_defaults = bool(input(" has defaults? True/False --> "))
name = str(input("name of collateral --> "))
value = float(input("collayteral value --> "))

maxloan = 0
feerate = 0


if age >= 21 and years >= 2.0 and has_defaults == False:
    print("pass")
    if cc >=720:#t1
        print("credit score is high")
        maxloan = 3 * monthly
        if monthly >= 50000:
            feerate = 0.015
            print("your fee rate is", feerate)
        else:
            feerate = 0.025
            print("your fee rate is", feerate)

            if value >= maxloan:
                print("your",name,"with the value of",value,"is accepted")
            else:
                print("rejected: insifficient collateral value for",name)

            if value % 5000 != 0:
                feerate += 250
                print(" additinal cahrge added to your fee rate, total fee rate is",feerate)
            else:
                print("collateral value divisible by 5000ss")
            
    elif cc <= 620 and cc < 720:#t2
        print("range of 620 to 720 credit score")
        maxloan = 1.5 * monthly
        if years >= 5.0:
            feerate = 0.02
            print("your fee rate is",feerate)
            feerate = 0.035
        else:
            print("your fee rate is", feerate)
            if cc < 620:
                print("credit score too low")  
            else:
                print("credit score to low")          
else:
    print("not pass")