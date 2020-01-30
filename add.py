import tensorflow
print(' ')
print(' ')
print(' ')
print('-----------')
print(' ')

# Build a graph
a = tensorflow.constant([2])
b = tensorflow.constant([3])


@tensorflow.function
def add(x, y):
    return x + y


result = add(a, b)
print('The result: ', result)


print(' ')
print(' ')
print(' ')
print('----end----')
print(' ')
