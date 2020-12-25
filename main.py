"""
author: Mina Emad Lotfy
Group : IS_DS 4
ID    : 20170309
"""
import pandas as pd
import random
import numpy
import numbers
import math

from numpy import double, longdouble, longlong
from xlrd import open_workbook


def laoding_file(filename):
    filedata = pd.read_excel(filename)
    students = list()
    for i in range(0, 150):
        students.append([filedata.values[i, j] for j in range(0, 21)])
    return students

def Distance_Calculator (centriod, students):
    diffrance_list=[]
    summ=0.0
    distance=0.0
    distance_list=[]
    for i in range(0,len(centriod)):
        for j in range (1, len(students)):
            x=longdouble(centriod[i][j])
            y=longdouble(students[j])
            diff= y - x
            pow_diff= diff ** 2
            diffrance_list.append(pow_diff)
        summ=sum(diffrance_list)
        distance=math.sqrt(summ)
       # print(distance)
        distance_list.append(distance)
        diffrance_list.clear()
    #print(distance_list)
    return distance_list

def Center_In_Cluster (students_cluster):
    t=zip(*students_cluster)
    tlist=[]
    for s in t:
        tlist.append(list(s))
    newcentriod=[]
    for i in range(len(tlist)):
        newcentriod.append(sum(tlist[i])/len(tlist[i]))
    return(newcentriod)

def chechequality(oldcluster,newcluster):
    if oldcluster==newcluster:
        return True
    else:
        return False

# --------------------------------------------------------------------------------
"""
wb = open_workbook('Course Evaluation.xls')
for s in wb.sheets():
    students = []
    for row in range(s.nrows):
        col_value = []
        for col in range(3, 6):
            value = (s.cell(row, col).value)
            try:
                value = str(int(value))
            except:
                pass
            col_value.append(value)
        students.append(col_value)

"""
students = laoding_file("Course Evaluation.xls")

#print(students)


k=int(input("Enter Number of clusters =>"))

first_Centriod=random.sample(students, k)
#print(first_Centriod)

stud_clusterd_list=list()

for s in students:
    x= Distance_Calculator(first_Centriod, s)

    numofcluster= (x.index(min(x))) + 1
    stud_clusterd_list.append((s, numofcluster))

#print(stud_clusterd_list)

clusters=list()
for i in range (0,k):
    clusters.append([])

for i in range(0,len(clusters)):
    for s, numofcluster in stud_clusterd_list:
        if numofcluster==i+1:
            clusters[i].append(s)
#firstcluster ^

oldcluster=list()
newcluster=list()
newCentriods=list()
for c in clusters:     
    newCentriods.append(Center_In_Cluster(c))
for s in students:
    x= Distance_Calculator(newCentriods, s)
    numofcluster= (x.index(min(x))) + 1
    oldcluster.append((s, numofcluster))


for k in clusters:
    k.clear()   
for i in range(0,len(clusters)):
    for s, numofcluster in oldcluster:
        if numofcluster==i+1:
            clusters[i].append(s)
newCentriods.clear()
for c in clusters:     
    newCentriods.append(Center_In_Cluster(c))
for s in students:
    x= Distance_Calculator(newCentriods, s)
    numofcluster= (x.index(min(x))) + 1
    newcluster.append((s, numofcluster))

while (chechequality(oldcluster, newcluster) != True):
    oldcluster.clear()
    newcluster.clear()
    for c in clusters:     
        newCentriods.append(Center_In_Cluster(c))
    for s in students:
        x= Distance_Calculator(newCentriods, s)

        numofcluster= (x.index(min(x))) + 1
        oldcluster.append((s, numofcluster))


    for k in clusters:
        k.clear()   
    for i in range(0,len(clusters)):
        for s, numofcluster in oldcluster:
            if numofcluster==i+1:
                clusters[i].append(s)
    newCentriods.clear()
    for c in clusters:     
        newCentriods.append(Center_In_Cluster(c))
    for s in students:
        x= Distance_Calculator(newCentriods, s)
        numofcluster= (x.index(min(x))) + 1
        newcluster.append((s, numofcluster))

#print(newcluster)
for i in range(0,len(clusters)):
    clen=len(clusters[i])
    print("Cluster",i+1)
    print("============")
    for j in range(0,clen):
        print(clusters[i][j][0])

