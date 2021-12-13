from typing import List
#import numpy as np

f = open('Input_03.txt', 'r')
gamma=[]
epsi=[]
# pk=gamma*epsi
commonbit=[[],[],[],[],[],[],[],[],[],[],[],[]]
for a in f:
    bits=[i for i in str(a)]
    for b in range(12):
        commonbit[b].append(bits[b])

for c in range(12):
    nzeros=commonbit[c].count("0")
    nones=commonbit[c].count("1")
    print(f"Bit: {c}, Zeros: {nzeros}, Ones: {nones}:" )
    if nzeros>nones:
        gamma.append(0)
        epsi.append(1)
    else:
        gamma.append(1)
        epsi.append(0)
gamma_int=int("".join([str(integer) for integer in gamma]),2)
epsi_int=int("".join([str(integer) for integer in epsi]),2)

print(f"Gamma: {gamma}")
print(f"Epsilon: {epsi}")

print(f"Gamma ickebinärt: {gamma_int}")
print(f"Epsilon ickebinärt: {epsi_int}")
print ("power= ", gamma_int*epsi_int)

## part 2

f = open('Input_03.txt', 'r')
gamma=[]
epsi=[]
# pk=gamma*epsi
commonbit=[]
commonbit_ox=[]
commonbit_os=[]


for a in f:
    bits=[i for i in str(a)]
    commonbit.append(bits[:-1])

def check_common(data,max_min, bit):
    data_zero=[]
    data_one=[]
    n_one=0
    n_zero=0
    for c in range(len(data)):
        if data[c][bit]=="0":
            n_zero += 1
            data_zero.append(data[c])
        else:
            n_one += 1
            data_one.append(data[c])
    if n_zero > n_one:
        commonbit_ox=data_zero
        commonbit_os=data_one
    else:
        commonbit_ox=data_one
        commonbit_os=data_zero
    if max_min=="max":
        data_out=commonbit_ox
    else:
        data_out=commonbit_os
    return data_out

commonbit_newOX=commonbit
commonbit_newOS=commonbit


for d in range(len(bits)):
    if len(commonbit_newOX)>1:
        commonbit_newOX=check_common(commonbit_newOX, "max", d)
    if len(commonbit_newOS) > 1:
        commonbit_newOS=check_common(commonbit_newOS, "min", d)

print()
print("Part2:")
print(commonbit_newOX)
print(commonbit_newOS)


OX_int=int("".join("".join([str(integer) for integer in commonbit_newOX[0]])),2)
OS_int=int("".join("".join([str(integer) for integer in commonbit_newOS[0]])),2)

print(OX_int)
print(OS_int)
print ("LS= ", OX_int*OS_int)


print()

