def show_exp():
    with open("expenses.txt","r") as f:
        for line in f:
            print(line)