import csv
import matplotlib.pylab as plt
#import pylab as pl
import operator

csvfile = open("firebug2.csv", 'r')
myDict = {}

for line in csvfile.readlines():
	#print(line)
	array = line.split(',')
	if array[3] in myDict:
		myDict[array[3]] = myDict[array[3]]+1
	else:
		myDict[array[3]] = 1



for k, v in myDict.items():
	print(k, v)

for key in sorted(myDict, key=myDict.get):		#for key in sorted(myDict, key=lambda k: myDict[k]):
	print(key, myDict[key])

print(len(myDict))

#print (myDict.items(), myDict.keys(), myDict.values())

# https://stackoverflow.com/questions/12791923/using-sorted-in-python --> using lambda
# It is not possible to sort a dict, only to get a representation of a dict that is sorted. 
# Dicts are inherently orderless, but other types, such as lists and tuples, are not. 
# So you need a sorted representation, which will be a list—probably a list of tuples.
components_sorted_by_frequency = sorted(myDict.items(), key=operator.itemgetter(1)) # sorted by value, return a list of tuples
#print(components_sorted_by_frequency)
top_components = components_sorted_by_frequency[-10:]
print(top_components)

x, y = zip(*top_components) # unpack a list of pairs into two tuples

#plt.plot(x, y)
#plt.show()

plt.xticks(range(len(top_components)), x, rotation=45) #writes strings with 45 degree angle
plt.bar(range(len(top_components)),y)
plt.show()
