
def Bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(0,len(arr)-1-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
		# print(arr)

arr = [64, 34, 25, 12,12, 22, 11, 90]
print(f"Before : {arr}")
Bubble_sort(arr)
print(f'After  : {arr}')

