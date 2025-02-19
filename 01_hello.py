print("hello world")

l = ["10","20","30","40","50"]
k = ["1","2","3","4","5"]
l.append("60")
k.insert(0,"0")
l.insert(6,"70")

p = l+k
print(p)
print(len(p))

p.insert(0,"Start")
print(p)

p.remove("Start")
print(p)

x = l.index("30")
print(x)

l.remove("50")
l.pop(3)
p = ["a","b","c"]
l.extend(p)

print(l)