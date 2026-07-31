import math
history = []
while True:
    try:
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         while True:
            operator = input("Enter Operator (+,-,/,*,^,%,avg): ")
            if operator == "+":
                print("The addition is = ", num1 + num2)
                history.append(f"\tAddition of {num1} and {num2} is {num1 + num2}")
                break
            elif operator == "-":
                print("The subtraction is = ", num1 - num2)
                history.append(f"\tSubtraction of {num1} and {num2} is {num1 - num2}")
                break
            elif operator == "/":
                if num2 == 0:
                    print("Division by zero is invalid.")
                    
                else:
                    print("The divide is = ", num1 / num2)
                    history.append(f"\tDivision to {num1} by {num2} is {num1 / num2}")
                    break
            elif operator == "*":
                print("The multiply is = ", num1 * num2)
                history.append(f"\tMultiplication of {num1} and {num2} is {num1 * num2}")
                break
            elif operator == "^":
                print("The power is = ", num1 ** num2)
                history.append(f"\tThe power {num2} of the number {num1} is {num1 ** num2}")
                break
            elif operator == "%":
                if num2 == 0:
                    print("Division by zero is invalid.")    
                else:
                    print("The remainder is = ", num1 % num2)
                    history.append(f"\tThe remainder of {num1} by {num2} is {num1 % num2}")
                    break
            elif operator == "avg":
                print("The average is = ", (num1 + num2) / 2)
                history.append(f"\tThe average of {num1} and {num2} is {(num1 + num2) / 2}")
                break
            else:
                print("Invalid Operator")
         while True:
            choice = input("Continue? yes/no/history/sqrt: ").lower()
            if choice == "no":
              break  
            elif choice == "yes":
               break
            elif choice == "history":
                for h in history:
                    print(h)
            elif choice == "sqrt":
                num3 = float(input("Enter number "))
                if num3 < 0:
                    print("Square root of a negative number is impossible.")
                else:
                    print(f"The square root is ", math.sqrt(num3))    
                    history.append(f"\tThe square root of number {num3} is {math.sqrt(num3)}")
            else:
               print("only type 'yes' or 'no'")  
         if choice == "no":
             print("Thank you for using this calculator.")
             break  
           
    except ValueError:
        print("no string value allowed!")
        continue
    except TypeError:
        print("You type something wrong!")
        continue
    except ZeroDivisionError:
        print("Division by zero is not allowed!")
    except OverflowError:
        print("Sorry! number is too big to be dislay.")   
        continue
