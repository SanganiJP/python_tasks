print("hello world")

l = [10,20,30,40,50]
k = [1,2,3,4,5]
l.append(60)
k.insert(0,0)
l.insert(6,70)

p = l+k
print(p)
    #print(len(p))

#list enumerate python
    #[print(i) for i in ["apple", "banana", "mango"]]
    #[print(i) for i in l]

#j = [2,4,5,6]
even = [i for i in p if i % 2 == 0]
print("Event element:",even)

odd = [x for x in p if x % 2 != 0]
print("Odd element:",odd)

p.sort()
# odd.reverse()
#even1 = [val for val in j if val % 2 == 0]
#print(even1)

#p.insert(0,"Start")
print(p)

#p.remove("Start")
#print(p)

#x = l.index(30)
#print(x)

#l.remove(50)
#l.pop(0)
#print(l)


lst1 =[8,4,6,3,7,9]

for i in lst1 :
    if i % 2 != 0:
        print("Odd element ",i)

for j in range(len(lst1)-1,0,-1):
    for i in range(j) :
        if lst1[i] > lst1[i+1]:
            lst1[i],lst1[i+1] = lst1[i+1],lst1[i]

print(lst1)

name = "Jayesh"
print(f"My name is {name}")