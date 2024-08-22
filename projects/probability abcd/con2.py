import random
import csv

pc = [1,2,3,4]

def onlyC (num):
    counter = 0
    for num in range(num):
        if pc[random.randrange(0, 4)] == 3:
            counter +=1
    return (counter/num *100)
    

onlyC(20)

def abcd (num):
    abcd = [1,2,3,4]
    counter = 0
    idx = 0
    for num in range(num):
        if pc[random.randrange(0, 4)] == abcd[idx]:
            counter +=1
        idx += 1
        if idx <3:
            idx = 0
    return (counter/num *100)

l1 = [onlyC(random.randrange(10, 500)) for _ in range(500)] 
l2 = [abcd(random.randrange(10, 500)) for _ in range(500)] 

def comparer(list1, list2):
    avg1 = sum(list1) / len(list1) if list1 else 0
    avg2 = sum(list2) / len(list2) if list2 else 0
    print(str(avg1), '\n', str(avg2))

comparer(l1,l2)

with open('table7.csv', 'w', encoding='UTF-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["Only C Percentages", "ABCD Percentages"])
    for val1, val2 in zip(l1, l2):
        writer.writerow([val1, val2])


Cbetter = 0
abcdbetter = 0

for idx in range(len(l1)):
    if l1[idx] > l2[idx]:
        Cbetter += 1
    else: abcdbetter += 1

print(Cbetter)
print(abcdbetter)