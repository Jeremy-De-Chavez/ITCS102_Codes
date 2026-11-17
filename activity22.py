anime_type = ("isekai","adventure","romance","scifi")
anime_title = []

while True:
    ans = input("do you know any anime? ----> (yes/no) ")

    if ans.lower() =='yes':
        print("what item type? pick in the list!")
        for x in anime_type:
            print(x) 

        a_type = input("what type? ---> ")

        title = input("what title? --> ")
        anime_title.append(title)
        continue
    else:
        print("thank you")
        print("so far you have encoded the following")
        break
