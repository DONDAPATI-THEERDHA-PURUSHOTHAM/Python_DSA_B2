#Frequecy Counting
print("Frequency Counting: ")
arr=[2,4,2,5,7,8,3,7,2,1,6]
freq={}
for num in arr:
  freq[num]=freq.get(num,0)+1
print(freq)
print("===========================")
#Find first non-repeating element
print("Find first non-repeating element: ")
arr=[2,4,2,5,7,8,3,7,2,1,6]
freq={}
for num in arr:
  freq[num]=freq.get(num,0)+1
for key in freq:
  if freq[key]==1:
    print(key)
    break
print("===========================")
print("Remove duplicate elements from a list while maintaining order: ")
arr=[2,4,2,5,7,8,3,7,2,1,6]
freq=[]
for num in arr:
  if num not in freq:
    freq.append(num)
print(freq)
print("===========================")
print("Return the duplicate elements in list using sets: ")
arr=[2,4,2,5,7,8,3,7,2,1,6]
seen = set()
duplicates = set()
for num in arr:
  if num in seen:
    duplicates.add(num)
  else:
    seen.add(num)
print(list(duplicates))
print("===========================")
print("1. Top K Frequent Elements: ")
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # Create buckets where index = frequency, value = list of numbers with that frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        res = []
        # Traverse buckets from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

# Example usage:
sol = Solution()
nums_example = [1,1,1,2,2,3]
k_example = 2
result = sol.topKFrequent(nums_example, k_example)
print(f"For nums={nums_example} and k={k_example}, the top {k_example} frequent elements are: {result}")

nums_example_2 = [1]
k_example_2 = 1
result_2 = sol.topKFrequent(nums_example_2, k_example_2)
print(f"For nums={nums_example_2} and k={k_example_2}, the top {k_example_2} frequent elements are: {result_2}")
print("===========================")
print("2. Top K Frequent Elements: ")
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count the frequency of each number
        # Initialize an empty dictionary to store the count of each number.
        # The keys will be the numbers, and the values will be their frequencies.
        count = {}
        for num in nums:
            # For each number in the input list 'nums',
            # increment its count in the 'count' dictionary.
            # If the number is not yet in the dictionary, 'get(num, 0)' returns 0,
            # so it starts counting from 1.
            count[num] = count.get(num, 0) + 1   

        # Step 2: Sort numbers by their frequency in descending order
        # Get all unique numbers (keys) from the 'count' dictionary.
        # Sort these numbers based on their corresponding frequencies (values) in descending order.
        # The 'key=lambda x: count[x]' tells the sorted() function to use the frequency of 'x'
        # as the sorting criterion.
        # 'reverse=True' ensures that numbers with higher frequencies come first.
        sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # Step 3: Return the top k most frequent elements
        # After sorting, the first 'k' elements in 'sorted_nums' are the 'k' most frequent ones.
        # Slice the 'sorted_nums' list from the beginning up to (but not including) index 'k'
        # to get these top 'k' elements.
        return sorted_nums[:k]

# Example usage:
sol = Solution()

# Example 1
nums_example = [1,1,1,2,2,3]
k_example = 2
result = sol.topKFrequent(nums_example, k_example)
print(f"For nums={nums_example} and k={k_example}, the top {k_example} frequent elements are: {result}")

