
term=10
def Fibonaci(n):
    if n <= 1:
        return n
    else :
         return Fibonaci(n-1) + Fibonaci(n-2)

print("Fibonacci:")
for j in range(term):
    print(Fibonaci(j))




print(Fibonaci(10))