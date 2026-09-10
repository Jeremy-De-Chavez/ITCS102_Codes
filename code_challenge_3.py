name = input("What is your name? ")
item = input("What type of item? ")
is_fragile = input("Is it fragile?(True/False): ")
weight = float(input("weight (kg): "))
distance = float(input("distance (km): "))
is_express = input("Is it express?(True/False) ")
if is_express == "True" or is_express == "Yes" or is_express == "yes" or is_express == "true":
	is_express = True
else:
	is_express = False

is_international = input("Is it international?(True/False) ")

if is_international == "True" or is_international == "Yes" or is_international == "yes" or is_international == "true":
	is_international = True
else:
	is_international = False

base_cost = (weight * 2.5) + (distance * 0.15)

if is_express == True and is_international == True:
	total = (base_cost * 1.40) + 50

if is_express == "True" or is_international == "True" and weight > 20:
	total = (base_cost * 1.20) + 25

if weight > 30 or distance > 100:
	total = base_cost + 30
else:
	total = base_cost

print("\n\n")
print("---> SHIPPING RECIETP <---")
print("| name ->",name)
print("| item ->",item)
print("| Fragile ->", is_fragile)
print("| Weight ->",weight, "kg")
print("| Distance ->",distance, "km")
print("| Express ->", is_express)
print("| International ->", is_international)
print("|_________________________")
print("| Total fare ->",base_cost)