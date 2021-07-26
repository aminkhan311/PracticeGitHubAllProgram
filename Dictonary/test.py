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


#insert single dict key and values to the another dict
d={1:2,4:3,2:7,8:2,9:6}
p={}
p[list(d.keys())[0]]=list(d.values())[0]
print(p)

#insert whole dict to another and sort
d={1:2,4:3,2:7,8:2,9:6}
p={}
for i in range(10):
   for k,v in d.items():
       if i==v:
           p[k]=v
print(p)


# sort nested dict
d={'e1':{"name":"amin","marks":99,"sal":1000000},
   "e2":{"name":"abc","marks":34,"sal":800000},
   "e3":{"name":"XYZ","marks":80,"sal":90000},}
p={}
for i in range(100):
    for k1,v1 in d.items():
        if i==v1["marks"]:
            p[k1]=v1
print(p)