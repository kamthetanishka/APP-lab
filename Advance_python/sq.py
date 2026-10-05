# Memoization 
memo = {}

def fib(n):
   
    if n in memo:
        print("Fetching from memo/taking stored result")
        return memo[n]
    if n<=1:
        return n
    
    print("Calculating")
    
    memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

print(fib(5))

print("\n-------------------")

memo = {}

def square(n):
   
    if n in memo:
        print("Fetching from memo/taking stored result")
        return memo[n]
    if n<=1:
        return n
    
    print("Calculating")
    
    memo[n] = square(n-1) + square(n-2)
    
    return memo[n]

print(square(5))