import math 
print("CASIO SIMPLE CALCULATOR")
num1 = input ("Enter a number ")
num2 = input ("Enter a number ")
print("Choose an operation (+,-,/,,*,%,√) ")
operation = input ("Enter an operation  ")
if operation == "+" :
    result = float(num1) + float(num2)
    print("results", result)
elif operation == "-":
    result = float(num1) - float(num2)
    print("result:", result)
elif operation == "*":
    result = float(num1) * float(num2)
    print("result:", result)
elif operation == "":
    result = float(num1) ** float(num2)
    print("Results: ", result)
elif operation == "%":
    result = float(num1) % float(num2)
    print("Results: ", result)
elif operation == "√":
     result = math.sqrt(float(num1))
     print("Results:"  , result)
     another= input(" do you want to input another number for square root? (YES/NO:"  )
     if another.upper()  == "YES":
         another = float (input ("Enter another number:  "))
         result= math.sqrt(another)
         print("Results:  ", result)  
elif operation == "/":
        if num2 != 0 :
          result = float(num1)/float(num2)
else:
      result = ("Error! , CAN'T DIVIDE bY ZERO")
print("RESULTS:  ", result)