num1 = input(" Enter first number  ")
num2 = input(" Enter second number  ")
num1 = int(num1)
num2 = int(num2)


print(" enter + for addition\n" , "enter - for substraction" )
print(" enter * for multiplication\n" , "enter / for decimal accurate division" ) 
print(  " enter // for integer division\n"  )
op = input("Enter operation = ")
print(op)
if op == "+" :
    print(num1+num2)
elif op == "-" :
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/" :
    print(num1/num2)
elif op == "//":
    print(num1//num2)
else:
    print('Operator does not exists')
