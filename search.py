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