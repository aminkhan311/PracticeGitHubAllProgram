py_t=1,2,3,4,5,6,7,8,6,5,4
py_t1=(1,2,3,4,5,6,7,8,6,5,4)
print("Both same or not")
print(py_t==py_t1)

print(py_t.count(5))

i=py_t.index(3)
print(i)


print("Tuple is Immutable")

a=(1,2,3,[1,2])
print(id(a))
a[3].append("amin khan")
print(a)
print(id(a))