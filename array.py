print("Find the sum of elements")
#withot uing Built-in functions
arr=[2,5,4,6,7,9]
total_elements_sum=0 
for i in arr:
  total_elements_sum+=i
print(total_elements_sum)
print("=====================")
print("Find the sum of index from 2 to 5")
#withot uing Built-in functions
arr=[2,5,4,6,7,9]
current_range_sum=0 
for i in range(2,6):
  current_range_sum+=arr[i]
print(current_range_sum)
print("=====================")
print("prefix Sum:")
def build_prefix(arr):
  prefix=[]
  current_sum=0
  for i in arr:
    current_sum+=i
    prefix.append(current_sum)
  return prefix
#arr=[2,2+5,7+4]
arr=[2,5,4,6,7,9]
print(build_prefix(arr))
print("======================")
print("Explaintion:")
# This code block demonstrates how to calculate the prefix sum of an array.

# A prefix sum (or cumulative sum) array is an array where each element at index `i`
# stores the sum of all elements from the original array up to and including index `i`.

# Function to build a prefix sum array
def build_prefix(arr):
  # Initialize an empty list to store the prefix sums
  prefix = []
  # Initialize a variable to keep track of the running sum
  current_sum = 0 # Renamed 'sum' to 'current_sum' to avoid shadowing the built-in sum() function

  # Iterate through each element in the input array `arr`
  for element in arr:
    # Add the current element to the running sum
    current_sum += element
    # Append the `current_sum` to the `prefix` list
    # This `current_sum` is the sum of all elements encountered so far
    prefix.append(current_sum)

  # Return the completed prefix sum array
  return prefix

# Example usage of the build_prefix function:
# Define an example array
arr = [2, 5, 4, 6, 7, 9]

# Call the function to get the prefix sum array
# For arr = [2, 5, 4, 6, 7, 9]:
# - prefix[0] = 2
# - prefix[1] = 2 + 5 = 7
# - prefix[2] = 7 + 4 = 11
# - prefix[3] = 11 + 6 = 17
# - prefix[4] = 17 + 7 = 24
# - prefix[5] = 24 + 9 = 33
# Expected output: [2, 7, 11, 17, 24, 33]
print(build_prefix(arr))
print("======================")
def range_sum(prefix,start,end):
  if start==0:
    return prefix[end]
  return prefix[end]-prefix[start-1]
arr=[2,5,4,6,7,9,7,6]
prefix=build_prefix(arr)
print(prefix)
print(range_sum(prefix,2,6))
print("======================")
print("Explaiation:")
# This function calculates the sum of elements in a given range [start, end] (inclusive) using a prefix sum array.
# The 'prefix' array is assumed to be already built by a function like 'build_prefix' from a previous cell.
def range_sum(prefix, start, end):
  # If the start index is 0, the sum from index 0 to 'end' is simply prefix[end].
  # This is because prefix[end] stores the cumulative sum up to 'end'.
  if start == 0:
    return prefix[end]
  # If the start index is not 0, the sum of elements from 'start' to 'end' is calculated as:
  # (Sum up to 'end') - (Sum up to 'start-1')
  # This effectively isolates the sum of elements within the desired range.
  return prefix[end] - prefix[start - 1]

# Define an example array for demonstration.
arr = [2, 5, 4, 6, 7, 9, 7, 6]

# Call the 'build_prefix' function (defined in a previous cell) to create the prefix sum array.
# For arr = [2, 5, 4, 6, 7, 9, 7, 6], the prefix array will be:
# [2, 7, 11, 17, 24, 33, 40, 46]
prefix = build_prefix(arr)

# Print the generated prefix sum array.
print(prefix)

