def recur_factorial(n):
    if n ==1:
        return n
    else:
        return n*recur_factorial(n-1)
    
num = int(input("enter the value"))

if num<0:
    print("sorry, the factorial does not exist for nrgative values")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print(" factorial of", num,"is",recur_factorial(num))