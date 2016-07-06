import random, datetime

# establish start time
start = datetime.datetime.now()

# various test cases
# testarr = [8,7,6,5,4,3,2,1]
# testarr = [8,3,6,1,2,5,4,7]
# testarr = [1,2,3,4,5,6,7,8]
# testarr = []

# generate array of 100 elements, randomized in range 0 - 10,000
testarr = []
for x in range (100):
	testarr.append(int(round(random.random()*10000)))

# itinialize a swap variable
temp = 0

# sort algorithm
def bubble_sort(arr):
	# max_ndx will decrement as the sorted portions are moved to the end of the array
	max_ndx = len(arr)
	while max_ndx > 0:
		for i in range(0,max_ndx-1):
			# test the bubble and swap if need be
			if arr[i] > arr[i+1]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
			# un-comment for troubleshooting - prints after each iteration
			# print arr
		max_ndx = max_ndx-1
	return arr

# call the sort function and print the results
print bubble_sort(testarr)

# calculate and print elapsed time
print "It took: ", datetime.datetime.now() - start