def cd(N):
    c=0
    for i in range(1,N+1):
        if i%3==0 or i%5==0:
            c+=1
    return c
N=int(input().strip())
res=cd(N)