# Example usage of range_sum:
# Calculate the sum of elements from index 2 to 6 (inclusive) of the original array 'arr'.
# arr[2] = 4, arr[3] = 6, arr[4] = 7, arr[5] = 9, arr[6] = 7
# Expected sum: 4 + 6 + 7 + 9 + 7 = 33
# Using prefix sum: prefix[6] (sum up to index 6) - prefix[2-1] (sum up to index 1)
# prefix[6] = 40 (2+5+4+6+7+9+7)
# prefix[1] = 7 (2+5)
# Result = 40 - 7 = 33
print(range_sum(prefix, 2, 6))
print("==================")
print("Equilibrium index")
def Equilibrium_index(arr):
  total_sum = sum(arr)
  left_sum = 0
  for i in range(len(arr)):
    right_sum = total_sum - arr[i] - left_sum
    if right_sum == left_sum:
      return i
    left_sum += arr[i]
  return -1
arr = [-7, 1, 5, 2, -4, 3, 0]
print(Equilibrium_index(arr))
print("======================")
#Equilibrium index
# An equilibrium index of an array is an index such that the sum of elements
# at lower indices is equal to the sum of elements at higher indices.

def Equilibrium_index(arr):
  # Calculate the total sum of all elements in the array.
  # Renamed 'sum' to 'total_array_sum' to avoid shadowing the built-in sum() function.
  total_array_sum = sum(arr)
  # Initialize 'left_sum' to keep track of the sum of elements to the left of the current index.
  left_sum = 0
  
  # Iterate through the array with its indices.
  for i in range(len(arr)):
    # Calculate 'right_sum': total_array_sum - current_element - left_sum
    # This gives the sum of elements to the right of the current index.
    right_sum = total_array_sum - arr[i] - left_sum
    
    # If 'left_sum' equals 'right_sum', then 'i' is an equilibrium index.
    if right_sum == left_sum:
      return i # Return the equilibrium index
    
    # Add the current element to 'left_sum' for the next iteration.
    left_sum += arr[i]
    
  # If no equilibrium index is found after checking all elements, return -1.
  return -1

# Example usage:
arr = [-7, 1, 5, 2, -4, 3, 0]
print(Equilibrium_index(arr))

# Another example:
arr2 = [1, 2, 3, 4, 5, 5]
print(f"Equilibrium index for arr2: {Equilibrium_index(arr2)}")
print("===========================")
print("Sub array equal to total")
#possible sub array
#[1],[2],[3],[4],[1,2],[2,3],[1,2,3],[1,2,3,4],[2,3,4],[3,4] find which equl k=7
a2=[1,2,3,4]
k=7
def sub_array(arr, target):
  result = []
  n = len(arr)
  for i in range(n):
    current_sum = 0
    current_subarray = []
    for j in range(i, n):
      current_sum += arr[j]
      current_subarray.append(arr[j])
      if current_sum == target:
        result.append(list(current_subarray)) # Append a copy of the subarray
  return result

print(f"Subarrays with sum {k}: {sub_array(a2, k)}")
print("=================================")
print("Explaination:")
#Sub aay equal to total
#possible sub array
#[1],[2],[3],[4],[1,2],[2,3],[1,2,3],[1,2,3,4],[2,3,4],[3,4] find which equl k=7
a2=[1,2,3,4]
k=7

# Function to find all subarrays within an array that sum up to a given target.
def sub_array(arr, target):
  result = [] # Initialize an empty list to store the subarrays that meet the criteria.
  n = len(arr) # Get the total number of elements in the input array.

  # Outer loop: Iterates through each possible starting element of a subarray.
  # 'i' represents the starting index of the subarray.
  for i in range(n):
    current_sum = 0 # Initialize the sum for the current subarray.
    current_subarray = [] # Initialize an empty list to build the current subarray.

    # Inner loop: Iterates from the current starting element 'i' to the end of the array.
    # 'j' represents the ending index of the subarray.
    for j in range(i, n):
      current_sum += arr[j] # Add the current element to the running sum of the subarray.
      current_subarray.append(arr[j]) # Add the current element to the current subarray list.

      # Check if the sum of the current subarray equals the target.
      if current_sum == target:
        # If it matches, append a copy of the current_subarray to the results list.
        # A copy (list(current_subarray)) is used because 'current_subarray' will continue to change.
        result.append(list(current_subarray)) 
  return result # Return the list of all subarrays whose sum equals the target.

# Example usage:
print(f"Subarrays with sum {k}: {sub_array(a2, k)}")
