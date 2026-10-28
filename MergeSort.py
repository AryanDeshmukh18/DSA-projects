
def merge(orders, left, middle, right):
    left_part = orders[left:middle + 1]
    right_part = orders[middle + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            orders[k] = left_part[i]
            i += 1
        else:
            orders[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        orders[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        orders[k] = right_part[j]
        j += 1
        k += 1


def merge_sort(orders, left, right):
    if left < right:
        middle = (left + right) // 2

        merge_sort(orders, left, middle)
        merge_sort(orders, middle + 1, right)

        merge(orders, left, middle, right)


def display_orders(orders):
    if len(orders) == 0:
        print("\nNo orders available.")
        return

    print("\n" + "=" * 50)
    print("          ONLINE ORDERS")
    print("=" * 50)

    for i in range(len(orders)):
        print("Order", i + 1, "->", orders[i], "minutes")

    print("=" * 50)


def display_priority(orders):
    if len(orders) == 0:
        print("\nNo orders available.")
        return

    print("\n" + "=" * 50)
    print("          DELIVERY PRIORITY")
    print("=" * 50)

    for i in range(len(orders)):
        if i == 0:
            print("Priority", i + 1, "->",
                  orders[i], "minutes [HIGHEST]")
        else:
            print("Priority", i + 1, "->",
                  orders[i], "minutes")

    print("=" * 50)


orders = []

while True:
    print("\n" + "=" * 60)
    print("       ONLINE ORDERING SYSTEM USING MERGE SORT")
    print("=" * 60)

    print("1. Add Orders")
    print("2. Display Orders")
    print("3. Sort Orders By Delivery Time")
    print("4. Display Delivery Priority")
    print("5. Exit")
    print("=" * 60)

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nInvalid input. Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        try:
            number_of_orders = int(
                input("\nEnter number of online orders: ")
            )
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number_of_orders <= 0:
            print("Number of orders must be positive.")
            continue

        orders.clear()
        valid = True

        print("\nEnter estimated delivery times:")

        for i in range(number_of_orders):
            try:
                delivery_time = int(
                    input("Order " + str(i + 1) + " (minutes): ")
                )
            except ValueError:
                print("Invalid delivery time. Enter numbers only.")
                valid = False
                break

            if delivery_time < 0:
                print("Delivery time cannot be negative.")
                valid = False
                break

            orders.append(delivery_time)

        if valid:
            print("\nOrders added successfully!")
        else:
            orders.clear()

    elif choice == 2:
        display_orders(orders)

    elif choice == 3:
        if len(orders) == 0:
            print("\nPlease add orders first.")
        else:
            print("\nBefore sorting:", orders)

            merge_sort(orders, 0, len(orders) - 1)

            print("Orders sorted successfully!")
            print("After sorting:", orders)

    elif choice == 4:
        display_priority(orders)

    elif choice == 5:
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice. Please select a number from 1 to 5.")
