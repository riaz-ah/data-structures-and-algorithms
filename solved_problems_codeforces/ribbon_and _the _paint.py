def ribbon_and_the_paint(n,m,k):
    if n>m:
        if m>k:
            return "YES"
        else:
            return "NO"
    else:
        if n>k:
            return "YES"
        else:
            return "NO"


t= int(input())

for _ in range(t):
    n,m,k= map(int, input().split())
    print(ribbon_and_the_paint(n,m,k))