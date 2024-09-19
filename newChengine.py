import random

#BOARD####################################################
board = [ 
  [None ,'br1',None ,None ,None ,None ,'wr2',None ],
  [None ,None ,None ,None ,None ,None ,'wp7','wp8'],
  [None ,None ,'wp3',None ,'wk_',None ,None ,None ],  
  [None ,'bp3',None ,None ,None ,'bp7',None ,None ],
  ['bb2',None ,None ,None ,None ,'bb1',None ,'bp8'],
  [None ,None ,None ,None ,None ,'bk_',None ,None ],
  [None ,None ,None ,None ,None ,'bp6',None ,None ],
  [None ,None ,None ,'br2',None ,None ,None ,None ]
       ]
##########################################################


#MOVES#####################################################

def rook_move(x,y,grid,black = False,primary=True):
    color = 'w'
    if black:
        color = 'b'

    if grid[y][x] == None or grid[y][x][1] != 'r':
        return 'error wrong piece'
    moves = []
    illegal_moves = []
    for i in range(1,8):
        if (x+i > -1 and x+i <8):
            if grid[y][x+i] ==None:
                moves.append([x+i,y])
            elif grid[y][x+i][0] != grid[y][x][0]:
                moves.append([x+i,y])
                break
            else:
                break
    for i in range(1,8):
        if (x-i > -1 and x-i <8):
             if grid[y][x-i] ==None:
                moves.append([x-i,y])
             elif grid[y][x-i][0] != grid[y][x][0]:
                moves.append([x-i,y])
                break
             else:
                break
    for j in range(1,8):
        if (y+j > -1 and y+j <8):
             if grid[y+j][x] == None:
                moves.append([x,y+j])
             elif grid[y+j][x][0] != grid[y][x][0]:
                moves.append([x,y+j])
                break
             else:
                break
    for j in range(1,8):
        if (y-j > -1 and y-j <8):
            if grid[y-j][x] ==None:
                moves.append([x,y-j])
            elif grid[y-j][x][0] != grid[y][x][0]:
                moves.append([x,y-j])
                break
            else:
                break 
    if moves == []:
        return None 
    if primary:
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = color + 'rx'
            if checkCheck(possibleGrid,black):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def bishop_move(x,y,grid,black = False,primary=True):
    color = 'w'
    if black:
        color = 'b'

    if grid[y][x] == None or grid[y][x][1] != 'b':
        return 'error wrong piece'
    moves = []
    illegal_moves = []
    for i in range(1,8):
        if (x+i > -1 and y+i <8) and (x+i<8 and y+i>-1):
            if grid[y+i][x+i] ==None:
                moves.append([x+i,y+i])    
            elif grid[y+i][x+i][0] != grid[y][x][0]:
                moves.append([x+i,y+i])
                break
            else:
                break
    for i in range(1,8):
        if (x+i > -1 and y-i <8) and (x+i<8 and y-i>-1):
            if grid[y-i][x+i] ==None:
                moves.append([x+i,y-i])
            elif grid[y-i][x+i][0] != grid[y][x][0]:
                moves.append([x+i,y-i])
                break
            else:
                break
    for j in range(1,8):
        if (x-j > -1 and y+j <8) and (x-j<8 and y+j>-1):
             if grid[y+j][x-j] ==None:
                moves.append([x-j,y+j])
             elif grid[y+j][x-j][0] != grid[y][x][0]:
                moves.append([x-j,y+j])
                break
             else:
                break
    for j in range(1,8):
        if (x-j > -1 and y-j <8) and (x-j<8 and y-j>-1):
            if grid[y-j][x-j] ==None:
                moves.append([x-j,y-j])
            elif grid[y-j][x-j][0] != grid[y][x][0]:
                moves.append([x-j,y-j])
                break
            else:
                break
    if moves == []:
        return None 
    if primary:  
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = color + 'bx'
            if checkCheck(possibleGrid,black):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)
    
