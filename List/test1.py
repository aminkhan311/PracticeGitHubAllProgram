py_list=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,3,2]

print('print list: ',py_list)
print('length of list: ',len(py_list))
print('type of object:',type(py_list))
print('memory address of object:',id(py_list))
print('\nPrint every elements of list')
for i in py_list:
    print(i,end=' ')

print(f"\nprint 3 to 5:{py_list[2:5]}")
print(f"reverse list:{py_list[::-1]}")
print(f"odd position:{py_list[0::2]}")
print(f"even position{py_list[1::2]}")
