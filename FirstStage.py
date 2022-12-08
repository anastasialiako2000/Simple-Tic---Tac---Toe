ans = input("Enter a string with 9 symbols ")
i = 0
while(len(ans)!=9):
    ans = input("You have to enter 9 symbols ")
while(i<=8):
    while(ans[i]!="X" and ans[i]!="O" and ans[i]!="_"):
        ans = input("You have to enter X symbols ")
        while(len(ans)!=9):
            ans = input("You have to enter 9 symbols ")
    i+=1

grid = [[ ans[0], ans[1], ans[2] ], [ans[3], ans[4], ans[5] ], [ ans[6], ans[7], ans[8] ]]


print("---------")
print("| " + " ".join(grid[0]) + " |")
print("| " + " ".join(grid[1]) + " |")
print("| " + " ".join(grid[2]) + " |")
print("---------")

prob = True
area = ["1", "2", "3"]
while(prob==True):
    move = input()
    while(move[0].isnumeric() == False or move[2].isnumeric()==False):
        move = input("You should enter numbers! ")
    while((move[0] not in area ) or (move[2] not in area)):
        move= input("Coordinates should be from 1 to 3! ")
        while(move[0].isnumeric() == False or move[2].isnumeric()==False):
            move = input("You should enter numbers! ")

    row = move[0] #to sygrinw me grid[0] , grid[1], grid[2]
    column = move[2] #to sugrinw me deutero stoiexeio tou grid dld grid[0][0],



    if(int(row) == 1):
        firstin = 0
    elif(int(row) == 2):
        firstin = 1
    elif(int(row)==3):
        firstin = 2

    if(int(column) == 1):
        secondin = 0
    elif(int(column) == 2):
        secondin = 1
    elif(int(column)==3):
        secondin = 2

    if(grid[firstin][secondin] == "X" or grid[firstin][secondin]== "O"):
        print("This cell is occupied! Choose another one!")
        prob = True
    else:
        grid[firstin][secondin] = "X"
        prob =False
        print("---------")
        print("| " + " ".join(grid[0]) + " |")
        print("| " + " ".join(grid[1]) + " |")
        print("| " + " ".join(grid[2]) + " |")
        print("---------")









i=0
winsx=0
winso=0
countX = 0
countO = 0
countempty = 0
flag = -1
#while(flag!=1):
while(i<len(ans)):
    if(ans[i] == "X"):
        countX += 1
    elif(ans[i] == "O"):
        countO+=1
    else:
        countempty+=1
    i+=1



if (grid[0] =="X" or grid[1] =="X" or grid[2]=="X" or
    ans[0] == ans [3] == ans[6] =="X" or ans[1]==ans[4]==ans[7] == "X" or ans[2]==ans[5]==ans[8]=="X" or
    ans[2] == ans[4] == ans[6] == "X" or ans[0] == ans[4] == ans[8] == "X"):
        winsx +=1
#       print("X wins")
        flag = 1
#       break
if( grid[0] == "O" or grid[1] == "O" or grid[2] == "O" or
    ans[0] == ans [3] == ans[6] == "O" or ans[1] == ans[4] == ans[7] == "O" or ans[2] == ans[5] == ans[8] == "O" or
    ans[2] == ans[4] == ans[6] == "O" or ans[0] == ans[4] == ans[8] == "O"):
        winso+=1
#        print("O wins")
        flag = 1
#        break

if((winsx==1 and winso==1) or abs(countX-countO)>=2):
    print("Impossible")
#    break
elif(winsx == 1):
    print("X wins")
#    break
elif(winso==1):
    print("O wins")
#    break
elif(countempty == 0 and (countX == countO or countX == countO +1 or countX + 1 == countO)):
    print("Draw")
#    break
elif(countempty>0 and (countX == countO or countX == countO +1 or countX + 1 == countO)):
    print("Game not finished")
    flag=1
#    break





