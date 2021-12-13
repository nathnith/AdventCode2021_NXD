f = open('Input4_small.txt', 'r')

Bnumb=(f.readline())
Bnumb=Bnumb[:-1].split(",")
print(Bnumb)
boards=[]
Bnum=0
Rown=1
bingoStatus=[]
for rowinput in f:
    if not rowinput.isspace():
        if Rown == 1:
            boards.append([])
            bingoStatus.append([])
        boards[Bnum].append(rowinput.split())
        Rown += 1
        if Rown == 6:
            Bnum+=1
            Rown = 1


def checkBingo(board):
    sumBoard=0
    bingo = False
    for row in board:
        valind_r = [index for index, row in enumerate(row) if "X" in row]
        if len(valind_r)==5:
            bingo=True
            sumBoard=sum_board(board)
    Tboard = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    for col in Tboard:
        valind_c = [index for index, col in enumerate(col) if "X" in col]
        if len(valind_c)==5:
            bingo=True
            sumBoard = sum_board(board)
    return [bingo, sumBoard]

def checknumber(board,number):
    valind=[[index, row.index(number)] for index, row in enumerate(board) if number in row]
    bstatus=[False, 0]
    if valind:
        board[valind[0][0]][valind[0][1]]="X"
        bstatus=checkBingo(board)
    return [board,bstatus]

def sum_board(board):
    sumboard=[]
    for row in board:
        nonmarkedindex = [index for index, row in enumerate(row) if "X" not in row]
        nonmarked=[int(row[i]) for i in nonmarkedindex]
        sumboard.append(sum(nonmarked))
    sumboard=sum(sumboard)
    return sumboard

print()
for bingoinput in Bnumb:
    c = 0
    for tile in boards:
        [boards[c],bingoStatus[c]]=checknumber(tile,bingoinput)
        if bingoStatus[c][0]==True:
            answ=bingoStatus[c][1]*int(bingoinput)
            break
        c += 1
    else:
        continue
    break

print(bingoStatus)
print ("ans part1: ", answ)


### Part 2

print()
print()
print("Part 2")
f = open('Input_04.txt', 'r')

Bnumb=(f.readline())
Bnumb=Bnumb[:-1].split(",")
print(Bnumb)
boards=[]
Bnum=0
Rown=1
bingoStatus=[]
for a in f:
    if not a.isspace():
        if Rown == 1:
            boards.append([])
            bingoStatus.append([])
        boards[Bnum].append(a.split())
        Rown += 1
        if Rown == 6:
            Bnum+=1
            Rown = 1

tempboards=boards
tempbstatus=bingoStatus
for bingoinput in Bnumb:
    c = 0
    boards=tempboards
    bingoStatus=tempbstatus
    tempboards=[]
    tempbstatus = []
    for tile in boards:
        [boards[c],bingoStatus[c]]=checknumber(tile,bingoinput)
        if len(boards)==1 and bingoStatus[c][0]==True:
            answ2 = bingoStatus[c][1] * int(bingoinput)
            break
        if bingoStatus[c][0]==False:
            tempboards.append(boards[c])
            tempbstatus.append(bingoStatus[c])
        c += 1
    else:
        continue
    break
print(bingoStatus)
print(boards)
print ("ans part2: ", answ2)