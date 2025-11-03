day_of_week= input("Enter day of the week: ").lower()
print("You entered:", day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday": #true
    print("I will learn live DevOps")
else: #false
    print("I will practice DevOps")
 
num1 = int(input("Enter first number: "))  #string input -> int Type casting
num2 = int(input("Enter second number: ")) #string input -> int Type casting
   
choice = input("Enter the operation: (Options + , -, * , / , %) ")

if choice == "+":
    sum_of_num = num1 + num2
    print("addition:", sum_of_num)
elif choice == "-":
    diff_of_num = num1 - num2
    print("subtraction:", diff_of_num)
elif choice == "*":
    prod_of_num = num1 * num2
    print("multiplication:", prod_of_num)
elif choice == "/":
    div_of_num = num1 / num2
    print("division:" , div_of_num)
elif choice == "%":
    mod_of_num =num1 % num2
    print("modulus:", mod_of_num)
else:
    print("Invalid choice")