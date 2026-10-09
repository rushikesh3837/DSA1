def fractional_knapsack(items, capacity):
    """
    Solves the Fractional Knapsack problem using a Greedy approach.
    Expects items to be a list of lists, where each item is [weight, profit, ratio].
    """
    # Sort by profit/weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    total_profit = 0

    print("\nSelected Parcels:")
    for item in items:
        weight = item[0]
        profit = item[1]

        if capacity == 0:
            break

        if weight <= capacity:
            print(f"Full Parcel -> Weight: {weight}, Profit: {profit}")
            capacity -= weight
            total_profit += profit
        else:
            fraction = capacity / weight
            partial_profit = profit * fraction
            print(f"Partial Parcel -> Weight: {capacity}, Profit: {round(partial_profit, 2)}")
            total_profit += partial_profit
            capacity = 0

    print(f"\nMaximum Profit = {round(total_profit, 2)}")


# ---------------- Main Program ---------------- #
if __name__ == "__main__":
    try:
        n = int(input("Enter number of parcels: "))
        if n <= 0:
            print("Please enter a positive integer for the number of parcels.")
        else:
            items = []
            for i in range(n):
                print(f"\n--- Parcel {i + 1} ---")
                weight = float(input("Enter weight: "))
                profit = float(input("Enter profit: "))
                
                if weight <= 0 or profit < 0:
                    print("Weight must be greater than 0 and profit cannot be negative.")
                    exit()
                    
                ratio = profit / weight
                items.append([weight, profit, ratio])

            capacity = float(input("\nEnter truck capacity: "))
            if capacity < 0:
                print("Truck capacity cannot be negative.")
            else:
                fractional_knapsack(items, capacity)

    except ValueError:
        print("Invalid Input! Please enter valid numerical values.")
