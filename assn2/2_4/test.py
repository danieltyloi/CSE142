
import csv

with open("knn_train.csv","r") as f:
  reader = csv.reader(f)
  features = next(reader)
  print(features)
  for row in reader:
    print(row)



