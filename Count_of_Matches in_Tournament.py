n = int(input())
m = 0
while(n>0):
    if(n%2 == 0):
        m += n//2
        n = n//2
    else:
        n = n-1
        m += (n//2)+1
        n = n//2
print(int(m))