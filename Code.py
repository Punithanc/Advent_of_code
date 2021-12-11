# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:10:52 2021

@author: 20200463
"""
#%%1a_comapring subsequent measurement

with open("day1_input_data.txt") as f:
    lst = [int(x) for x in f.read().split()]
j=0
for i in range(len(lst)-1):
    a=lst[i+1]-lst[i]
    if a>0:
       j=j+1
print("There are",j,"measurements that are larger than the previous measurement.")

#%%1b_measurement window size=3

with open("day1_input_data.txt") as f:
    lst = [int(x) for x in f.read().split()]
j=0
for i in range(len(lst)-3):
    a=lst[i+3]-lst[i]
    if a>0:
       j=j+1
print("There are",j,"measurements that are larger than the previous measurement.")

#%%2a_submarine movement

f2 = open('day2_input_data.txt', 'r') 
lines = f2.readlines()
command = []
distance = [] 
for line in lines:
    p = line.split()
    command.append((p[0]))
    distance.append((int(p[1])))
f2.close() 

horizontal=0
depth=0

for i in range(len(command)):
    if command[i]=="forward":
        horizontal=horizontal+distance[i]
    elif command[i]=="down":
        depth=depth+distance[i]
    elif command[i]=="up":
        depth=depth-distance[i]
print("The result is", horizontal*depth)

#%%2b_aim

f2 = open('day2_input_data.txt', 'r') 
lines = f2.readlines()
command = []
distance = [] 
for line in lines:
    p = line.split()
    command.append((p[0]))
    distance.append((int(p[1])))
f2.close() 

horizontal=0
depth=0
aim=0

for i in range(len(command)):
    if command[i]=="forward":
        horizontal=horizontal+distance[i]
        depth=depth+aim*distance[i]
    elif command[i]=="down":
        aim=aim+distance[i]
    elif command[i]=="up":
        aim=aim-distance[i]
print("The result is", horizontal*depth)
 
#%%3a_binary_gamma&epsilon rate
import numpy as np
a=np.loadtxt('day3_input_data.txt',dtype=str)
gamma=[]
epsilon=[]
gammadecimal=0
epsilondecimal=0
for i in range(len(a[0])):
    countzero=0
    countone=0
    for j in range(len(a)):
        if a[j][i]=='0':
            countzero=countzero+1
        else:
            countone=countone+1
    if countzero>countone:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

print("gamma is",gamma,"epsilon is",epsilon)

for k in range(len(gamma)):
    gammadecimal=gammadecimal+gamma[-k-1]*(2**k)
    
for l in range(len(epsilon)):
    epsilondecimal=epsilondecimal+epsilon[-l-1]*(2**l)

print("The power consumption of the submarine is",gammadecimal*epsilondecimal)

#%%3b_life support rating
import time
start=time.time()
import numpy as np
a=np.loadtxt('day3_input_data.txt',dtype=str)    
o2,co2=a,a

for i in range(len(o2[0])):
    countzero=0
    countone=0
    i_index=[]
    j_index=[]
    for j in range(len(o2)):
        if o2[j][i]=='0':
            countzero+=1
            i_index.append(j)
        else:
            countone+=1
            j_index.append(j)
    if countzero>countone:
        o2=o2[i_index]
    elif countzero<countone or countzero==countone:
        o2=o2[j_index]
print("The O2 scrubber is",o2)


for i in range(len(co2[0])):
    countzero=0
    countone=0
    i_index=[]
    j_index=[]
    for j in range(len(co2)):
        if co2[j][i]=='0':
            countzero+=1
            i_index.append(j)
        
        elif co2[j][i]=='1':
            countone+=1
            j_index.append(j)
    if len(co2) !=1:   
        if countzero>countone:
            co2=co2[j_index]
        elif countzero<countone or countzero==countone:
            co2=co2[i_index]
print("The CO2 scrubber is",co2)
o2=list(o2)
o2=int(o2[0],2)
co2=list(co2)
co2=int(co2[0],2)
print("life support rating is",co2*o2)
end=time.time()
print(end-start)