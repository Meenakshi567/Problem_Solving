s = int(input("Enter number of sushi:"))
t = int(input("Enter number of toppings:"))
s_lst = []
t_lst = []
for i in range(s):
    s_lst.append(int(input("Enter sushi:")))
for i in range(t):
    t_lst.append(int(input("Enter toppings:")))
s_lst.sort()
t_lst.sort()
i,j,count = 0,0,0
while i < len(s_lst) and j < len(t_lst) :
    if t_lst[j] <= 2*s_lst[i]:
        count += 1
        i +=1
        j +=1
        
    else:
        i += 1
print(count)
