import random

# List of random integers
arr = random.sample(range(0, 10), 10)
print("The random list: %s" %str(arr))

# Insertion sort
sorted = [arr[0]] # The final sorted list
sorting = True

while sorting == True:
    for i in arr:
        if i == 0:
            continue
        if i > 0:
            sorted.append(arr[i])
            for sortedI in range(len(sorted)):
                if sorted[sortedI] > sorted[sortedI - 1]:
                    sorted[sortedI], sorted[sortedI - 1] = sorted[sortedI - 1], sorted[sortedI]
                else: 
                    continue



print("Sorted using insertion sort: %s" %sorted)
    