def queen_move(x,y,grid, black = False,primary=True):
    color = 'w'
    if black:
        color = 'b'
    if grid[y][x] == None or grid[y][x][1] != 'q':
        return 'error wrong piece'
    moves = []
    illegal_moves = []
    for i in range(1,8):
        if (x+i > -1 and x+i <8):
            if grid[y][x+i] ==None:
                moves.append([x+i,y])
            elif grid[y][x+i][0] != grid[y][x][0]:
                moves.append([x+i,y])
                break
            else:
                break
    for i in range(1,8):
        if (x-i > -1 and x-i <8):
             if grid[y][x-i] ==None:
                moves.append([x-i,y])
             elif grid[y][x-i][0] != grid[y][x][0]:
                moves.append([x-i,y])
                break
             else:
                break
    for j in range(1,8):
        if (y+j > -1 and y+j <8):
             if grid[y+j][x] == None:
                moves.append([x,y+j])
             elif grid[y+j][x][0] != grid[y][x][0]:
                moves.append([x,y+j])
                break
             else:
                break
    for j in range(1,8):
        if (y-j > -1 and y-j <8):
            if grid[y-j][x] ==None:
                moves.append([x,y-j])
            elif grid[y-j][x][0] != grid[y][x][0]:
                moves.append([x,y-j])
                break
            else:
                break 
    for i in range(1,8):
        if (x+i > -1 and y+i <8) and (x+i<8 and y+i>-1):
            if grid[y+i][x+i] ==None:
                moves.append([x+i,y+i])    
            elif grid[y+i][x+i][0] != grid[y][x][0]:
                moves.append([x+i,y+i])
                break
            else:
                break
    for i in range(1,8):
        if (x+i > -1 and y-i <8) and (x+i<8 and y-i>-1):
             if grid[y-i][x+i] ==None:
                moves.append([x+i,y-i])
             elif grid[y-i][x+i][0] != grid[y][x][0]:
                moves.append([x+i,y-i])
                break
             else:
                break
    for j in range(1,8):
        if (x-j > -1 and y+j <8) and (x-j<8 and y+j>-1):
             if grid[y+j][x-j] ==None:
                moves.append([x-j,y+j])
             elif grid[y+j][x-j][0] != grid[y][x][0]:
                moves.append([x-j,y+j])
                break
             else:
                break
    for j in range(1,8):
        if (x-j > -1 and y-j <8) and (x-j<8 and y-j>-1):
            if grid[y-j][x-j] ==None:
                moves.append([x-j,y-j])
            elif grid[y-j][x-j][0] != grid[y][x][0]:
                moves.append([x-j,y-j])
                break
            else:
                break
    if moves == []:
        return None 
    if primary:  
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = color + 'q_'
            if checkCheck(possibleGrid,black):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def king_move(x,y,grid, black = False,primary=True):
    color = 'w'
    if black:
        color = 'b'
    if grid[y][x] == None or grid[y][x][1] != 'k':
        return 'error wrong piece'
    moves = []
    illegal_moves = []
    for i in range(-1,2):
        for j in range(-1,2):
            if (x+i >-1) and (x+i<8) and (y+j >-1) and (y+j < 8):
                if grid[y+j][x+i] == None:
                    moves.append([x+i,y+j])
                elif grid[y+j][x+i][0] != grid[y][x][0]:
                    moves.append([x+i,y+j])
    if moves == []:
        return None 
    if primary:  
        illegal_moves = []
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = color + 'k_'
            if checkCheck(possibleGrid,black):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def knight_move(x,y,grid,black = False,primary=True):
    color = 'w'
    if black:
        color = 'b'    
    if grid[y][x] == None or grid[y][x][1] != 'n':
        return 'error wrong piece'
    possible_moves = [[2,1],[-1,2],[-2,-1],[1,-2],[1,2],[-2,1],[-1,-2],[2,-1]]
    moves = []
    illegal_moves = []
    for move in possible_moves:
        newGridPos_X = move[0] + x
        newGridPos_Y = move[1] + y
        if newGridPos_X < 0 or newGridPos_X > 7 or newGridPos_Y < 0 or newGridPos_Y > 7:
            continue
        if grid[newGridPos_Y][newGridPos_X] == None or grid[newGridPos_Y][newGridPos_X][0] != grid[y][x][0]:
            moves.append([newGridPos_X,newGridPos_Y])
    if moves == []:
        return None 
    if primary:  
        illegal_moves = []
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = color +'nx'
            if checkCheck(possibleGrid,black):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def pawn_move(x,y,grid,black = False,primary=True):
    color = 'w'
    if black:
        color = 'b'    
    if grid[y][x] == None or grid[y][x][1] != 'p':
        return 'error wrong piece'
    illegal_moves = []
    

    if black:
        capture_moves = [[1, -1], [-1, -1]]
        moves = []
        if(y == 6):
            newGridPos_Y = 4
            if grid[4][x] == None and grid[5][x] == None :
                moves.append([x,4])

        newGridPos_Y = y-1
        if newGridPos_Y > -1 and newGridPos_Y < 8:
            if grid[newGridPos_Y][x] == None:
                moves.append([x,newGridPos_Y ])

        for move in capture_moves:
            newGridPos_X = move[0] + x
            newGridPos_Y = move[1] + y

            if newGridPos_X < 0 or newGridPos_X > 7 or newGridPos_Y < 0 or newGridPos_Y > 7:
                continue

            if grid[newGridPos_Y][newGridPos_X]!= None and grid[newGridPos_Y][newGridPos_X][0] == 'w':
                moves.append([newGridPos_X, newGridPos_Y])
        if moves == []:
            return None

    else:
        capture_moves = [[1, 1], [-1, 1]]
        moves = []
        illegal_moves = []
        if(y == 1):
            if grid[3][x] == None and grid[2][x] == None :
                moves.append([x,3])

        newGridPos_Y = 1 + y
        if newGridPos_Y > -1 and newGridPos_Y < 8:
            if grid[newGridPos_Y][x] == None:
                moves.append([x,newGridPos_Y])

        for move in capture_moves:
            newGridPos_X = move[0] + x
            newGridPos_Y = move[1] + y
            if newGridPos_X < 0 or newGridPos_X > 7 or newGridPos_Y < 0 or newGridPos_Y > 7:
                continue
            if grid[newGridPos_Y][newGridPos_X]!= None and grid[newGridPos_Y][newGridPos_X][0] == 'b':
                moves.append([newGridPos_X, newGridPos_Y])
    if moves == []:
        return None 
    
    if primary:  
          for move in moves:
              possibleGrid = gridCopy(grid)
              possibleGrid[y][x] = None
              possibleGrid[move[1]][move[0]] = color +'px'
              if checkCheck(possibleGrid,black):
                  illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

