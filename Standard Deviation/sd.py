import csv
import math

with open('C:/Users/v0788/Desktop/Python/Standard Deviation/data.csv', newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
squiredList=[]
for number in data:
    a = int(number) - mean(data) 
    a= a**2 
    squiredList.append(a) 
    
#getting sum 
sum =0 
for i in squiredList: 
    sum =sum + i 
#dividing the sum by the total values 
result = sum/ (len(data)-1) 
# getting the deviation by taking square root of the result 
std_deviation = math.sqrt(result) 
print(std_deviation) 
# print("derived using predefined function ",statistics.stdev(data)) 