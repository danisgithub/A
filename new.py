def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
	
n = fact(5)

print(n)