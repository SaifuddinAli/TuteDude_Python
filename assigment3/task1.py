def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i

    return result
m=int(input("Enter a number: "))
print(f"Factorial of {m} is: {factorial(m)}")
