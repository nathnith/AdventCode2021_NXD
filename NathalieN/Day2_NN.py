from typing import List
import math

f = open('Input_02.txt', 'r')

# depth=0
# horizontal=0
# counter=0
# for a in f:
#     counter +=1
#     line=a.split()
#     if line[0] == "forward":
#         horizontal += int(line[1])
#     elif line[0] == "up":
#         depth -= int(line[1])
#     elif line[0] == "down":
#         depth += int(line[1])
#     else:
#         print ("no change")
#
# print ("counter=", counter)
# print ("depth=", depth)
# print ("horizontal=", horizontal)
# answer=depth*horizontal
# print ("Part 1: ", answer)
# print()

## part 2

depth=0
horizontal=0
counter2=0
aim=0
for b in f:
    counter2 +=1
    line=b.split()
    if line[0] == "forward":
        horizontal += int(line[1])
        depth += (aim*int(line[1]))
    elif line[0] == "up":
        aim -= int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    else:
        print ("no change")
    print("a: ", aim)
    print("d: ",depth)
    print("h: ",horizontal)
    print()

print ("counter=", counter2)
print ("depth=", depth)
print ("horizontal=", horizontal)
answer=depth*horizontal
print ("Part 2: ", answer)
