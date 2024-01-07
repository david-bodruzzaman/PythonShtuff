"""
Requirements

How to Store Data

Dictionary list 

x o : a b ,0 1


"""

# positions = {
#   "a1":None,
#   "a2":None,
#   "a3":None,
#   "b1":None,
#   "b2":None,
#   "b3":None,
#   "c1":None,
#   "c2":None,
#   "c3":None,
# }

openPositions = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
player1 = []
player2 = []
currentPlayer = "player1"
count = 1
loopFlag = True
while loopFlag:
    choicePos =  input(f"""what position does you want to put?
                    {openPositions[0]} | {openPositions[1]} | {openPositions[2]}
                    {openPositions[3]} | {openPositions[4]} | {openPositions[5]}
                    {openPositions[6]} | {openPositions[7]} | {openPositions[8]}
                       """)
    for index, item in enumerate(openPositions):
        print(index)
        if item == choicePos:
            # print(f"{openPositions[index]} Position")
            # openPositions[index] = "x"

            # Check To see if someone has won
            if (count%2 ==0):
                player2.append(choicePos)
                openPositions[index] = "x"
                if(("a1" in player2 and "a2" in player2 and "a3" in player2) or ("b1" in player2 and "b2" in player2 and "b3" in player2) or ("c1" in player2 and "c2" in player2 and "c3" in player2) or ("a1" in player2 and "b1" in player2 and "c1" in player2) or ("a2" in player2 and "b2" in player2 and "c2" in player2) or ("a3" in player2 and "b3" in player2 and "c3" in player2) or ("c1" in player2 and "b2" in player2 and "a3" in player2) or ("a1" in player2 and "b2" in player2 and "c3" in player2)):
                    print(f"""
                    {openPositions[0]} | {openPositions[1]} | {openPositions[2]}
                    {openPositions[3]} | {openPositions[4]} | {openPositions[5]}
                    {openPositions[6]} | {openPositions[7]} | {openPositions[8]}
                       """)
                    print("player2 wins")
                    loopFlag = False
                    break
                    
            else:
                player1.append(choicePos)
                openPositions[index] = "o"
                if(("a1" in player1 and "a2" in player1 and "a3" in player1) or ("b1" in player1 and "b2" in player1 and "b3" in player1) or ("c1" in player1 and "c2" in player1 and "c3" in player1) or ("a1" in player1 and "b1" in player1 and "c1" in player1) or ("a2" in player1 and "b2" in player1 and "c2" in player1) or ("a3" in player1 and "b3" in player1 and "c3" in player1) or ("c1" in player1 and "b2" in player1 and "a3" in player1) or ("a1" in player1 and "b2" in player1 and "c3" in player1)):
                    print(f"""
                    {openPositions[0]} | {openPositions[1]} | {openPositions[2]}
                    {openPositions[3]} | {openPositions[4]} | {openPositions[5]}
                    {openPositions[6]} | {openPositions[7]} | {openPositions[8]}
                       """)
                    print("player1 wins")
                    loopFlag = False
                    break
                    
    count+=1
