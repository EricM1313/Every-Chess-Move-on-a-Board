
board = [ 
  ['wr1','wn1','br1','wq_','wk_','wb2',None ,'wr2'],
  ['wp1','wp2','wp3',None ,'wp5','wp6','wp7','wp8'],
  [None ,None ,None ,None ,'wb1','wn2',None ,None ],  
  [None ,'bq_',None ,'wp4',None ,None ,None ,None ],
  ['bp1',None ,None ,'bp4',None ,None ,None ,'bp8'],
  [None ,None ,'bn1',None ,None ,'bn2',None ,None ],
  [None ,'bp2','bp3',None ,'bp5','bp6','bp7',None ],
  [None ,None ,'bb1',None ,'bk_','bb2',None ,'br2']
       ]

def rook_move(x,y,grid, black = False):
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
    if black == False:  
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = 'wrx'
            if checkCheck(possibleGrid):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def bishop_move(x,y,grid,black = False):
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
    if black == False:  
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = 'wbx'
            if checkCheck(possibleGrid):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)
    
def queen_move(x,y,grid, black = False):
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
    if black == False:  
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = 'wq_'
            if checkCheck(possibleGrid):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def king_move(x,y,grid, black = False):
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
    if black == False:  
        illegal_moves = []
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = 'wk_'
            if checkCheck(possibleGrid):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def knight_move(x,y,grid,black = False):
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
    if black == False:  
        illegal_moves = []
        for move in moves:
            possibleGrid = gridCopy(grid)
            possibleGrid[y][x] = None
            possibleGrid[move[1]][move[0]] = 'wnx'
            if checkCheck(possibleGrid):
                illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def pawn_move(x,y,grid,black = False):
    if grid[y][x] == None or grid[y][x][1] != 'p':
        return 'error wrong piece'
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

        for move in moves:
            newGridPos_X = move[0] + x
            newGridPos_Y = move[1] + y

            if newGridPos_X < 0 or newGridPos_X > 7 or newGridPos_Y < 0 or newGridPos_Y > 7:
                continue

            if grid[newGridPos_Y][newGridPos_X]!= None and grid[newGridPos_Y][newGridPos_X][0] == 'w':
                moves.append([newGridPos_X, newGridPos_Y])
        if moves == []:
            return None 
        return moves
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
    if black == False:  
          for move in moves:
              possibleGrid = gridCopy(grid)
              possibleGrid[y][x] = None
              possibleGrid[move[1]][move[0]] = 'wrx'
              if checkCheck(possibleGrid):
                  illegal_moves.append(move)
    moves = [i for i in moves if i not in illegal_moves]
    if moves == []:
        return None
    return(moves)

def checkCheck(grid):
    wkx = -1
    wky = -1
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None:
                if grid[i][j][0] == 'w' and grid[i][j][1] == 'k':
                    wkx, wky = j, i  

    possible_moves = []
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None and grid[i][j][0] == 'b':
                    if grid[i][j][1] == 'r':
                        if rook_move(j,i,grid,True) != None:
                            possible_moves.append(rook_move(j,i,grid,True))
                    if grid[i][j][1] == 'n':
                        if knight_move(j,i,grid,True) != None:
                            possible_moves.append(knight_move(j,i,grid,True))
                    if grid[i][j][1] == 'b':
                        if bishop_move(j,i,grid,True) != None:
                            possible_moves.append(bishop_move(j,i,grid,True))
                    if grid[i][j][1] == 'k':
                        if king_move(j,i,grid,True) != None:
                            possible_moves.append(king_move(j,i,grid,True))
                    if grid[i][j][1] == 'q':
                        if queen_move(j,i,grid,True) != None:
                            possible_moves.append(queen_move(j,i,grid,True))
                    if grid[i][j][1] == 'p':
                        if pawn_move(j,i,grid,True) != None:
                            possible_moves.append(pawn_move(j,i,grid,True))
    for move_list in possible_moves:
        if move_list != None:
            if [wkx, wky] in move_list:
                return True

    return False

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

def everyLegalMove(grid):
    moves = []
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None and grid[i][j][0] == 'w':
                if grid[i][j][1] == 'r':
                    if rook_move(j,i,grid) != None:
                        for move in rook_move(j,i,grid):
                            moves.append('r' + grid[i][j][2] +':' + str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'n':
                    if knight_move(j,i,grid) != None:
                        for move in knight_move(j,i,grid):
                            moves.append('n' + grid[i][j][2] +':' +str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'b':
                    if bishop_move(j,i,grid) != None:  
                        for move in bishop_move(j,i,grid):
                            moves.append('b' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'k':
                    if king_move(j,i,grid) != None:
                        for move in king_move(j,i,grid):
                            moves.append('k' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'q':
                    if queen_move(j,i,grid) != None:
                        for move in queen_move(j,i,grid):
                            moves.append('q' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
                if grid[i][j][1] == 'p':
                    if pawn_move(j,i,grid) != None:
                        for move in pawn_move(j,i,grid):
                            moves.append('p' + grid[i][j][2] +':'+ str(move[0])+','+str(move[1]))
    return moves

def findPiece(piece,grid):
    for i in range(8):
        for j in range(8):
            if grid[j][i] != None and grid[j][i][1:] == piece:
                return ([i,j])
    return None

def moveToGridHelper(move,grid):
    retg = gridCopy(grid)
    retg[move[-1]][move[-3]] = move[:2]
    retg[findPiece(move[:2])[1]][findPiece(move[:2])[0]] = None
    return retg
    
def everyLegalBoard(grid):
    ret = []
    for move in everyLegalMove(grid):
        ret.append(moveToGridHelper(move,grid))
    return ret


print(everyLegalBoard(board))
