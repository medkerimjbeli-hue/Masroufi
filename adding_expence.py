import os
def add_exp():
    titles = ['Date','Item','Description','Price']
    if not os.path.exists("expenses.txt"):
        with open("expenses.txt", "w") as f:
            f.write("|".join(titles) + "\n")
    print("ENTER THE NEEDED INFORMATION : ")
    date = input("Give the date in this form DD/MM/YYYY : ")
    item = input("Give the item name : ")
    disc = input("Give item description : ")
    price = input("Give the price of the item : ")
    temp = [date,item,disc,price]
    with open("expenses.txt",'a') as f:
        f.write('|'.join(temp)+"\n")    
