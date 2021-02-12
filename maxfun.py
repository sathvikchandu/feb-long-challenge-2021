n = int(input())
for i in range(n):
    t = int(input())
    l = list(map(int,input().split()))
    su=0
    l.sort()
    le= len(l)-1
    a = l[0]
    b = l[1]
    c = l[le]
    su = 0
    su = su+abs(a-b)
    su = su+abs(b-c)
    su = su+abs(c-a)
    print(su)
