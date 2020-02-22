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

# This is the code or long information that goes on behind the scenes.
# In abstraction the user only sees "Enter a value" and "Enter another value" instead of the long code.
