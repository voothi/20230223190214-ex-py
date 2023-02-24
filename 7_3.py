# 7.3

def print_name_of_season(month: int):
    if month == 12 or \
            month == 1 or \
            month == 2:
        print("Winter")
    elif month == 3 or \
            month == 4 or \
            month == 5:
        print("Spring")
    elif month == 6 or \
            month == 7 or \
            month == 8:
        print("Summer")
    elif month == 6 or \
            month == 7 or \
            month == 8:
        print("Autumn")
    else:
        print("Please enter a valid month number")


month = int(input("Please enter month number: "))

print_name_of_season(month)
