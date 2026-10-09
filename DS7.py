def mergeSort(arr):
    """
    Sorts an array in ascending order using the Merge Sort algorithm.
    It recursively divides the array into halves, sorts them, and merges them.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # Merge the two halves back into the original array
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left subarray
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy any remaining elements from the right subarray
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    try:
        orders = []
        n = int(input("Enter number of online orders: "))
        
        if n <= 0:
            print("Please enter a positive integer for the number of orders.")
        else:
            for i in range(n):
                time = int(input(f"Enter delivery time for order {i + 1} (minutes): "))
                orders.append(time)

            print("\nOriginal Delivery Times:")
            print(orders)

            mergeSort(orders)

            print("\nSorted Delivery Times (Quickest First):")
            print(orders)
            
    except ValueError:
        print("Invalid Input! Please enter integers only for orders and times.")
