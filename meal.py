def main():

    time = input("What time is it? ")
    hours, minutes = time.split(":")

    if minutes == 30.0:
        minutes == 0.5

    print(convert(hours, minutes))

def convert(x,y):
    x = float(x)
    y = float(y)

    return x,y

if __name__ == "__main__":
    main()