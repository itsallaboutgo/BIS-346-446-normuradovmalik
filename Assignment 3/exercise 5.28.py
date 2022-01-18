# exercise 5.28

import statistics

import numpy

l=[1,2,5,4,3,5,2,1,3,3,1,4,3,3,3,2,3,3,2,5]

print('The min value of data is:',min(l))
print('The max value of data is:',max(l))
print("The range of data is: (",min(l),', ',max(l),')')
print("The mean of data is: ",numpy.mean(l))
print("The median of data is: ",numpy.median(l))
print("The mode of data is:",statistics.mode(l))
print("The variance of data is:",statistics.variance(l))
print("The standard deviation of data is:",statistics.stdev(l))
