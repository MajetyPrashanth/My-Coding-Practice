import numpy
numpy.set_printoptions(legacy = '1.13')
lst = list(map(float,input().split()))
lst1 = numpy.array(lst)
print(numpy.floor(lst1))
print(numpy.ceil(lst1))
print(numpy.rint(lst1))
