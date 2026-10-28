def fractional_knapsack(weights,profits,capacity):
	n = len(weights)

	items = []

	for i in range(n):
		ratio = profits[i]/weights[i]

		items.append([i+1, weights[i], profits[i], ratio])
		
	items.sort(key = lambda x:x[3], reverse = True)

	total_profit = 0

	remaining_capacity = capacity

	print("\nItems selected: ")

	print("="*50)

	print("Items\tWeight\tProfit\tRatio\tFraction\tProfit Earned")

	print("-"*65)

	for item in items:
		item_no = item[0]
		weight = item[1]
		profit = item[2]
		ratio = item[3]

		if weight <= remaining_capacity:
			fraction = 1
			earned_profit = profit
			taken_weight = weight

		else:
			fraction = remaining_capacity/weight
			earned_profit = profit*fraction
		
		total_profit += earned_profit
		remaining_capacity -= taken_weight

		print(f"{item_no}\t"
		      f"{weight:.2f}\t"
	              f"{profit:.2f}\t"
		      f"{ratio:.2f}\t"
	              f"{fraction*100:.2f}\t"
	              f"{earned_profit:.2f}\t"
                )
		
		if remaining_capacity == 0:
			break
	return total_profit


print("="*65)

print("		FRACTIONAL KNAPSACK - SHIPPING COMPANY")

print("="*65)

n = int(input("\nEnter number of parcels: "))

weights = []

profits = []

for i in range(n):
	print(f"\nParcel {i+1}")
	weight = float(input("Enter weiht: "))
	profit = float(input("Enter profit: "))

	weights.append(weight)
	profits.append(profit)

capacity = float(input("\nEnter Truck Capacity: "))

maximum_profit = fractional_knapsack(weights,profits,capacity)

print("\n" + "=" *65)

print("		FINAL RESULT")

print("="*65)

print(f"Truck Capacity: {capacity:.2f}")

print(f"Maximum Profit: {maximum_profit:.2f}")

print("=" * 65)
			
			