# Example 2
nums_example_2 = [1]
k_example_2 = 1
result_2 = sol.topKFrequent(nums_example_2, k_example_2)
print(f"For nums={nums_example_2} and k={k_example_2}, the top {k_example_2} frequent elements are: {result_2}")
print("===========================")
print("3. Top K Frequent Elements: ")
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        # Initialize an empty dictionary to store the count of each number.
        # The keys will be the numbers, and the values will be their frequencies.
        freq={}
        for num in nums:
            # For each number in the input list 'nums',
            # increment its count in the 'freq' dictionary.
            # If the number is not yet in the dictionary, 'get(num, 0)' returns 0,
            # so it starts counting from 1.
            freq[num]=freq.get(num, 0) + 1

        # Step 2: Convert frequency map to a list of (count, number) pairs
        # This step creates a list where each element is a tuple (frequency, number).
        # This format is convenient for sorting based on frequency.
        arr=[]
        for num,count in freq.items():
            arr.append((count,num))

        # Step 3: Sort the list of (count, number) pairs
        # The list 'arr' is sorted in ascending order by default. Since we want top K frequent,
        # sorting in ascending order means the highest frequencies will be at the end of the list.
        arr.sort()

        # Step 4: Extract the top K frequent elements
        # Initialize an empty list to store the results.
        res=[]
        # Loop until 'res' contains 'k' elements.
        # 'arr.pop()' removes and returns the last element (which has the highest frequency
        # because 'arr' is sorted in ascending order of frequency). We then take the number (index 1).
        while len(res)<k:
            res.append(arr.pop()[1])

        # Return the list of top K frequent numbers.
        return res

# Example usage:
sol = Solution()

# Example 1
nums_example = [1,1,1,2,2,3]
k_example = 2
result = sol.topKFrequent(nums_example, k_example)
print(f"For nums={nums_example} and k={k_example}, the top {k_example} frequent elements are: {result}")

# Example 2
nums_example_2 = [1]
k_example_2 = 1
result_2 = sol.topKFrequent(nums_example_2, k_example_2)
print(f"For nums={nums_example_2} and k={k_example_2}, the top {k_example_2} frequent elements are: {result_2}")
print("===========================")
print("Group Anagrams: ")
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Initialize a dictionary to store groups of anagrams.
        # The keys will be the sorted string (canonical form of an anagram),
        # and the values will be lists of original words that are anagrams of each other.
        group = {}

        # Step 2: Iterate through each word in the input list of strings.
        for word in strs:
            # Step 2a: Create a 'key' for the anagram group.
            # Anagrams have the same characters, just in a different order.
            # Sorting the characters of a word creates a unique identifier (canonical form)
            # for all its anagrams. For example, 'eat', 'tea', and 'ate' all become 'aet' when sorted.
            key = "".join(sorted(word))

            # Step 2b: Check if this 'key' (sorted word) already exists in our 'group' dictionary.
            # If the key does not exist, it means we haven't encountered any anagrams for this key yet.
            if key not in group:
                # If it's a new key, initialize its value as an empty list.
                # This list will hold all words that produce this same sorted key.
                group[key] = []

            # Step 2c: Append the original word to the list corresponding to its sorted key.
            # Regardless of whether the key was new or existing, add the current word
            # to the list associated with its canonical form.
            group[key].append(word)

        # Step 3: Return the collected groups of anagrams.
        # The 'group.values()' method returns a view object that displays a list of all the values
        # in the dictionary (which are the lists of anagrams). Converting it to a list ensures
        # it's returned in the expected format List[List[str]].
        return list(group.values())

# Example usage:
sol = Solution()

# Example 1
strs_example_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
result_1 = sol.groupAnagrams(strs_example_1)
print(f"For input {strs_example_1}, grouped anagrams are: {result_1}")
# Expected output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (order of inner lists/elements may vary)

# Example 2
strs_example_2 = [""""""],
result_2 = sol.groupAnagrams(strs_example_2)
print(f"For input {strs_example_2}, grouped anagrams are: {result_2}")
# Expected output: [['']]

# Example 3
strs_example_3 = ["a"]
result_3 = sol.groupAnagrams(strs_example_3)
print(f"For input {strs_example_3}, grouped anagrams are: {result_3}")
# Expected output: [['a']]
print("===========================")
print("Find the number of digits in the given number: ")
arr=[1,2,3,4,-1]
count=0
for num in arr:
  count+=1
print(count)
print("===========================")
print("Name -> Nickname like Rohit sharam->RS ")
str="Rohit Sharma"
out=[]
for i in str:
  if i.isupper():
    out.append(i)
print("".join(out))