##########################################################


#HELPERS##################################################

def checkCheck(grid,black = False):

    color = 'w'
    if black:  
        color = 'b'
    kx = -1
    ky = -1

    for i in range(8):
        for j in range(8):
            if grid[i][j] != None:
                if grid[i][j][0] == color and grid[i][j][1] == 'k':
                    kx, ky = j, i  

    possible_moves = []
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None and grid[i][j][0] != color:
                    if grid[i][j][1] == 'r':
                        if rook_move(j,i,grid,not black,False) != None:
                            possible_moves.append(rook_move(j,i,grid,not black,False))
                    if grid[i][j][1] == 'n':
                        if knight_move(j,i,grid,not black,False) != None:
                            possible_moves.append(knight_move(j,i,grid,not black,False))
                    if grid[i][j][1] == 'b':
                        if bishop_move(j,i,grid,not black,False) != None:
                            possible_moves.append(bishop_move(j,i,grid,not black,False))
                    if grid[i][j][1] == 'k':
                        if king_move(j,i,grid,not black,False) != None:
                            possible_moves.append(king_move(j,i,grid,not black,False))
                    if grid[i][j][1] == 'q':
                        if queen_move(j,i,grid,not black,False) != None:
                            possible_moves.append(queen_move(j,i,grid,not black,False))
                    if grid[i][j][1] == 'p':
                        if pawn_move(j,i,grid,not black,False) != None:
                            possible_moves.append(pawn_move(j,i,grid,not black,False))
    for move_list in possible_moves:
        if move_list != None:
            if [kx, ky] in move_list:
                return True

    return False

def checkMateCheck(grid,black=False):
    if (len(everyLegalBoard(grid,black)) == 0):
        if (checkCheck(grid,black)):
            return 'checkmate'
        else:
            return 'stalemate'
    return 'KeepPlaying'


