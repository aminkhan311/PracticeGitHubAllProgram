a=set({})
b=set()
# error b=set(1,2,3,4,5,6)
c={1,2,3,4}

print(type(a),type(b),type(c))


print("_________Unordered Unique Elements_____________________")
py_set={1,'khan',2,3,4,5,66,7,8,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,0,9,8,'amin','python','java','MongoDB'}
print(py_set)

print("-"*50)
s={1,2,3,4,5,6,7,8,7,6,5,4,3,2,1}
print(s)

s.add(500)
print("add:",s)

s.discard(8)
s.discard(50000)
print("discard:",s)

s.add(8)
print(s)

# s.remove(50)
s.remove(8)
print("remove:",s)

s.add(8)
print("pop:",s.pop())
print(s)



