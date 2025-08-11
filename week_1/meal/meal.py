def main():
    prompt = input("What time is it? ")
    time = convert(prompt)

    # breakfast
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    if 12.0 <= time <= 13.0:
        print("lunch time")
    if 18.0 <= time <= 19.0:
        print("dinner time")

def convert(time):
    time = time.split(":")
    hour = int(time[0])
    minute = int(time[1])*1/60
    return hour + minute


if __name__ == "__main__":
    main()