def gridCopy(grid):
    retgrid = [ 
  [None, None, None, None,  None,  None, None, None],
  [None, None, None, None, None, None, None, None],
  [None,None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None,None],
  [None, None, None, None, None, None, None, None],
  [None, None, None, None,  None,  None, None, None]
       ]
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None:
                retgrid[i][j] = grid[i][j][0] + grid[i][j][1] + grid[i][j][2]
    return retgrid

def everyLegalMove(grid,black = False):
    color = 'w'
    if black:  
        color = 'b'
    moves = []
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None and grid[i][j][0] == color:
                if grid[i][j][1] == 'r':
                    if rook_move(j,i,grid,black) != None:
                        for move in rook_move(j,i,grid,black):
                            moves.append(color + 'r' + grid[i][j][2] +':' + str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'n':
                    if knight_move(j,i,grid,black) != None:
                        for move in knight_move(j,i,grid,black):
                            moves.append(color +'n' + grid[i][j][2] +':' +str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'b':
                    if bishop_move(j,i,grid,black) != None:  
                        for move in bishop_move(j,i,grid,black):
                            moves.append(color +'b' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'k':
                    if king_move(j,i,grid,black) != None:
                        for move in king_move(j,i,grid,black):
                            moves.append(color +'k' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'q':
                    if queen_move(j,i,grid,black) != None:
                        for move in queen_move(j,i,grid,black):
                            moves.append(color +'q' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'p':
                    if pawn_move(j,i,grid,black) != None:
                        for move in pawn_move(j,i,grid,black):
                            moves.append(color +'p' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
    return moves

def findPiece(piece,grid):
    for i in range(8):
        for j in range(8):
            if grid[j][i] != None and grid[j][i] == piece:
                return ([i,j])
    return None

def moveToGridHelper(move,grid,black=False):
    retg = gridCopy(grid)
    retg[int(move[-1])][int(move[-3])] = move[:3]
    retg[findPiece(move[:3],grid)[1]][findPiece(move[:3],grid)[0]] = None
    return retg
    
def everyLegalBoard(grid,black=False):
    ret = []
    for move in everyLegalMove(grid,black):
        ret.append(moveToGridHelper(move,grid))
    return ret

def visualPrint(board):
    print("      0      1      2      3      4      5      6      7")

    for row in range(8):
        print(0 + row, "|", end=" ")
        for col in range(8):
            piece = board[row][col]
            if piece is None:
                print("    ", end=" | ")
            else:
                print(f" {piece}", end=" | " if len(piece) == 3 else "  | ")
        print("\n   --------------------------------------------------------")

def everyVisualBoard(grid, black=False):
    for b in everyLegalBoard(grid,black):
        (visualPrint(b))

##########################################################


#EVALUATION_FUNCTION######################################

def evaluate(grid):
    ret = 0
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None:
                multi = 1
                if (grid[i][j][0] == 'b'):
                    multi = -1
                if (grid[i][j][1] == 'p'):
                    ret += multi
                if (grid[i][j][1] == 'n'):
                    ret += multi*3
                if (grid[i][j][1] == 'b'):
                    ret += multi*3
                if (grid[i][j][1] == 'r'):
                    ret += multi*5
                if (grid[i][j][1] == 'q'):
                    ret += multi*9
    return ret
    

  
##########################################################

#MINIMAX##################################################

def minimax(grid,depth,alpha,beta,black=False):
    retg = []
    if (depth == 0 or checkMateCheck(grid,black) != 'KeepPlaying'):
        return evaluate(grid)
    if (not black):
        maxEval = -999
        for g in everyLegalBoard(grid,False):
            evalu = minimax(g,depth-1,alpha,beta,True)
            if (evalu > maxEval):
                retg = g
            maxEval = max(evalu,maxEval)
            alpha = max(alpha,evalu)
            if (beta <= alpha):
                break
        if depth == 3:
            visualPrint(retg)
        return maxEval

    else:
        minEval = 999
        for g in everyLegalBoard(grid,True):     
            evalu = minimax(g,depth-1,alpha,beta,False)
            minEval = min(minEval,evalu)
            beta = min(beta, evalu)
            if (beta <= alpha):
                break
        return minEval

##########################################################

#TESTING#################################################




  
##########################################################