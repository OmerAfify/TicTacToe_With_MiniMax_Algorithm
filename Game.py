

board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}

player = 'O'
ai = 'X'

#Print the boards shape
def printBoard(board):
        print("----------")
        print(board[1] + " | "+ board[2]+ " | "+ board[3])
        print(board[4] + " | "+ board[5]+ " | "+ board[6])
        print(board[7] + " | "+ board[8] +" | "+ board[9])
        print("----------")

#check if there is a win or not
def isWinner (board):
    #rows win
    if board[1]==board[2] and board[1]==board[3] and board[1]!=' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4]!=' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7]!=' ':
        return True

    #diag wins
    elif board[1] == board[5] and board[1] == board[9] and board[1]!=' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3]!=' ':
        return True

    #columns win
    elif board[1] == board[4] and board[1] == board[7] and board[1]!=' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2]!=' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3]!=' ':
        return True
    else:
        return False

#check if there is a draw or not, used only inside playIn()
def isDraw(board):

    if isWinner(board)==False:
        for x in board:
            if isFreePos(board,x):
                return False
        return True

#check that the sepeciifiec pos is free or not
def isFreePos(board, position):
    if board[position]==' ':
        return True
    else:
        return False

#plays a token in a FREE Space + checks for wins or draws
def playIn(board, position,token):
    if isFreePos(board, position)==True:
        board[position]=token
        printBoard(board)

        if isDraw(board) == True:
             print("Draw")
             exit(0)
        elif isWinner(board)==True:
            if token==ai:
                print("ai wins")
                exit(0)
            else:
                print("player wins")
                exit(0)

    else:
        print("Wrong Pos, please reenter position")
        pos = int(input())
        playIn(board,pos, token)


#PLayer's turn
def playerPlays(board):
    print("Please enter position from 1->9")
    pos = int(input())
    playIn(board,pos,player)

#ai's turn (random movement)
# def aiPlays(board):
#     r = randint(1,9)
#     while(isFreePos(board,r))==False:
#          r=randint(1,9)
#     playIn(board, r, ai)



#ai's turn (minmax movement)
def aiPlays(board):
   bestMove=-1
   bestscore=-100000

   for x in board:
        if board[x] == ' ':
            board[x]=ai
            score = minmax(board,0,False)
            board[x]=' '

            if score > bestscore:
                bestscore = score
                bestMove = x

   playIn(board,bestMove,ai)

####################################################   MINMAX  ######################################################################

def winner (board,mark):
    # rows win
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] ==mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] ==mark:
         return True

    # diag wins
    elif board[1] == board[5] and board[1] == board[9] and board[1] ==mark:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] ==mark:
         return True

    # columns win
    elif board[1] == board[4] and board[1] == board[7] and board[1] ==mark:
            return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] ==mark:
            return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] ==mark:
            return True
    else:
        return False


# it is a function that calculates the score of a specifiec move, assuming that the opps also plays optimally

# ex: ai plays a move (in the ai move inside the loop that plays all the moves)
#   : minimax plays considerisng its self the ai as well as the opp. playing the optimal ones and chooses the path that maximizes its score
def minmax(board, depth, isMaximizing):
    # terminal conditions to return final stae values , and keeps adding then recursively to the parents waiting values
    if winner(board,'X'):
        return 1
    elif winner(board,'O'):
        return -1
    elif isDraw(board) == True:
        return 0

#computers turn trying to win!!! maximize
    if(isMaximizing== True):
        bestscore = -100000
        for x in board:
            if  board[x] == ' ':
                board[x] = 'X'
                score = minmax(board,depth + 1, False)


                board[x] = ' '

                if score > bestscore:
                    bestscore = score;
        return bestscore
    else:
# palyers turn trying to win!!! minimizing Computers score
        bestscore = 100000
        for x in board:
            if board[x] == ' ':
                board[x] = 'O'
                score = minmax(board,depth+1, True)
                board[x] = ' '

                if score < bestscore:
                    bestscore = score
        return bestscore
##########################################################################################################################



#####################################  Alpha- beta prunning  #############################################################
#alpha beta prunning
def minmaxAlphaBetaPruning(board, depth, isMaximizing, alpha, beta):
#terminal conditions to return final stae values , and keeps adding then recursively to the parents waiting values
    if winner(board,'X'):
        return 1
    elif winner(board,'O'):
        return -1
    elif isDraw(board) == True:
        return 0

#computers turn trying to win!!! maximize
    if(isMaximizing== True):
        bestscore = -100000
        for x in board:
            if  board[x] == ' ':
                board[x] = 'X'
                score = minmaxAlphaBetaPruning(board,depth + 1, False,alpha,beta)
                board[x] = ' '

                if score > bestscore:
                    bestscore = score

                if(score>alpha):
                    alpha = score

                if alpha>= beta:
                    break

        return bestscore
    else:
# palyers turn trying to win!!! minimizing Computers score
        bestscore = 100000
        for x in board:
            if board[x] == ' ':
                board[x] = 'O'
                score = minmaxAlphaBetaPruning(board,depth+1, True, alpha, beta)
                board[x] = ' '

                if score < bestscore:
                    bestscore = score

                if (score < beta):
                    beta = score

                if alpha >= beta:
                    break


        return bestscore
#####################################################################################################################################


#Start Game
def StartGame(board):
    while not isWinner(board):
        aiPlays(board)
        playerPlays(board)



#main
StartGame(board)
#StartGame(board)


