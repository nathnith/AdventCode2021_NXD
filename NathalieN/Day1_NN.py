from typing import List
import math

depth=[]
depth_diff: List[int]=[]
a_prev=0
f = open('Input_01.txt', 'r')
for a in f:
    depth.append(int(a))
    depth_diff.append(int(a)- int(a_prev))
    a_prev=a

print (depth_diff)
total_increase=0

for b in depth_diff[1:]:
    if b>0:
        total_increase+=1


print (total_increase)
print()


## part 2
total_increase_new=0
sum_num=3
newdepth=0
newdepth_list=[]
newdepth_diff=[]
n1=0
n2=1
n3=2
olddepth=0
for c in range(len(depth)-2):
    newdepth=depth[n1]+depth[n2]+depth[n3]
    newdepth_list.append(newdepth)
    newdepth_diff=newdepth-olddepth
    if newdepth_diff>0:
        total_increase_new+=1
    olddepth=newdepth
    n1+=1
    n2+=1
    n3+=1

print (total_increase_new-1)
