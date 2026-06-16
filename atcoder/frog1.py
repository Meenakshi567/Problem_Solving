import sys

n=int(input())

h=list(map(int,sys.stdin.readline().split()))
l=len(h)
k=2

val=[0] * n
if l > 1:
    val[1] = abs(h[1] - h[0])
while  k<l:
   
    val1 =val[k-1]+abs((h[k]-h[k-1]))
   
    val2 =val[k-2]+abs((h[k]-h[k-2]))
     
    if val1<=val2:
        val[k] =val1
    else:
        val[k]=val2
    k=k+1
print(val[l-1])
