#Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it (e.g. 
#if num = 4, return (4 * 3 * 2 * 1)).

num = int(input("Enter number: "))

factorial = 1

if num < 0:
   print("No negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, (num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

