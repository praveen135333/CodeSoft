def calculator():
    var1 = int(input("Enter the first variable: "))
    var2 = int(input("Enter the second variable: "))
    while True: 
        print("------->Enter operation you want to perform:\n1.Add\n2.Subtract\n3.Multiply\n4.Division\n5.Exit")
        operation = int(input("Enter the choice: "))
        if operation == 1:
            result = var1+var2
            print(f"Addition of {var1} and {var2} is {result}.")
        elif operation == 2:
            if var1>=var2:
                result = var1-var2
            else:
                result = var2 - var1
            print(f"Difference of {var1} and {var2} is {result}.")
        elif operation == 3:
            result = var1*var2
            print(f"Multiplication of {var1} and {var2} is {result}.")
        elif operation == 4:
            result = var1/var2
            print(f"Division of {var1} and {var2} is {result}.")
        elif operation == 5:
            print("thanks for using calculator")
            return
        else:
            print("wrong choice.. Please Start Again.")
calculator()