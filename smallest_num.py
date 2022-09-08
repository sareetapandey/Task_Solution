arr = [12, 89, 19, 6, 4, 8]
mini = arr[0]

for i in range(len(arr)):
  if arr[i] < mini:
     mini = arr[i]

print ("The smallest num is: " + str(mini))