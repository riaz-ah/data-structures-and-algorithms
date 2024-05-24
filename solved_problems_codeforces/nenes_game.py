

def nene_game_question():
    lst3 = []
    for i in range(len(lst2)):
        if lst2[i] < lst1[0]:
            lst3.append(lst2[i])
        else:
            lst3.append(lst1[0] - 1)
    for i in lst3:
        print(i, end=' ')





t = int(input())

for i in range(t):
    k, q = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    nene_game_question()
