import random

# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def search(arr, n, x):
    operations = 0
    for i in range(0, n):
        operations += 1
        if arr[i] == x:
            return i
        return -1

def binary_search(arr, left, right, x):
    operations = 0
    while left <= right:
        operations += 1
        mid = left + (right - left) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1

        # If x is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


if __name__ == "__main__":

    # Driver Code
    arr_ay = [random.randint(0, 200) for r in range(0, 200)]
    sorted_array = sorted(arr_ay)
    print(sorted_array)

    #needle selection randomly from the array
    needle = random.choice(sorted_array)
    print("The selected needle value is:", needle)

import timeit

iterations = 10
ltime = timeit.timeit(lambda: search(arr_ay, len(arr_ay), needle),
                      setup="from __main__ import search", number=iterations)
btime = timeit.timeit(lambda: binary_search(arr_ay, 0,  len(arr_ay), needle),
                      setup="from __main__ import search", number=iterations)

print("linear search time:", ltime)
print("binary search time:", btime)

