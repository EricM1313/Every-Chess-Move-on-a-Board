class Piece:

  def __init__(self, color, type, x, y):
    self.type = type
    self.color = color
    self.x = x
    self.y = y

  def move(self):
    for i in range(9):
      if self.type == "p" + str(i):
        return pawn_move(self.x, self.y)
        break

    if type == "r1" or self.type == "r2":
      return rook_move(self.x, self.y)
    if self.type == "n1" or self.type == "n2":
      return knight_move(self.x, self.y)
    if self.type == "b1" or self.type == "b2":
      return bishop_move(self.x, self.y)
    if self.type == "q":
      return queen_move(self.x, self.y)
    if self.type == "k":
      return king_move(self.x, self.y)

  def myfunc(self):
    print("Hello my name is " + self.name)
    
'''
Classification:

1,1111,111,111
1,2333,444,555

1:
W = 1
B= 0
2:
Pawn = 0
Big Piece = 1
3:
num 0-7, indicating position left to right
4:
x-position 0-7, left to right
4:
y-position 0-7, left to right

'''
  
wp1 = Piece('W','p1',1,2)
wp2 = Piece('W','p2',2,2)
wp3 = Piece('W','p3',3,2)
wp4 = Piece('W','p4',4,2)
wp5 = Piece('W','p5',4,3)
wp6 = Piece('W','p6',6,2)
wp7 = Piece('W','p7',7,2)
wp8 = Piece('W','p8',8,2)
wr1 = Piece('W','r1',1,1)
wr2 = Piece('W','r2',8,1)
wb1 = Piece('W','b1',3,1)
wb2 = Piece('W','b2',6,1)
wn1 = Piece('W','n1',5,4)
wn2 = Piece('W','n2',7,1)
wk = Piece('W','k',5,1)
wq = Piece('W','q',4,1)

bp1 = Piece('B','p1',1,7)
bp2 = Piece('B','p2',2,7)
bp3 = Piece('B','p3',3,7)
bp4 = Piece('B','p4',4,7)
bp5 = Piece('B','p5',5,7)
bp6 = Piece('B','p6',6,7)
bp7 = Piece('B','p7',7,7)
bp8 = Piece('B','p8',8,7)
br1 = Piece('B','r1',1,8)
br2 = Piece('B','r2',8,8)
bb1 = Piece('B','b1',3,8)
bb2 = Piece('B','b2',6,8)
bn1 = Piece('B','n1',2,8)
bn2 = Piece('B','n2',7,8)
bk = Piece('B','k',5,8)
bq = Piece('B','q',5,6)



