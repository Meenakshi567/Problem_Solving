x = int(input("Enter a number:"))
n= x+1
while True:
    is_p = True
    for j in range(2,n):
        if n%j == 0:
            is_p = False
            break
    if is_p:
        print("The next prime number is:",n)
        break
    n +=1
