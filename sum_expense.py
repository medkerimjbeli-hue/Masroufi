def sum_exp():
    s: float = 0.0

    with open("expenses.txt", "r") as f:
        for line in f:
            price = line.strip().rsplit("|", 1)[-1]

            try:
                s += float(price)
            except ValueError:
                continue

    print("Your total expense is:", s)