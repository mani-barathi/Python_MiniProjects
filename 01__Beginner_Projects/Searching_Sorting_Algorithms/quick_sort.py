
def swap(arr,i,j):
	arr[i],arr[j] = arr[j],arr[i]

def partition(arr,l,r):
	pivot = arr[r]
	i = l-1
	j = l
	for j in range(l,r):
		if arr[j] < pivot:
			i+=1
			swap(arr,i,j)
	i+=1
	swap(arr,i,r)
	return i
		
def quickSort(arr,l,r):
	if l<r :
		newIndex = partition(arr,l,r)
		quickSort(arr,newIndex+1,r)
		quickSort(arr,l,newIndex-1)


arr = [-2,3,4,1,5,0]
print("Before:",arr)
quickSort(arr,0,len(arr)-1)
print('After :',arr)