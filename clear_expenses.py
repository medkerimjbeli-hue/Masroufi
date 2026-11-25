def clear_exp():
    with open("expenses.txt", "w") as f:
        f.write("Date|Item|Description|Price\n")

    print("ALL EXPENSES CLEARED!")