s1="my name is python"
s2='my name is python'
s3='''myname is python'''   #not same

print(s1==s2)
print('-'*50)

s="my name is Java"
print("Upper:",s.upper())
print("lower:",s.lower())
print("Captitaliazed:",s.capitalize())
print("SwapCase:",s.swapcase())
print("Count:",s.count('s'))
print("len:",len(s))
print("Split:",s.split())
print("index:",s.index('a'))
print("Find:",s.find("is"))
print("Startwith:",s.startswith('my'))
print("endwith:",s.endswith('Java'))
print("cenetr:",s.center(30))
print("replace:",s.replace('is','am'))
print("join:","".join(['1','2','3','4','5']))
print(s)
print("-"*50)
print(s[0])
print(s[0:10])
print(s[5:10])
print(s[::-1])
print(s[0::+2])
print(s[1::+2])
print(s)