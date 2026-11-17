
def heapify(arr, n, i, is_max):
    best = i
    l, r = 2*i+1, 2*i+2

    if l < n and (arr[l] > arr[best] if is_max else arr[l] < arr[best]):
        best = l
    if r < n and (arr[r] > arr[best] if is_max else arr[r] < arr[best]):
        best = r

    if best != i:
        arr[i], arr[best] = arr[best], arr[i]
        heapify(arr, n, best, is_max)


def heap_sort(arr, is_max):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i, is_max)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, is_max)


print("="*60)
print("              HEAP SORT ALGORITHM")
print("="*60)
print("\n1. Max-heap -> Ascending order")
print("2. Min-heap -> Descending order")

choice = input("\nEnter your choice (1 or 2): ")
arr = list(map(int, input("Enter integers separated by spaces: ").split()))

print("\nOriginal Array:", arr)

if choice in ("1", "2"):
    result = arr.copy()
    heap_sort(result, choice == "1")
    print("Heap used:", "Max heap" if choice == "1" else "Min heap")
    print("Sorted array:", result)
else:
    print("Invalid choice! Please select 1 or 2.")

print("\nTime complexity: O(n log n)")
print("Space complexity: O(log n) recursive stack")
print("="*60)
