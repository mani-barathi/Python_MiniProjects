def smallest(arr):
	return (min(arr))

def selection(arr):
	for i in range(len(arr)):
		current=arr[i]
		small_index=arr.index(smallest(arr[i:]))
		arr[i]=arr[small_index]
		arr[small_index]=current
	return arr

if __name__ == '__main__':
	print("Unsorted: ",[10,8,9,7,6])
	sorted=selection([10,8,9,7,6])
	print(f'Sorted  : {sorted}')