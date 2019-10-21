import csv
import math
from operator import itemgetter
import random

'''
with open("knn_train.csv","r") as f:
    reader = csv.reader(f)
  
    features = next(reader)
    # print(features)
  
    DataList = []
    for row in reader:
        DataList += [row]
        print(row)
'''

def manhattanDistance(list1, list2):

    if len(list1) != len(list2):
        raise Exception('Length of Lists are not equal')
    
    distance = 0
    for i in range(len(list1)-1):
        distance += abs(int(list1[i+1]) - int(list2[i+1]))
        
    return distance

def euclideanDistance(list1, list2):

    if len(list1) != len(list2):
        raise Exception('Length of Lists are not equal')

    distance = 0
    for i in range(len(list1)-1):
        distance += pow((int(list1[i+1]) - int(list2[i+1])), 2)

    return math.sqrt(distance)

def maxNormDistance(list1, list2):
    
    if len(list1) != len(list2):
        raise Exception('Length of Lists are not equal')

    distance = []
    for i in range(len(list1)-1):
        distance.append(abs(int(list1[i+1]) - int(list2[i+1])))

    return max(distance)

#testData1 = DataList[1].copy()
#testData2 = DataList[2].copy()
#testData1 .remove('4000')

#print(testData1)
#print(testData2)

#x = euclideanDistance(testData1, testData2)
#print(x)

def kNearestNeighbors(trainingSet, testInstance, k):
    '''
    with open("knn_train.csv","r") as f:
        reader = csv.reader(f)
        features = next(reader)
        # print(features)
  
        DataList = []
    '''

    distanceList = []
        
    #Finds distances of testValue to TrainingSet
    for i in trainingSet:
        dist = euclideanDistance(testInstance, i)
        #print(dist)
        distanceList.append((i[0], dist))
    
    #print(distanceList)

    #Sort for nearest distances to get neighbors
    x = sorted(distanceList, key=itemgetter(1))
        
    neighbors = []
        
    for i in range(k):
        neighbors.append(x[i])

    return neighbors

def prediction(neighbors):
    counter = 0

    for i in neighbors:
        counter += int(i[0])
   
    #print(counter)
    if counter == 0:
        return random.choice((-1, 1))
    elif counter > 0:
        return 1
    else:
        return -1
    
def main():

    with open("knn_train.csv","r") as f:
        reader = csv.reader(f)
        features = next(reader)
        # print(features)
  
        DataList = []

        for row in reader:
            DataList += [row]
        
        #testData1 = DataList[1].copy()
        #testData2 = DataList[2].copy()
        #testData1 .remove('4000')

        #print(testData1)
        #print(testData2)

        #euclidianTest = euclideanDistance(testData1, testData2)
        #print(euclidianTest)
        
        #manhattanTest = manhattanDistance(testData1, testData2)
        #print(manhattanTest)

        #maxNormTest = maxNormDistance(testData1, testData2)
        #print(maxNormTest)

        testInstance = ['1','2','9','2250','22']
        x = kNearestNeighbors(DataList, testInstance, 4)
        #print(x)

        result = prediction(x)
        #print(result)
    
if __name__ == "__main__":
    main()
