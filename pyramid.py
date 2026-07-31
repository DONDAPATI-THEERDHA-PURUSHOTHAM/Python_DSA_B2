print("Stars pyrmid in line:")
n=5
for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
print("======================")
print("Right angle pyramid:")
n=5
for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
  print()
print("======================")
print("Explaination")
# Initialize the number of rows for the triangle pattern
n = 8

# Outer loop: Iterates through each row of the triangle
# 'i' represents the current row number (from 1 to n)
for i in range(1, n + 1):
  # Inner loop: Iterates to print the asterisks for the current row
  # The number of asterisks in each row is equal to the current row number 'i'
  for j in range(i):
    # Print an asterisk followed by a space, staying on the same line
    print("*", end=" ")
  # After printing all asterisks for the current row, move to the next line
  print()
print("======================")
print("Pyramid Method 1:")
n=5
for i in range(n):
  for j in range(n-1-i):
    print(" ",end=" ")
  for k in range(2*i+1):
    print("*",end=" ")
  print()
print("=======================")
print("Pyraid Method 2:")
n=5
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(i):
    print("*",end=" ")
  print()
print("=====================")
print("Trail:")
n=5
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end=" ")
  print()
print("======================")
print("Donwards:")
n=5
for i in range(n, 0, -1):
  for j in range(n - i):
    print(" ",end="")
  for k in range(i):
    print("*",end=" ")
  print()
print("=====================")
print("Diamond method 1:")
n=5
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(i):
    print("*",end=" ")
  print()
n=5
for i in range(n-1, 0, -1):
  for j in range(n - i):
    print(" ",end="")
  for k in range(i):
    print("*",end=" ")
  print()
print("====================")
print("Diamond Methd 2:")
n=5
for i in range(1,n+1):
  for j in range(n-i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end="")
  print()
n=5
for i in range(n-1, 0, -1):
  for j in range(n - i):
    print(" ",end="")
  for k in range(2*i-1):
    print("*",end="")
  print()
print("==================")
print("Hollow square:")
n = 5
for i in range(n):
    for j in range(n):
        # Print '*' for the first row, last row, first column, and last column
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            # Print space for the inner part of the square
            print(" ", end=" ")
    print()  # Move to the next line after each row
print("======================")
print("adjacant square")
n=6
for i in range(n):
  for j in range(n):
    if i == 0 or i == n - 1 or i==j or j == 0 or j == n - 1:
      print("* ", end=" ")
    else:
      print("  ", end=" ")
  print()
print("======================")
print("Armstrong numbers:")
n=153
or_n=n
s_str=str(n)
power=len(s_str)
total=0
while n>0:
  digit=n%10
  total+=digit**power
  n=n//10
if total==or_n:
  print("Armstrong")
else:
  print("Not an Armstrong number")
print("==========================")
print("Perfect number:")
n = 6
sum=0
for i in range(1, n):
    if n%i==0:
        sum+=i
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
print("================================")
print("Pascal Triangle:")
def generate_pascal_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
def print_pascal_triangle(triangle):
    max_len = len(" ".join(map(str, triangle[-1]))) if triangle else 0
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_len))
num_rows = 5
pascal_triangle = generate_pascal_triangle(num_rows)
print_pascal_triangle(pascal_triangle)
print("=====================================")
print("Strong Number:")
def factorial(n):
    if n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
num = 145
original_num = num
sum_of_factorials = 0
while num > 0:
    digit = num % 10
    sum_of_factorials += factorial(digit)
    num //= 10
if sum_of_factorials == original_num:
    print(f"{original_num} is a strong number")
else:
    print(f"{original_num} is not a strong number")
print("================================")
