a={}
b={1:1,2:2,3:3}
# c={[1,2,3]:1,[2,1,3]:3}   error key is immutable
c={1:1,2:2,1:4}   #duplicates key not allowed always consider latest
print(type(a),type(b),type(c))

print(b)
print(c)
a["name"]="amin"
print(a)
a["name"]="khan"
print(a)

print("Keys:",b.keys())
print("Values:",b.values())

print("Items:",b.items())

print("get:",b.get(2))
print("Get:",b.get(500,"Not present"))

b.pop(1)
print("pop:",b)

b.popitem()
print("popItems:",b)

b.setdefault(1,"amin khan")
print(b)

b.setdefault(b.setdefault(2,"python"))
print("Setdefault:",b)
