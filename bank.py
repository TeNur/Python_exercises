def main():

    x = input("Give a greeting: ").strip()
    x = x.lower()

    print(hello_tester(x))

def hello_tester(greeting):
    if greeting.startswith("hello"):
        return "$0"
    elif greeting.startswith("h"):
        return "$20"
    else:
        return "$100"

main()