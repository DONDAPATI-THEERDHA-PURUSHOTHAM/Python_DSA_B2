#Day 4
print("Range")
for i in "nriit":
  print(i)
print("======================")
print("Find how any vowels,conconants,spaces and special characters")
x="**python** is a programming language..."
v=0
c=0
s=0
sc=0
vowel="aeiouAEIOU"
for i in x:
  if i.isalpha() and i in vowel:
    v+=1
  elif i.isalpha() and i not in vowel:
    c+=1
  elif i==" " or i.isspace():
    s+=1
  else:
    sc+=1
print(f"the count of vowels:{v}")
print(f"The count of conconants:{c}")
print(f"The count of space:{s}")
print(f"The coun of special characters:{sc}")
print("===============================")
print("Remove duplicates and print")
print("Method 1:")
s="aaaappppppeeee"
dupli=""
for i in s:
  if i not in dupli:
    dupli+=i
print(dupli)
print("Method 2:")
s="aaaaaappppe"
seen=set()
c=""
for i in s:
  if i in seen:
    continue
  seen.add(i)
  c+=i
print(c)
print("==========================")
print("Reverse a string and Palindrome:")
s="mom"
rev=""
for c in s:
  rev=c+rev
print(rev)
if s==rev:
  print("Palindrome")
else:
  print("NOt Palindrome")
print("============================")
print("Anagram Method 1:")
a="listen"
b="silent"
if sorted(a) == sorted(b):
  print("Anagram")
else:
  print("Not Anagram")
print("===========================")
print("Method 2:")
# This code checks if two strings, str1 and str2, are anagrams of each other.
# Anagrams are words or phrases formed by rearranging the letters of another, using all the original letters exactly once.

# Initialize the first string
str1="listen"
# Initialize the second string
str2="silent"

# Step 1: Check if the lengths of the two strings are different.
# If lengths are different, they cannot be anagrams, so print 'Not anagram'.
# Output logic: If len("listen") (6) != len("silent") (6), this condition is false.
if len(str1)!=len(str2):
  print("Not nagram")
else:
  # Step 2: If lengths are the same, proceed to create a frequency map for characters in str1.
  # This dictionary will store each character as a key and its count as a value.
  freq={}
  # Iterate through each character in the first string.
  # Output logic: For str1="listen":
  #   'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1
  for ch in str1:
    # Increment the count of the current character in the frequency dictionary.
    # If the character is not already in the dictionary, it defaults to 0 before incrementing.
    freq[ch]=freq.get(ch,0)+1

  # Step 3: Iterate through each character in the second string to check against the frequency map.
  # Output logic: For str2="silent", it will iterate through 's', 'i', 'l', 'e', 'n', 't'.
  for ch in str2:
    # Check if the character from str2 is not in the frequency map (meaning it wasn't in str1)
    # OR if its count in the frequency map is already zero (meaning all occurrences from str1 have been matched).
    # If either is true, str2 cannot be an anagram, so print 'Not anagram' and exit the loop.
    # Output logic:
    # 's': freq['s'] becomes 0.
    # 'i': freq['i'] becomes 0.
    # 'l': freq['l'] becomes 0.
    # 'e': freq['e'] becomes 0.
    # 'n': freq['n'] becomes 0.
    # 't': freq['t'] becomes 0.
    # At no point is a character not in freq or freq[ch] == 0 before decrementing, so the 'break' is not triggered.
    if ch not in freq or freq[ch]==0:
      print("Not anagram")
      break # Exit the loop if a mismatch is found
    # If the character is found and its count is greater than zero, decrement its count.
    freq[ch]=freq[ch]-1
  else:
    # This 'else' block executes only if the 'for' loop completes without encountering a 'break' statement.
    # If the loop finishes, it means all characters in str2 were found in str1 with matching frequencies.
    # Therefore, the strings are anagrams.
    # Output logic: The loop for str2 completes without a break. So, 'Anagram' is printed.
    print("Anagram")

# Final Output for inputs str1="listen", str2="silent":
# Anagram
print("==========================")
print("Fibonacci series:")
#Fibonacci series
def fibonacci(n):
  if n<=1:
    return n
  return fibonacci(n-1)+fibonacci(n-2)
for i in range(10):
  print(fibonacci(i),end=" ")
