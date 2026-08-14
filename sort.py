#Day 8
#Merge sort
arr=[3,4,2,1]
def merge_sort(arr):
  if len(arr)>1:
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    lp=0
    rp=0
    fp=0
    while lp<len(left) and rp<len(right):
      if left[lp]<right[rp]:
        arr[fp]=left[lp]
        lp+=1
        fp+=1
      elif left[lp]>right[rp]:
        arr[fp]=right[rp]
        rp+=1
        fp+=1
    while lp<len(left):
      arr[fp]=left[lp]
      fp+=1
      lp+=1
    while rp<len(right):
      arr[fp]=right[rp]
      fp+=1
      rp+=1
print(arr)
merge_sort(arr)
print(arr)
print("=================")
import random
x=random.random()
print(x)
print("=================")
#Rock, Paper and Scissors using random
"""import random
def play_rps():
    choices=["rock","paper","scissors"]
    player_choice=input("Enter your choice (rock,paper,or scissors): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please choose rock,paper,or scissors.")
        return
    computer_choice=random.choice(choices)
    print(f"You chose:{player_choice}")
    print(f"Computer chose:{computer_choice}")
    if player_choice==computer_choice:
        print("It's a tie!")
    elif (
        (player_choice=="rock" and computer_choice=="scissors") or
        (player_choice=="paper" and computer_choice=="rock") or
        (player_choice=="scissors" and computer_choice=="paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
play_rps()"""
print("=================")
#Quick sort
import random
def quick_sort(arr):
  if len(arr)<=1:
    return arr
  else:
    pivot=random.choice(arr)
    left=[i for i in arr if i<pivot]
    middle=[i for i in arr if i==pivot]
    right=[i for i in arr if i>pivot]
  return quick_sort(left)+middle+quick_sort(right)
arr=[1,2,5,4,3]
print(quick_sort(arr))
print("=================")