grid = [ 
  [wr1, None, wb1, wq,  wk,  wb2, wn2, wr2],
  [wp1, wp2, wp3, wp4, None, wp6, wp7, wp8],
  [None,None,None,wp5,None,None,None,None],
  [None,None,None,None,wn1,None,None,None],
  [None,None,None,None,None,None,None,None],
  [None,None,None,None,bq,None,None,None],
  [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
  [br1, bn1, bb1, None,  bk,  bb2, bn2, br2]
       ]







def rook_move(x,y):
    
    moves = []
    for i in range(1,9):
        if (x+i > 0 and x+i <9):
            if grid[y-1][x+i-1] ==None:
                moves.append([x+i,y])
            elif grid[y-1][x+i-1].color != grid[y-1][x-1].color:
                moves.append([x+i,y])
                break
            else:
                break
    for i in range(1,9):
        if (x-i > 0 and x-i <9):
             if grid[y-1][x-i-1] ==None:
                 moves.append([x-i,y])
             elif grid[y-1][x-i-1].color != grid[y-1][x-1].color:
                 moves.append([x-i,y])
                 break
             else:
                 break
    for j in range(1,9):
        if (y+j > 0 and y+j <9):
            
             if grid[y+j-1][x-1] == None:
                 moves.append([x,y+j])
             
             elif grid[y+j-1][x-1].color != grid[y-1][x-1].color:
                 moves.append([x,y+j])
                 break
             else:
                 break
    for j in range(1,9):
        if (y-j > 0 and y-j <9):
            if grid[y-j-1][x-1] ==None:
                  moves.append([x,y-j])
            elif grid[y-j-1][x-1].color != grid[y-1][x-1].color:
                  moves.append([x,y-j])
                  break
            else:
                 break 
    if moves == []:
        return None 
    remove_moves = []
    if grid[y-1][x-1].color == 'W':

        for move in moves:
            grid[move[1]-1][move[0]-1] = grid[y-1][x-1]
            grid[y-1][x-1] = None
            if king_in_check(grid):
                remove_moves.append(move)
            grid[y-1][x-1] = grid[move[1]-1][move[0]-1]
            grid[move[1]-1][move[0]-1] = None
        moves = [i for i in moves if i not in remove_moves]
    

    

    if moves == []:
        return None

    return(moves)



def bishop_move(x,y):
    moves = []
    for i in range(1,9):
        if (x+i > 0 and y+i <9) and (x+i<9 and y+i>0):
            if grid[y+i-1][x+i-1] ==None:
                moves.append([x+i,y+i])    
            elif grid[y+i-1][x+i-1].color != grid[y-1][x-1].color:
                moves.append([x+i,y+i])
                break
            else:
                break
    for i in range(1,9):
        if (x+i > 0 and y-i <9) and (x+i<9 and y-i>0):
             if grid[y-i-1][x+i-1] ==None:
                 moves.append([x+i,y-i])
             elif grid[y-i-1][x+i-1].color != grid[y-1][x-1].color:
                 moves.append([x+i,y-i])
                 break
             else:
                 break
    for j in range(1,9):
        if (x-j > 0 and y+j <9) and (x-j<9 and y+j>0):
             if grid[y+j-1][x-j-1] ==None:
                 moves.append([x-j,y+j])
             elif grid[y+j-1][x-j-1].color != grid[y-1][x-1].color:
                 moves.append([x-j,y+j])
                 break
             else:
                 break
    for j in range(1,9):
        if (x-j > 0 and y-j <9) and (x-j<9 and y-j>0):
            if grid[y-j-1][x-j-1] ==None:
                moves.append([x-j,y-j])
            elif grid[y-j-1][x-j-1].color != grid[y-1][x-1].color:
                moves.append([x-j,y-j])
                break
            else:
                  break
    if moves == []:
        return None
    remove_moves = []
    if grid[y-1][x-1].color == 'W':

        for move in moves:
            grid[move[1]-1][move[0]-1] = grid[y-1][x-1]
            grid[y-1][x-1] = None
            if king_in_check(grid):
                remove_moves.append(move)
            grid[y-1][x-1] = grid[move[1]-1][move[0]-1]
            grid[move[1]-1][move[0]-1] = None
        moves = [i for i in moves if i not in remove_moves]
    if moves == []:
        return None
    return(moves)

def queen_move(x,y):
    moves = []
    for i in range(1,9):
        if (x+i > 0 and y+i <9) and (x+i<9 and y+i>0):
            if grid[y+i-1][x+i-1] ==None:
                moves.append([x+i,y+i])
            elif grid[y+i-1][x+i-1].color != grid[y-1][x-1].color:
                moves.append([x+i,y+i])
                break
            else:
                break
    for i in range(1,9):
        if (x+i > 0 and y-i <9) and (x+i<9 and y-i>0):
             if grid[y-i-1][x+i-1] ==None:
                 moves.append([x+i,y-i])
             elif grid[y-i-1][x+i-1].color != grid[y-1][x-1].color:
                 moves.append([x+i,y-i])
                 break
             else:
                 break
    for j in range(1,9):
        if (x-j > 0 and y+j <9) and (x-j<9 and y+j>0):
             if grid[y+j-1][x-j-1] ==None:
                 moves.append([x-j,y+j])
             elif grid[y+j-1][x-j-1].color != grid[y-1][x-1].color:
                 moves.append([x-j,y+j])
                 break
             else:
                 break
    for j in range(1,9):
        if (x-j > 0 and y-j <9) and (x-j<9 and y-j>0):
            if grid[y-j-1][x-j-1] ==None:
                moves.append([x-j,y-j])
            elif grid[y-j-1][x-j-1].color != grid[y-1][x-1].color:
                moves.append([x-j,y-j])
                break
            else:
                  break
    for i in range(1,9):
        if (x+i > 0 and x+i <9):
            if grid[y-1][x+i-1] ==None:
                moves.append([x+i,y])
            elif grid[y-1][x+i-1].color != grid[y-1][x-1].color:
                moves.append([x+i,y])
                break
            else:
                break
    for i in range(1,9):
        if (x-i > 0 and x-i <9):
             if grid[y-1][x-i-1] ==None:
                 moves.append([x-i,y])
             elif grid[y-1][x-i-1].color != grid[y-1][x-1].color:
                 moves.append([x-i,y])
                 break
             else:
                 break
    for j in range(1,9):
        if (y+j > 0 and y+j <9):
             if grid[y+j-1][x-1] ==None:
                 moves.append([x,y+j])
             elif grid[y+j-1][x-1].color != grid[y-1][x-1].color:
                 moves.append([x,y+j])
                 break
             else:
                 break
    for j in range(1,9):
        if (y-j > 0 and y-j <9):
            if grid[y-j-1][x-1] ==None:
                  moves.append([x,y-j])
            elif grid[y-j-1][x-1].color != grid[y-1][x-1].color:
                  moves.append([x,y-j])
                  break
            else:
                  break
    if moves == []:
        return None 
    remove_moves = []
    if grid[y-1][x-1].color == 'W':
        for move in moves:
            grid[move[1]-1][move[0]-1] = grid[y-1][x-1]
            grid[y-1][x-1] = None
            if king_in_check(grid):
                remove_moves.append(move)
            grid[y-1][x-1] = grid[move[1]-1][move[0]-1]
            grid[move[1]-1][move[0]-1] = None
        moves = [i for i in moves if i not in remove_moves]
    if moves == []:
        return None
    return(moves)

def king_move(x,y):
    moves = []
    for i in range(-1,2):
        for j in range(-1,2):
            if (x+i >0) and (x+i<9) and (y+j >0) and (y+j < 9):
                if grid[y+j-1][x+i-1] == None:
                    moves.append([x+i,y+j])
                elif grid[y+j-1][x+i-1].color != grid[y-1][x-1].color:
                    moves.append([x+i,y+j])
    if moves == []:
        return None 
    remove_moves = []
    if grid[y-1][x-1].color == 'W':
        for move in moves:
            grid[move[1]-1][move[0]-1] = grid[y-1][x-1]
            grid[y-1][x-1] = None
            if king_in_check(grid):
                remove_moves.append(move)
            grid[y-1][x-1] = grid[move[1]-1][move[0]-1]
            grid[move[1]-1][move[0]-1] = None
        moves = [i for i in moves if i not in remove_moves]
    if moves == []:
        return None
    return(moves)

def knight_move(x,y):
    x = x - 1
    y = y - 1
    possible_moves = [[1, 2], [-1, 2], [2, 1], [2, -1], [1, -2], [-1, -2],
                    [-2, 1], [-2, -1]]
    moves = []
    for move in possible_moves:
        newGridPos_X = move[0] + x
        newGridPos_Y = move[1] + y
        if newGridPos_X < 0 or newGridPos_X > 7 or newGridPos_Y < 0 or newGridPos_Y > 7:
            continue
        if grid[newGridPos_Y][newGridPos_X] == None or grid[newGridPos_Y][
                newGridPos_X].color != grid[y][x].color:
                moves.append([newGridPos_X + 1, newGridPos_Y + 1])
    if moves == []:
        return None 
    remove_moves = []
    if grid[y-1][x-1].color == 'W':

        for move in moves:
            grid[move[1]-1][move[0]-1] = grid[y-1][x-1]
            grid[y-1][x-1] = None
            if king_in_check(grid):
                remove_moves.append(move)
            grid[y-1][x-1] = grid[move[1]-1][move[0]-1]
            grid[move[1]-1][move[0]-1] = None
        moves = [i for i in moves if i not in remove_moves]
    

    

    if moves == []:
        return None
    return(moves)

def pawn_move(x,y):
    x = x - 1
    y = y - 1  
    capture_moves = [[1, 1], [-1, 1]]
    return_moves = []
    if(y == 1):
      newGridPos_Y = 2 + y
      if grid[newGridPos_Y][x] == None:
        return_moves.append([x+1,newGridPos_Y+1])
  #for pawn moving forward 2
  
  #for pawn moving forward 1
    newGridPos_Y = 1 + y
    if newGridPos_Y >=0 and newGridPos_Y <= 7:
      if grid[newGridPos_Y][x] == None:
          return_moves.append([x+1,newGridPos_Y+1 ])
  #for pawn capturing diagonal
    for move in capture_moves:
      newGridPos_X = move[0] + x
      newGridPos_Y = move[1] + y

      if newGridPos_X < 0 or newGridPos_X > 7 or newGridPos_Y < 0 or newGridPos_Y > 7:
        continue

      if grid[newGridPos_Y][newGridPos_X]!= None and grid[newGridPos_Y][newGridPos_X].color == 'B':
        return_moves.append([newGridPos_X+1, newGridPos_Y+1])
    if return_moves == []:
        return None 
    remove_moves = []
    if grid[y-1][x-1]!= None and grid[y-1][x-1].color == 'W':

        for move in return_moves:
            grid[move[1]-1][move[0]-1] = grid[y-1][x-1]
            grid[y-1][x-1] = None
            if king_in_check(grid):
                remove_moves.append(move)
            grid[y-1][x-1] = grid[move[1]-1][move[0]-1]
            grid[move[1]-1][move[0]-1] = None
        reutrn_moves = [i for i in return_moves if i not in remove_moves]
    

    

    if return_moves == []:
        return None
    return(return_moves)


def king_in_check(grid):
    possible_moves = []
    for i in range(8):
        for j in range(8):
            if grid[i][j] != None and grid[i][j].color == 'B':
                if grid[i][j].move() != None:
                    possible_moves.append(grid[i][j].move())
    for move_list in possible_moves:
        if move_list != None:
            if [wk.x, wk.y] in move_list:
                return True
    return False





def find_white_pieces_sorted(grid):
    pawns = []
    rooks = []
    bishops = []
    knights = []
    king = []
    queen = []
    for i in grid:
        for s in i:
            if s != None:
                if s.color == 'W':
                    if s.type[0] =='p':
                        pawns.append([s.type,s.x,s.y])
                    elif s.type[0]=='r':
                        rooks.append([s.type,s.x,s.y])
                    elif s.type[0]=='b':
                        bishops.append([s.type,s.x,s.y])
                    elif s.type[0]=='n':
                        knights.append([s.type,s.x,s.y])
                    elif s.type[0]=='k':
                        king.append([s.type,s.x,s.y])
                    elif s.type[0]=='q':
                        queen.append([s.type,s.x,s.y])
                    
    return [pawns,rooks,bishops,knights,king,queen]
#print(find_white_pieces_sorted(grid))

def everyMovePossible(grid):
    ret = []
    for piece in find_white_pieces_sorted(grid)[0]:
        ret.append([piece[0],pawn_move(piece[1],piece[2])])
    for piece in find_white_pieces_sorted(grid)[1]:
        ret.append([piece[0],rook_move(piece[1],piece[2])])
    for piece in find_white_pieces_sorted(grid)[2]:
        ret.append([piece[0],bishop_move(piece[1],piece[2])])
    #for piece in find_white_pieces_sorted(grid)[3]:
        #ret.append([piece[0],knight_move(piece[1],piece[2])])
    for piece in find_white_pieces_sorted(grid)[4]:
        ret.append([piece[0],king_move(piece[1],piece[2])])
    for piece in find_white_pieces_sorted(grid)[5]:
        ret.append([piece[0],queen_move(piece[1],piece[2])])
    
    return ret

print(everyMovePossible(grid))
            
  



               





 




    