a = [1, 2, 3]
b = [4, 5]
result = a + b
print(result) # [1, 2, 3, 4, 5]
print(a)
print(b)

a = a + b
print(a)

c = "py"
c = c + "thon"
print(c)










a = [10, 20, 30]
b = a

print(a)
print(b)
print(a == b)
print(a is b)

b[0] = 999
print(a) 
print(b) 



a = [10, 20, 30]
b = a[:] #a와는 다른 값 참조

print(a)
print(b)
print(a == b) 
print(a is b)

b[0] = 999
print(a) # [10, 20, 30]
print(b) # [999, 20, 30]