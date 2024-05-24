def inhabitant_of_the_deep_sea(n,k,lst):
    count1=0
    count2=0
    sum1=0
    sum2=0
    if sum(lst) <= k:
        return n
    elif k % 2 == 1:

        for i in range(n):
            sum1 = sum1 + lst[i]
            if sum1 <= (k // 2) + 1:
                count1 += 1
            else:
                break

        for i in range(n - 1, -1, -1):
            sum2 = sum2 + lst[i]
            if sum2 <= k // 2:
                count2 += 1
            else:
                break

    else:

        for i in range(n):
            sum1 = sum1 + lst[i]
            if sum1 <= (k // 2):
                count1 += 1
            else:
                break

        for i in range(n - 1, -1, -1):
            sum2 = sum2 + lst[i]
            if sum2 <= k // 2:
                count2 += 1
            else:
                break
    return count1+count2


t=int(input())

for _ in range(t):
    n, k=map(int, input().split())
    lst=list(map(int, input().split()))
    print(inhabitant_of_the_deep_sea(n,k,lst))