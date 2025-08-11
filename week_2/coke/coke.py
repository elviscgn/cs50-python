due = 50

while due > 0:
    print("Amount Due:", due)
    coin = int(input("Insert coin: "))
    if coin == 25:
        due -= coin
    elif coin == 10:
        due -= coin
    elif coin == 5:
        due -= coin

print("Change owed:", -due)
