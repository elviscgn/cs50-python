while True:
    try:
        X, Y = input("Fraction: ").split("/")
        X, Y = int(X), int(Y)
        percentage = X/Y

        if X > Y or Y == 0:
            continue
        elif X < 0 or Y < 0:
            continue
        elif percentage >= .99:
            print("F")
            break
        elif percentage <= 0.01:
            print("E")
            break
        else:
            print(f"{int(round(percentage,2)*100)}%")
            break

    except ValueError:
        continue
    except ZeroDivisionError:
        print("cant divide by 0")
