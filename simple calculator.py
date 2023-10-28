val1 = int(input("Enter the First Value:  "))
val2 = int(input("Enter the Second Value:  "))
operator = input("Enter operation you want ")

if operator == "+" :
  add = val1 + val2
  print("Result for Addition is ",add)
if operator == "-" :
  subtract = val1 - val2
  print("Result for Subtraction is ",subtract)
if operator == "*" :
  multiply = val1 * val2
  print("Result for Multiplication is ",multiply)
if operator == "/" :
  divide = val1 / val2
  print("Result for Division is ",divide)