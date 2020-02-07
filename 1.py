n = input(" Hoe groot?")
n= int(n)
for i in range(0,n):
    for j in range (0,i+1):
        print("*", end=" ")
    print("\r")
for i in range(n,0,-1 ):
    for o in range(0,i-1):
         print("*", end=" ")
    print("\r")

