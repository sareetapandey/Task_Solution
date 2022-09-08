def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [12, 27, 76, 89, 102]
n = len(arr)
solution = largest(arr, n)
print("Largest in given array ", solution)
