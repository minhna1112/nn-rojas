def factorial(n: int):
    if n>1:
        return n*factorial(n-1)
    if n in [0,1]:
        return 1