#print(1/0)
#---------------------------------------------------------------------------
#ZeroDivisionError                         Traceback (most recent call last)
#/tmp/ipykernel_3186/165659023.py in <cell line: 0>()
#----> 1 print(1/0)

print("ZeroDivisionError: division by zero")
print("\n=================")

try:
  print(1/0)
except ZeroDivisionError:
  print("Division by zero")

print("\n============")
print("try,except")
try:
  print(1/0)
except:
  print("ZeroDivisionError")

print("\n============")
print("try,except,except")
try:
  x=int(input())
  print(x)
except ValueError as e:
  print(e)
except:
  print("Error")

#ZeroDivisionError
#ValueError
#TypeError
#IndexError  #IUndexOutOfRange
#ClassNotFoundError
#ModuleNotFoundError
#KeyError

print("\n=================")
print("try, except, finally")
try:
  x=int(input())
  print(x)
except:
  print("Error")
finally:
  print("Done")

print("\n========")
print("for, else")
for i in range(5):
  print(i)
else:
  print("Done")

print("========")
print("for, break, else")
for i in range(5):
  print(i)
  if i==3:
    break
else:
  print("Done")

print("\n========")
print("try,except,else")
try:
  x=int(input())
  print(x)
except:
  print("Error")
else:
  print(f"{x} is the number")
print("\n===================")
print("file in pc create and write, read")
import os
# Define the directory and filename parts
directory_name = "Dondapati Theerdha Purushotham"
file_name = "file.txt"
# Construct the full path using os.path.join for cross-platform compatibility
# This will use '/' as the separator in Colab (Linux)
full_path = os.path.join(directory_name, file_name)
# Create the directory if it doesn't already exist
os.makedirs(directory_name, exist_ok=True)
# Open the file in write mode and write the message
with open(full_path, "w") as f:
  f.write("Hello Boss")

print("======================")
print("file write and read")
with open ("file.txt","w") as f:
  f.write("Hello Boss")
with open("file.txt","r") as f:
  print(f.read())
print("Append")
with open("file.txt","a") as f:
  f.write("\tGoodbye")
print("append read")
with open("file.txt","r") as f:
  print(f.read())

print("======================")
print("Number of positive check")
x=int(input())
print(x)
if x<0:
  raise ValueError(f"Number {x} should be positive")

print("=======================")
print("class")
class dummy():
  def __init__(self,name,age,city):
    self.name=name
    self.age=age
    self.city=city
d=dummy("Arjun",18,"vijayawada")
d1=dummy("Porus",21,"Ramavarapadu")
print(d.age)
print(d1.name)

print("=========================")
print("Class and implementation")
class dummy():
  def __init__(self,name,age,city):
    self.name=name
    self.__age=age # Changed from self.age = age to self.__age = age
    self.city=city
  def getage(self):
    return self.__age
  def setage(self,age):
    self.__age=age
d=dummy("Arjun",18,"vijayawada")
print(d.getage())

print("=======================")
print("Inheritance")
class Animal():
  def dummy(self):
    print("Animal")
  def sound(self):
    print("Animal Sound")
class Dog(Animal):
  def sound(self):
    print("Bark")
class Cat(Animal):
  def sound(self):
    print("Meow")
a=Animal()
d=Dog()
c=Cat()
a.dummy()
a.sound()
d.sound()
d.dummy()
c.dummy()
c.sound()

print("\n==================")
print("Bank work")
from abc import abstractmethod,ABC
class BankAccount(ABC):
  def __init__(self,balance):
    self.__balance=balance
  def deposit(self,amount):
    self.balance+=amount
  def withdraw(self,amount):
    self.balance-=amount
  def getbalance(self):
    return self.balance
@abstractmethod
def interstcal(self):
  pass

class SavingAcc(BankAccount):
  def interstcal(self):
    return 0.03*self.__balance
s=SavingAcc(100)

print("Explaination with comments")
from abc import abstractmethod, ABC

# Abstraction and Inheritance: BankAccount is an Abstract Base Class (ABC).
# It defines a common interface for different types of bank accounts
# but cannot be instantiated directly. Subclasses must implement its abstract methods.
class BankAccount(ABC):
  # Encapsulation: The __balance attribute is 'private' (name-mangled).
  # It's accessed and modified through methods (deposit, withdraw, getbalance).
  def __init__(self,balance):
    self.__balance=balance # Encapsulated balance

  # Encapsulation: Public method to deposit money, modifying the private balance.
  def deposit(self,amount):
    self.__balance+=amount # Accessing the encapsulated balance

  # Encapsulation: Public method to withdraw money, modifying the private balance.
  def withdraw(self,amount):
    self.__balance-=amount # Accessing the encapsulated balance

  # Encapsulation: Public method to get the current balance.
  def getbalance(self):
    return self.__balance # Accessing the encapsulated balance

  # Abstraction and Polymorphism: This is an abstract method.
  # Subclasses (like SavingAcc from another cell) *must* provide their own implementation
  # of this method. This allows different account types to calculate interest
  # in their own way (polymorphism), while ensuring all BankAccounts have this capability (abstraction).
  @abstractmethod
  def interstcal(self):
    pass
  
class SavingAcc(BankAccount):
  # Inheritance: SavingAcc inherits from BankAccount, gaining its attributes and non-abstract methods.
  # Polymorphism: It provides its specific implementation for the abstract method 'interstcal'.
  def interstcal(self):
    # Encapsulation: Although __balance is private in BankAccount, subclasses can access it 
    # indirectly via inherited public methods like getbalance() or by defining their own mechanism.
    # In this case, we'll assume a method to access balance for calculation.
    # If direct access was needed, BankAccount would need a protected getter or a property.
    # For simplicity, let's assume getbalance() is used here if direct access wasn't intended.
    # The previous code for SavingAcc directly accessed self.__balance which would cause an AttributeError
    # because __balance is name-mangled to _BankAccount__balance in the parent.
    # To correctly access the balance from a subclass, one would typically use a public getter method.
    return 0.03 * self.getbalance() # Accessing balance via the public getter method
s=SavingAcc(100)
#Outputs
# Print initial balance
print(f"Initial balance: {s.getbalance()}")

# Perform a deposit
s.deposit(50)
print(f"Balance after deposit: {s.getbalance()}")

# Perform a withdrawal
s.withdraw(20)
print(f"Balance after withdrawal: {s.getbalance()}")

# Print calculated interest
print(f"Calculated interest: {s.interstcal()}")