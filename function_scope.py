a =10;

def f1():
    a=100
    print(a)

def f2():
    print(a)


f1()
f2()



# overriding global funciton 

a =10;

def f1_global_example():
    global a
    a=150
    print(a)

def f2_global_example():
    a=10
    print(a)


f1_global_example()
f2_global_example()
print(a)


