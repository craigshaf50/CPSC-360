
def array_func(array):
    array[0][1]=2
    print(array)

array_func([[1,4],[0,1]])

def array_nest():
    return [[1,5],[3,4]]

array_func(array_nest())

###########################
# python does not support method overloading

def overload_func():
    return 6

def overload_func():
    return 7

print(overload_func())