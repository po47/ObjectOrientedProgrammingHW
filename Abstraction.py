def calculation():
    print("This is a simple calculator")
    x = int(input("Enter a value"))
    y= int(input("Enter another value"))

    print("Press 1 to add\n Press 2 to subtract")
    option = int(input("--> "))

    def add():
        res = x + y
        print(res)

    def subtract():
        res = x - y
        print(res)

    if (option ==1):
        add()

    elif (option == 2):
        subtract()

calculation()
