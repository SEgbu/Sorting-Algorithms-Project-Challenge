import random
import time

size = int(input("Random list size: "))

# List of random integers
arr = random.sample(range(0, size), size)
print("The random list: %s \n" %str(arr))

choice = input("Bubble or insertion (b or i): ")

if choice == "i":
    # Insertion sort
    sorted = [arr[0]] # The final sorted list
    insertionSorting = True

    # Start timer
    insertionSortStartTime = time.time()

    while insertionSorting == True:
        for i in range(len(arr)):
            if i == 0:
                continue
            if i > 0:
                sorted.append(arr[i])
                sortedI = len(sorted) - 1
                while sortedI > 0:
                    if sorted[sortedI] < sorted[sortedI - 1]:
                        sorted[sortedI], sorted[sortedI - 1] = sorted[sortedI - 1], sorted[sortedI]
                        sortedI -= 1
                    else: 
                        sortedI -= 1
                        continue
        
        insertionSorting = False

    print("The time elasped of insertion sort: " + str(time.time() - insertionSortStartTime ) + "\n")
    print("Sorted using insertion sort: %s" %sorted)

elif choice == "b":
    # Bubble sort
    bubbleSorting = True

    bubbleSortStartTime = time.time()

    while bubbleSorting == True:
        for loopi in range(len(arr)):
            for i in range(len(arr) - 1): # Iterate through unsorted list
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    continue
                elif arr[i] <= arr[i + 1]:
                    continue
        # Stop sorting
        bubbleSorting = False

    print ("Sorted using bubble sort: %s \n" %str(arr))
    print ("The time elasped of bubble sort: " + str(time.time() - bubbleSortStartTime))
else: 
    print("invalid choice")
    