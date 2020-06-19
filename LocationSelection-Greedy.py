#################################################################################################################
# Case: Distribution Center Selection for Furniture Drop-ship Company
# Problem: The company wants to select p distribution center to cover n cities in the area.
# The distance that a DC can reach is d. If the distance between the DC and city is smaller
# then d, then the city is covered by the DC.
# The purpose is to select ideal cities to establish the DC and cover as many population as possible. 
#
# I'm using Greedy Algorithm to solve this problem. The algorithm will give selected DC cities, covered cities,
# and total covered population.
##################################################################################################################

# enter number of city, number of DCs and coverage distance
enter = input('n-cities, p-bases, d-distance:').split()
n = int(enter[0])
p = int(enter[1])
d = int(enter[2])

# load city's coordinate and population data
import csv

csv_file = open('Book1.csv','r')
reader = csv.reader(csv_file)
dst=[]
rowlist=[]
for row in reader:
    dst.append(row)

dst1=[]
for row in dst:
    row1=[]
    for i in row:
        row1.append(int(i))
    dst1.append(row1)

# if load coordinate data via mannual input:
# enter {x,y} and population of city i
#dst = []
#for i in range(n):
#    dst.append(input().split())   #after input.split, it becomes a list, and the list is appended to dst
#    for j in range(3):
#        dst[i][j] = int(dst[i][j])  # cover the elements to int in the list

import math

#calculate distance between cities
xyd = []
for x in range(n):
    dis = []
    for y in range(n):
        dis.append(float(math.sqrt((dst1[x][0]-dst1[y][0])**2+(dst1[x][1]-dst1[y][1])**2)))
    xyd.append(dis)
  
#for line in xyd:
#    print(line)

# create unselected city list
unslt = []
for i in range(n):
    unslt.append(i)
slt = []

# select DC using greedy algrithm
total_pop = 0
for i in range(p):
    # start with city 1 as DC city
    max_pop = 0
    base = 0
    dic = {}
    for city in unslt:
        pop = 0
        slt = []
    #pop = dst[city][2]  # coverage popultaion
        for a in unslt:
            if xyd[city][a] <= d:
                pop += dst1[a][2]  # total pop coverage of current base
               #print(city,a,pop)
                slt.append(a)    # list of covered city of current base
        if pop > max_pop:        # use greedy method to find base with max pop coverage
            max_pop = pop
            base = city
        #print('DC:'+str(city)+'coverage'+str(pop))
        dic[city] = slt
    print(base,dic[base],max_pop) # DC city, cover cities, coverage population 
    total_pop += max_pop
    for city in dic[base]:
        unslt.remove(city)
    #print(unslt)
print(total_pop)

