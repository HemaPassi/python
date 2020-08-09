
#packing and unpacking arguments
print(1,2,3,4)
numbers = [1,2,3,4]
print(numbers)  
print(*numbers)

def add(*numbers):
    total =0
    for num in numbers:
        total=num + total
    return(total)


total = add(1,2,3,4,5,6,7)
print(total)
