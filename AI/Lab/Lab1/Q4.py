while True:
    print("Menu\n1. Add two numbers\n2. Subtract two numbers\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice==3:
        break
    else:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        if choice==1:
            print("Result: ", num1+num2)
        elif choice==2:
            print("Result: ", num1-num2)
