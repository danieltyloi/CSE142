import csv

# Return the euclidean distance from any two feature vectors.
# Note: converts element in lists s1 and s2 to ints
def euclideanDistance(s1, s2):
	runningSum = 0
	for a, b in zip(s1, s2):
		runningSum += (int(a) - int(b)) ** 2
	return runningSum ** (1/2)

# given a training file and a test instance, return a list with of 
# distances from test instance to each training data instance and 
# its label. [(label, distance)..]
def getDistanceList(filename, testInstance):
	with open(filename) as csvFile:
		trainingData = csv.reader(csvFile, delimiter=',')
		distanceList = []
		#flag used to skip the first row in trainingData
		flag = True
		for row in trainingData:
			if flag:
				flag = False
				continue
			trainLabel = row[0]
			trainVector = row[1:]
			testVector = testInstance[1:]
			dist = euclideanDistance(trainVector, testVector)
			distanceList.append((trainLabel, dist))
		return distanceList

# given a k and a sorted distance list return the predicted label 
def kNearest(k, distanceList):
	predictedLabel = 0
	for i in range(k):
		instance = distanceList[i]
		predictedLabel += int(instance[0])
	return (-1 if predictedLabel < 0 else 1)

def main():
	testInstance = ['-1','1','24','6000','77']
	fileName = 'knn_train.csv'
	dlist = sorted(getDistanceList(fileName, testInstance), key=lambda a: a[1])
	x = kNearest(50, dlist)
	print(x)

if __name__ == "__main__":
	main()