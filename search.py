#day 7
#Linear Search
a=[10,20,30,40,50,4,50,54]
tar=50
for i in range(len(a)):
    if tar==a[i]:
        print(i)
        break
print("================")
#binary Search
#Only in sorted lists
a=[5,7,12,17,23,36,47,54]
target=36
left=0
right=len(a)-1
while left<=right:
  mid=(left+right)//2
  if a[mid]==target:
    print(mid)
    break
  elif a[mid]>target:
    right=mid-1
  elif a[mid]<target: 
    left=mid+1
print("================")
#Find square root of 50 using binary search
a=[5,7,12,17,23,36,47,54]
left=0
right=50
ans=0
while left<=right:
  mid=(left+right)//2
  if mid*mid==50:
    ans=mid
    break
  elif mid*mid>50:
    ans=mid
    right=mid-1
  elif mid*mid<50:
    ans=mid 
    left=mid+1
print(ans)
print("================")
# Sort the array using Bubble Sort algorithm
# This method does not use any built-in sorting functions.

# Initialize an array with unsorted elements
a=[2,5,1,9,3,4,6,8,7]

# Get the length of the array, which determines the number of passes needed
n=len(a)

# Outer loop: Iterate 'n' times (or n-1 times if considering passes)
# Each pass places the largest unsorted element at its correct position at the end.
for i in range(n):
  # Inner loop: Iterate through the unsorted part of the array
  # The '-i-1' ensures we don't compare elements that are already sorted
  # at the end of the array (after 'i' passes, 'i' elements from the end are sorted).
  for j in range(0,n-i-1):
    # Compare adjacent elements
    if a[j]>a[j+1]:
      # If the current element is greater than the next element, swap them
      # This 'bubbles up' the larger elements towards the end of the array
      a[j],a[j+1]=a[j+1],a[j]

# Print the sorted array
print(a)
print("================")
#Method 2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sorted:", bubble_sort(numbers))
print("================")
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min= j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
numbers = [29, 10, 14, 37, 13]
print("Selection Sorted:", selection_sort(numbers))