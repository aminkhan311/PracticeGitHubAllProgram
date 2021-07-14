p=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,5,6,7,6,5,6]

print(f"list:",p)

print("Append")
p.append("abcd")
print(p)

print("insert element in 3 position")
p.insert(2,'Java')
print(p)

print("remove elements")
p.remove('abcd')
print(p)

print("Pop elements")
p.pop(2)
print(p)

print("extend one to another")
p.extend([1,2,3])
print(p)

print("index of 9")
print(p.index(9))

print("Count number of 3")
print(p.count(3))

print("reverse")
p.reverse()
print(p)

print("Sort assending order")
p.sort()
print(p)

print("Sort reverse")
p.sort(reverse=True)
print(p)
