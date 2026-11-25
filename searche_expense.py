def search_exp():  
    date_ind = input("Give the date under this format DD/MM/YYYY")
    with open("expenses.txt","r") as f :
        for line in f :
            if date_ind.find(line) != -1 :
                print(line)