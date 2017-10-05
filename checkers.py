
#dict of starting board, with number and wether or not there is a piece
board = {57:' ',58:'o',59:' ',60:'o',61:' ',62:'o',63:' ',64:'o',
         49:'o',50:' ',51:'o',52:' ',53:'o',54:' ',55:'o',56:' ',
         41:' ',42:'o',43:' ',44:'o',45:' ',46:'o',47:' ',48:'o',
         33:' ',34:' ',35:' ',36:' ',37:' ',38:' ',39:' ',40:' ',
         25:' ',26:' ',27:' ',28:' ',29:' ',30:' ',31:' ',32:' ',
         17:'x',18:' ',19:'x',20:' ',21:'x',22:' ',23:'x',24:' ',
         9:' ',10:'x',11:' ',12:'x',13:' ',14:'x',15:' ',16:'x',
         1:'x',2:' ',3:'x',4:' ',5:'x',6:' ',7:'x',8:' '}

convert ={'a1':57,'a2':58,'a3':59,'a4':60,'a5':61,'a6':62,'a7':63,'a8':64,
          'b1':49,'b2':50,'b3':51,'b4':52,'b5':53,'b6':54,'b7':55,'b8':58,
          'c1':41,'c2':42,'c3':43,'c4':44,'c5':45,'c6':46,'c7':47,'c8':48,
          }
#printing the current board
def show():
    print'---------------------------------'
    print '|',board[57],'|',board[58],'|',board[59],'|',board[60],'|',board[61],'|',board[62],'|',board[63],'|',board[64],'|'
    print'---------------------------------'
    print '|',board[49],'|',board[50],'|',board[51],'|',board[52],'|',board[53],'|',board[54],'|',board[55],'|',board[56],'|'
    print'---------------------------------'
    print '|',board[41],'|',board[42],'|',board[43],'|',board[44],'|',board[45],'|',board[46],'|',board[47],'|',board[48],'|'
    print'---------------------------------'
    print '|',board[33],'|',board[34],'|',board[35],'|',board[36],'|',board[37],'|',board[38],'|',board[39],'|',board[40],'|'
    print'---------------------------------'
    print '|',board[25],'|',board[26],'|',board[27],'|',board[28],'|',board[29],'|',board[30],'|',board[31],'|',board[32],'|'
    print'---------------------------------'
    print '|',board[17],'|',board[18],'|',board[19],'|',board[20],'|',board[21],'|',board[22],'|',board[23],'|',board[24],'|'
    print'---------------------------------'
    print '|',board[9],'|',board[10],'|',board[11],'|',board[12],'|',board[13],'|',board[14],'|',board[15],'|',board[16],'|'
    print'---------------------------------'
    print '|',board[1],'|',board[2],'|',board[3],'|',board[4],'|',board[5],'|',board[6],'|',board[7],'|',board[8],'|'
    print'---------------------------------'

show()

def p1turn():
    input = raw_input("Enter Move: ")
    start,end = input.split()
    start = int(start)
    end = int(end)
    if board[start] == "x" and board[end] == " ":
        if end - start == 7 or end - start == 9:
          board[start] = " "
          board[end] = "x"
          show()
        else:
          print "invalid move"
    else:
        print "invalid move"
    
    
p1turn()
