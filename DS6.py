def heapify(arr, n, i):
    """
    Maintain the max heap property for a subtree rooted at index i.
    n is the size of the heap.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child of root exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed, and continue heapifying the affected sub-tree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heapSort(arr):
    """Sorts an array using the Heap Sort algorithm."""
    n = len(arr)

    # Step 1: Build a Max Heap (rearrange array)
    # Start from the last non-leaf node and move up to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move the current root (maximum element) to the end of the unsorted segment
        arr[0], arr[i] = arr[i], arr[0]
        
        # Call max heapify on the reduced heap
        heapify(arr, i, 0)


# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            arr = []
            for i in range(n):
                x = int(input(f"Enter element {i + 1}: "))
                arr.append(x)

            print("\nOriginal Array:")
            print(arr)

            heapSort(arr)

            print("\nSorted Array:")
            print(arr)
            
    except ValueError:
        print("Invalid Input! Please enter integers only.")
