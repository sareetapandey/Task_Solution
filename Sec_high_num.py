list1 = [9, 36, 18, 1, 39, 5, 64, 76, 10]


list2 = list(set(list1))


list2.sort()


print("Second largest element is:", list2[-2])
