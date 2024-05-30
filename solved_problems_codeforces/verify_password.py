def verify_password(string):
    sorted_string = ''.join(sorted(string))
    if string == sorted_string:
        print("YES")
    else:
        print("NO")

t= int(input())
for i in range(t):
    n= int(input())
    string= input()
    verify_password(string)