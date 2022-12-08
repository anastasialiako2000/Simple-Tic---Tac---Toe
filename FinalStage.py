ans = []
i = 0
while(i<9): #full the part of the table with " "
    ans.insert(i," ")
    i+=1

grid = [[ ans[0], ans[1], ans[2] ], [ans[3], ans[4], ans[5] ], [ ans[6], ans[7], ans[8] ]]


print("---------")
print("| " + " ".join(grid[0]) + " |")
print("| " + " ".join(grid[1]) + " |")
print("| " + " ".join(grid[2]) + " |")
print("---------")




winsx=0 #count win times of X player
winso=0 #count win times of O player


a=0 #to change the player, first X player then O player
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


# I find from the first digit of the cell that the player enters which row of the table represents
    if(int(row) == 1):
        firstin = 0
    elif(int(row) == 2):
        firstin = 1
    elif(int(row)==3):
        firstin = 2

#I find from the second digit of the cell that the player enters which column of the table represents
    if(int(column) == 1):
        secondin = 0
    elif(int(column) == 2):
        secondin = 1
    elif(int(column)==3):
        secondin = 2

    if(grid[firstin][secondin] == "X" or grid[firstin][secondin]== "O"): #check if its already full
        print("This cell is occupied! Choose another one!")
        prob = True
    else:
        if(a%2 == 0):
            grid[firstin][secondin] = "X"
            a+=1
        else:
            grid[firstin][secondin] = "O"
            a+=1

        print("---------")
        print("| " + " ".join(grid[0]) + " |")
        print("| " + " ".join(grid[1]) + " |")
        print("| " + " ".join(grid[2]) + " |")
        print("---------")



    countO=0 #helps to check the case for impossible
    countX =0 #helps to check the case for impossible
    countempty =0 #helps to check the case for Draw
    i=0
    while(i<3):
        j=0
        while(j<3):
            if(grid[i][j] == "X"):
                countX += 1
                j+=1
            elif(grid[i][j] == "O"):
                countO+=1
                j+=1
            else:
                countempty+=1
                j+=1
        i+=1

#check if X wins
    if (all(x == "X" for x in grid[0]) or all(x == "X" for x in grid[1]) or all(x == "X" for x in grid[2]) or
        grid[0][0] ==grid[1][0] == grid[2][0] =="X" or grid[0][1]==grid[1][1]==grid[2][1] == "X" or grid[0][2]==grid[1][2]==grid[2][2]=="X" or
        grid[0][2] == grid[1][1] == grid[2][0] == "X" or grid[0][0] == grid[1][1] == grid[2][2] == "X"):
            winsx +=1
            print(winsx)
#check if O wins
    if( all(x == "O" for x in grid[0])  or all(x == "O" for x in grid[1]) or all(x == "O" for x in grid[2]) or
        grid[0][0] ==grid[1][0] == grid[2][0] =="O" or grid[0][1]==grid[1][1]==grid[2][1] == "O" or grid[0][2]==grid[1][2]==grid[2][2]=="O" or
        grid[0][2] == grid[1][1] == grid[2][0] == "O" or grid[0][0] == grid[1][1] == grid[2][2] == "O"):
            winso+=1
#Check if its impossible, if both players win or there are much more X than O and vice versa
    if((winsx==1 and winso==1) or abs(countX-countO)>=2):
        print("Impossible")
        break
    elif(winsx == 1):
        print("X wins")
        break
    elif(winso==1):
        print("O wins")
        break
    elif(countempty == 0 and (countX == countO or countX == countO +1 or countX + 1 == countO)):
        print("Draw")
        break






