arr = [1, 4, 3, 2, 6, 5]

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -=1

    return arr

print(reverse_array(arr)) 