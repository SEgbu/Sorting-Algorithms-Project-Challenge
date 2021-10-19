## How to record a sort
+ Example
    ```python
    import time

    start_time = time.time()

    list1 = []
    for i in range(n):
        list1.append(random.randint(1, 1000))
        list1.sort()

    print("Execution time sorting : " + str((time.time() - start_time)))
    ```
    > Time returns the time of when the program starts in seconds