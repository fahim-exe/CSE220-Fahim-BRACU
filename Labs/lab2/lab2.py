def Billboard(str1, str2):
  
  
  up_index = 0
  down_index = 0
  up_board = [""]*10
  down_board = [""]*10
  whole_board = [up_board, down_board]

  for i in range(len(str1)):
    up_board[i]=str1[i]
    if ord(str1[i])>=65 and ord(str1[i])<=90:
      up_index = i
  
  for i in range(len(str2)):
    down_board[i] = str2[i]
    if ord(str2[i])>=65 and ord(str2[i])<=90:
      down_index = i

  out[0]=str1[up_index]
  out[1]=up_index
  out[2]=down_board[down_index]
  out[3]=down_index
  last1 = (up_index+len(str1)-1)%len(up_board)
  last2 = (down_index+len(str1)-1)%len(down_board)
  print(up_board)
  print(down_board)
  print(out)
  print(last1)
  print(last2)



def output(str1, str2):
  p_c =0
  if len(str1)>10 or len(str2)>10:
    return f"Invalid Input Size"

  print("Your Input is Valid. Press any key and the then enter to continue!!!")
  while True:
    
    user_input = input()
    if user_input=="q" or user_input=="Q":
      break
    Billboard(str1, str2)
    
    if p_c==0:
      print("Top Board Start Character:", out[0])    
      print("Top Board Start Index:", out[1])
      print("Bottom Board Start:", out[2])
      print("Bottom Board Start Index:", out[3])
      p_c+=1

      '''   for i in range( len(whole_board[0])):
      if whole_board[0][i] is not None:
        str1 +=str(whole_board[0][i])
    for i in range(len(whole_board[1])):
      if whole_board[1][i] is not None:
        str2 +=str(whole_board)

    print(str1, str2)
    '''


    p =out[1]
    for i in range(len(whole_board[0])):
      
      print(whole_board[0][out[1]])
      #whole_board[0][i-1] = whole_board[0][i]
      p = (p-1)%len(whole_board[0])
    q = output
    for i in range(out[3], len(whole_board[1])):
      temp = whole_board[1][out[3]]
      print(whole_board[1][i])
      i = (i+1)%len(whole_board[1])

      
    print("Press any key and the press enter to continue!!!")
    

up_index = 0
down_index = 0
up_board = [None]*10
down_board = [None]*10
whole_board = [up_board, down_board]
out = [None]*4
str1 = ""
str2 = ""
last1 = None
last2 = None



user_in1 = input()
user_in2 = input()

#output(user_in1, user_in2)

Billboard(user_in1, user_in2)