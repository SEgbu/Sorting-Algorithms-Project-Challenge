import random 
import time

# Allow user to input size
size = int(input("Random list size: "))

# List of random integers
arr = random.sample(range(0, size), size)
print("The random list: %s \n" %str(arr))

# Allow user to decide which sort to use
choice = input("Bubble or insertion (b or i): ")

if choice == "i":
    # Insertion sort
    sorted = [arr[0]] # The final sorted list
    insertionSorting = True # Checks if it is sorting 
    insertionSortStartTime = time.time() # Starts timer

    while insertionSorting == True:
        # Loop through the unsorted list 
        for i in range(len(arr)):
            # Skip the first element
            if i == 0:
                continue
            # If it is not the first element
            if i > 0:
                sorted.append(arr[i]) # Add an element from the unsorted list to the sorted list
                # Looping the sorted list from the end to the beginning
                sortedI = len(sorted) - 1 
                while sortedI > 0:
                    if sorted[sortedI] < sorted[sortedI - 1]:
                        sorted[sortedI], sorted[sortedI - 1] = sorted[sortedI - 1], sorted[sortedI] # swap
                        sortedI -= 1
                    else: 
                        sortedI -= 1
                        continue # skip
        # If sort is finished stop sorting
        insertionSorting = False

    print("The time elasped of insertion sort: " + str(time.time() - insertionSortStartTime ) + "\n")
    print("Sorted using insertion sort: %s" %sorted)

elif choice == "b":
    # Bubble sort
    bubbleSorting = True # Checks if still sorting
    bubbleSortStartTime = time.time() # Starts timer

    while bubbleSorting == True:
        # Repeat this for all element in unsorted list
        for loopi in range(len(arr)):
            # Loop through unsorted list
            for i in range(len(arr) - 1): # Iterate through unsorted list
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i] # swap 
                    continue
                elif arr[i] <= arr[i + 1]:
                    continue # skip
        # Stop sorting
        bubbleSorting = False

    print ("Sorted using bubble sort: %s \n" %str(arr))
    print ("The time elasped of bubble sort: " + str(time.time() - bubbleSortStartTime))
else: 
    print("invalid choice") 
    