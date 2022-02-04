def merge_sort(arr):
    if len(arr) <= 1:
        print(f"arr is {arr}")
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]
    print(f"left is {left} and right is {right}, calling merge_sort on them")

    merge_sort(left)
    merge_sort(right)
    print(f"calling merge_two_sorted_lists with left={left}, right={right} and arr={arr}")
    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    print(f"in merge_two_sorted_lists a={a}, b={b}, arr={arr}")
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1

if __name__ == '__main__':
    test_cases = [10, 3, 15, 7, 8, 23, 98, 29]

    merge_sort(test_cases)
    print(test_cases)