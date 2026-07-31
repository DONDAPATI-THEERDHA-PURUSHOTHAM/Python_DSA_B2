#Day 1
"""name="Dondapati Theerdha Purushotham"
for i in range(3):
    print(name)
print("\n")
print(3*"Dondapati Theerdha Purushotham\n")

print("C:\ new\ test")
print("C:\\new\\test")
print(r"C:\new\test")

a=float("1.2")
b=int(float("1.2"))
print(a)
print(b)

n=int(input("Enter the number:"))
if n%2!=0:
    print("Odd")
else:
    print("Even")

dict={
    "names":"Sriram",
    "gender":"male",
    "age": 20,
    "course":["python","java","datascience"]
}
dict["names"]="puru"
dict.update(names="arjun")
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict["course"])
print(dict.get("names"))

l=[1,2,3,4,5,3]
l.remove(3)
l.pop()
print(l)
"""
l=[]
l.append(1)
l.append(2)
l.append(3)
print(l)
x=[]
print(x)
x.append(l)
print(len(x))
print(x)
x.append(5)
print(x)
print(len(x[0]),"len(x[0])")
m=[4,5,6]
x.append(m)
print(x)
