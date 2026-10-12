num= [1,2, 'three']

def number():
    a= num+[4]
    return a

def alpha():
    b=num+["four"]
    return b

print("Numeric function:", number())
print("alpha function:", alpha())


