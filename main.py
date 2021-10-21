import random

# List of random integers
arr = random.sample(range(0, 10), 10)
print("The random list: %s" %str(arr))

# Bubble sort
sorting = True

while sorting == True:
    for loopi in range(len(arr)):
        for i in range(len(arr) - 1): # Iterate through unsorted list
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                continue
            elif arr[i] <= arr[i + 1]:
                continue

    sorting = False

print ("Sorted using bubble sort: %s" %str(arr))

