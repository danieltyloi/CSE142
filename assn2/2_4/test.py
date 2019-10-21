import csv
import math

with open("knn_train.csv","r") as f:
    reader = csv.reader(f)
  
    features = next(reader)
    # print(features)
  
    DataList = []
    for row in reader:
        DataList += [row]
        # print(row)

def euclideanDistance(length1, length2):

    if len(length1) != len(length2):
        raise Exception('Length of Lists are not equal')

    distance = 0
    for i in range(len(length1)-1):
        distance += pow((int(length1[i+1]) - int(length2[i+1])), 2)

    return math.sqrt(distance)

#testData1 = DataList[1].copy()
#testData2 = DataList[2].copy()
#testData1 .remove('4000')

#print(testData1)
#print(testData2)

#x = euclideanDistance(testData1, testData2)
#print(x)
