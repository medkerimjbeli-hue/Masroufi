from adding_expence import add_exp
from show_expences import show_exp
from searche_expense import search_exp
from sum_expense import sum_exp
from clear_expenses import clear_exp
op = False
while not op: 
    print("""
##     ##    ###     ######  ########   #######  ##     ## ######## ####
###   ###   ## ##   ##    ## ##     ## ##     ## ##     ## ##        ##
#### ####  ##   ##  ##       ##     ## ##     ## ##     ## ##        ##
## ### ## ##     ##  ######  ########  ##     ## ##     ## ######    ##
##     ## #########       ## ##   ##   ##     ## ##     ## ##        ##
##     ## ##     ## ##    ## ##    ##  ##     ## ##     ## ##        ##
##     ## ##     ##  ######  ##     ##  #######   #######  ##       ####
""")
    print("1.Add expense")
    print("2.View expenses")
    print("3.Search expense by date")
    print("4.View total expenses")
    print("5.Clear all expenses")
    print("6.Exit")
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("INVALID INPUT! ENTER A NUMBER.")
        continue
    if (choice not in [1,2,3,4,5,6]):
        print("OPTION INVALID!")
        continue
    match choice:
        case 1:
            add_exp()
        case 2:
            show_exp()
        case 3:
            search_exp()
        case 4:
            sum_exp()
        case 5:
            clear_exp()
        case 6:
            op = True
        