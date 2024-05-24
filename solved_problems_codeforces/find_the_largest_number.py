arr= [int(x) for x in input().split()]


def find_the_largest_num(arr):
    largest_element= arr[0]
    for i in range(len(arr)):
        if arr[i]>largest_element:
            largest_element= arr[i]
    return largest_element

print(find_the_largest_num(arr))


