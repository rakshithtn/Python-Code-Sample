#!/usr/bin/python

##################################################
#Rakshith Tumkur Nagabhushana
#N17419862
#rtn221
#Camelot.py
##################################################


import subprocess as sp
import math

####################################################################
#Class Model has two lists and a matrix for UI


class Model(object):
 def __init__(self):
  self.board = [[0 for i in range(10)]for j in range(14)]
  for i in range(14):
	for j in range(9):
		self.board[i][j]="-"

  self.humancount = 0
  self.computercount = 0 

  self.level = 0
  self.pinf = 10000
  self.ninf = -10000
  self.win = 0


  self.human = [
		[9,4],[9,5],[8,3],[8,4],[8,5],[8,6]
		]
  self.computer = [
		 [5,4],[5,5],[4,3],[4,4],[4,5],[4,6]
		 ]



  self.board[0][9] = ' '
  self.board[1][9] = ' '
  self.board[2][9] = ' '
  self.board[3][9] = ' '
  self.board[4][9] = ' '
  self.board[5][9] = ' '
  self.board[6][9] = ' '
  self.board[7][9] = ' '
  self.board[8][9] = ' '
  self.board[9][9] = ' '
  self.board[10][9] = ' '
  self.board[11][9] = ' '
  self.board[12][9] = ' '
  self.board[13][9] = ' '


  self.board[13][0] = ' '
  self.board[13][2] = ' '
  self.board[13][3] = ' '
  self.board[13][6] = ' '
  self.board[13][7] = ' '
  self.board[13][8] = ' '
  self.board[13][1] = ' '

  self.board[12][0] = ' '
  self.board[12][1] = ' '
  self.board[12][2] = ' '
  self.board[12][7] = ' '
  self.board[12][8] = ' '

  self.board[11][0] = ' '
  self.board[11][1] = ' '
  self.board[11][8] = ' '

  self.board[10][0] = ' '
  self.board[9][0] = ' '
  self.board[8][0] = ' '
  self.board[7][0] = ' '
  self.board[6][0] = ' '
  self.board[5][0] = ' '
  self.board[4][0] = ' '
  self.board[3][0] = ' '

  self.board[2][0] = ' '
  self.board[2][1] = ' '
  self.board[2][8] = ' '

  self.board[1][0] = ' '
  self.board[1][1] = ' '
  self.board[1][2] = ' '
  self.board[1][7] = ' '
  self.board[1][8] = ' '

  self.board[0][0] = ' '
  self.board[0][2] = ' '
  self.board[0][3] = ' '
  self.board[0][6] = ' '
  self.board[0][7] = ' '
  self.board[0][8] = ' '
  self.board[0][1] = ' '

  self.board[0][4] = 'X'
  self.board[0][5] = 'X'
  self.board[13][4] = 'Y'
  self.board[13][5] = 'Y'

  self.board[4][6] = '0'
  self.board[4][3] = '0'
  self.board[4][4] = '0'
  self.board[4][5] = '0'
  self.board[5][4] = '0'
  self.board[5][5] = '0'

  self.board[8][6] = '1'
  self.board[8][3] = '1'
  self.board[8][4] = '1'
  self.board[8][5] = '1'
  self.board[9][4] = '1'
  self.board[9][5] = '1'

##################################################################
#Class View is used to display the matrix of Class Model for UI


class View(object):
	tmp = sp.call('cls',shell=True)
	def __init__(self):
		pass
	def display(self, board):
	 print
	 print
	 print
	 print
	 print ' ',
	 for i in range(len(board[1])):
		 print i,
	 print
	 for i,element in enumerate(board):
	     print "\t"
	     print i,' '.join(element)
	 print
	 print '  ',
	 for i in range(len(board[1])):
		 print i,
	 print
	 print
	 print
	 print
	 print

##############################################################################
#This function allows human to play


def call_human(v,m):
	print "\nYour pieces are marked as 1, Computer pieces are marked as 0 \n\n"
	rin = input("Enter the row number of the initial position of the piece you want to move \n\n")
	cin = input("Enter the column number of the initial position of the piece you want to move \n\n")
	rout = input("Enter the row number of the destination position of the piece \n\n")
	cout = input("Enter the column number of the destination position of the piece \n\n")

	
	x = input("\nPress `7 if your move is plain move, 8 if it is a capturing move 9 if it is a cantering move \n\n")
	if x==8:
		rcap = input("\nEnter the row number of the opponent which you are capturing \n")
		ccap = input("\nEnter the column number of the opponent which you are capturing \n")
		for i in range(6): 
				if (m.computer[i][0] == rcap and m.computer[i][1] == ccap):#setting the captured position to 100
					m.computer[i][0] = 100
					m.computer[i][1] = 100

		for i in range(6): 
				if (m.human[i][0] == rin and m.human[i][1] == cin):
					m.human[i][0] = rout
					m.human[i][1] = cout
		
		m.board[rcap][ccap]='-'
		m.board[rout][cout]='1'
		m.board[rin][cin]='-'
		m.computercount=m.computercount+1
		check_if_human_won(v,m,rout,cout)
		v.display(m.board)

		#to allow another capture

		another_capture = input("\n\nPress 1 if you want to make another capturing move. Else press 2\n\n")

		while(another_capture == 1):

			v, m = call_human_another_capture(v,m)
			v.display(m.board)
			check_if_human_won(v,m,rout,cout)
			another_capture = input("\n\nPress 1 if you want to make another capturing move. Else press 2\n\n")


	elif x==7 or x==9:
		
		for i in range(6): 
				if (m.human[i][0] == rin and m.human[i][1] == cin):
					m.human[i][0] = rout
					m.human[i][1] = cout

		m.board[rin][cin]='-'
		m.board[rout][cout]='1'
		check_if_human_won(v,m,rout,cout)

	v.display(m.board)
	call_computer(v,m)



################################################################################

#it checks if human won after every move by human

def check_if_human_won(v,m,rout,cout):
	if m.computercount==6:
	     v.display(m.board)
	     print
	     print
	     print ("****************YOU WON!! You Captured all Opponents!!*************")
	     exit()
	
	if ((cout == 4 or cout == 5) and rout == 0):
	     v.display(m.board)
	     print
	     print
	     print ("****************YOU WON!! You Reached Opponent Castle!!*************")
	     exit()



#######################################################################################
#Another call_human which eleminates unwanted steps from the previous human call function

def call_human_another_capture(v,m):


	rin = input("\n\nEnter the row number of the initial position of the piece you want to move \n\n")
	cin = input("Enter the column number of the initial position of the piece you want to move \n\n")
	rout = input("Enter the row number of the destination position of the piece \n\n")
	cout = input("Enter the column number of the destination position of the piece \n\n")
	x=8

	
	if x==8:
		rcap = input("\nEnter the row number of the opponent which you are capturing \n")
		ccap = input("\nEnter the column number of the opponent which you are capturing \n")
		for i in range(6): 
				if (m.computer[i][0] == rcap and m.computer[i][1] == ccap):
					m.computer[i][0] = 100
					m.computer[i][1] = 100

		for i in range(6): 
				if (m.human[i][0] == rin and m.human[i][1] == cin):
					m.human[i][0] = rout
					m.human[i][1] = cout
		
		m.board[rcap][ccap]='-'
		m.board[rout][cout]='1'
		m.board[rin][cin]='-'
		m.computercount=m.computercount+1
		check_if_human_won(v,m,rout,cout)
		return v,m

########################################################################
#This function calls the computer to play

def call_computer(v,m):
	print "Computer will play"



	v, m, valcapture = call_capturing(v,m)
	v.display(m.board)

	if m.humancount == 6:
		v.display(m.board)
		print "Computer Won"
		exit()

	if(valcapture == 1):	

	 call_another_capture_comp = input("\n\nPress 1 if you want the computer to play another capturing move. Else press 2\n\n")

	 while(call_another_capture_comp == 1):
	     call_another_capture_comp = 0
	     v,m,valcaptureinc = call_capturing(v,m)
	     v.display(m.board)
	     if valcaptureinc == 1:
		if m.humancount == 6:
		 v.display(m.board)
		 print "Computer Won"
		 exit()
	        call_another_capture_comp = input("\n\nPress 1 if you want the computer to play another capturing move. Else press 2\n\n")




	if m.humancount == 6:
		v.display(m.board)
		print "Computer Won"
		exit()


	if(valcapture == 0):

	    if(m.level == 2):

		v, m, valcheck = call_plain_check(v,m)
		v.display(m.board)

		if(valcheck == 0):
		  v, m, valplain = call_plain(v,m)
		  v.display(m.board)

		  if(valplain == 0):
			  v, m, valplainsamerowcheck = call_plain_samerow_check(v,m)
			  v.display(m.board)

			  if valplainsamerowcheck == 0:
				v,m,valplainsamerow = call_plain_samerow(v,m)
				v.display(m.board)

				if valplainsamerow == 0:
				   v,m,valplainbackcheck = call_plain_back_check(v,m)
				   v.display(m.board)

				   if valplainbackcheck == 0:
					 v,m,valplainback = call_plain_back(v,m)
					 v.display(m.board)

					 if valplainback == 0:
						v.display(m.board)
				 		print ("No move possible")


	    else:

		  v, m, valplain = call_plain(v,m)
		  v.display(m.board)

		  if(valplain == 0):
			  v, m, valplainsamerow = call_plain_samerow(v,m)
			  v.display(m.board)

			  if valplainsamerow == 0:
				v,m,valplainback = call_plain_back(v,m)
				v.display(m.board)

				if valplainbak == 0:
				   v.display(m.board)
				   print ("No move possible")
	
	v.display(m.board)
	call_human(v,m)


#########################################################
#This function gives all the 8 possible capturs if any

def call_capturing(v,m):
	
	for i in range(6):
		a=m.computer[i][0]
		b=m.computer[i][1] 
		if(a != 100 and b != 100):
		  if (m.board[a+1][b-1] == '1' and (m.board[a+2][b-2] == '-' or m.board[a+2][b-2] == 'Y')):
			if m.board[a+2][b-2] == '-':
				v, m = set_human_vec(a+1,b-1,v,m)
				v, m = set_comp_vec(a,b,a+2,b-2,v,m)
				m.board[a+1][b-1] = '-'
				m.board[a+2][b-2] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v, m, 1

			elif m.board[a+2][b-2] == 'Y':
				m.board[a+1][b-1] = '-'
				m.board[a+2][b-2] = '0'
				m.board[a][b]='-'
				v.display(m.board)
				print "Computer Won"
				exit()


		  elif (m.board[a+1][b+1] == '1' and (m.board[a+2][b+2] == '-' or m.board[a+2][b+2] == 'Y')):
			if m.board[a+2][b+2] == '-':
				v, m = set_human_vec(a+1,b+1,v,m)
				v, m = set_comp_vec(a,b,a+2,b+2,v,m)
				m.board[a+1][b+1] = '-'
				m.board[a+2][b+2] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v,m,1
			elif m.board[a+2][b+2] == 'Y':
				m.board[a+1][b+1] = '-'
				m.board[a+2][b+2] = '0'
				m.board[a][b]='-'
				v.display(m.board)
				print "Computer Won"
				exit()


		  elif (m.board[a-1][b-1] == '1' and (m.board[a-2][b-2] == '-' or m.board[a-2][b-2] == 'Y')):
			  if m.board[a-2][b-2] == '-':
				v, m = set_human_vec(a-1,b-1,v,m)
				v, m = set_comp_vec(a,b,a-2,b-2,v,m)
				m.board[a-1][b-1] = '-'
				m.board[a-2][b-2] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v, m, 1
			  elif m.board[a-2][b-2] == 'Y':
				m.board[a-1][b-1] = '-'
				m.board[a-2][b-2] = '0'
				m.board[a][b]='-'
				v.display(m.board)
				print "Computer Won"
				exit()

		  elif (m.board[a-1][b+1] == '1'and (m.board[a-2][b+2] == '-' or m.board[a-2][b+2] == 'Y')):
			  if m.board[a-2][b+2] == '-':
				v, m = set_human_vec(a-1,b+1,v,m)
				v, m = set_comp_vec(a,b,a-2,b+2,v,m)
				m.board[a-1][b+1] = '-'
				m.board[a-2][b+2] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v, m, 1
			  elif m.board[a-2][b+2] == 'Y':
				m.board[a-1][b+1] = '-'
				m.board[a-2][b+2] = '0'
				m.board[a][b]='-'
				v.display(m.board)
				print "Computer Won"
				exit()


		  elif (m.board[a-1][b] == '1' and (m.board[a-2][b] == '-' or m.board[a-2][b] == 'Y')):
			  if m.board[a-2][b] == '-':
				v, m = set_human_vec(a-1,b,v,m)
				v, m = set_comp_vec(a,b,a-2,b,v,m)
				m.board[a-1][b] = '-'
				m.board[a-2][b] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v, m, 1
			  elif m.board[a-2][b] == 'Y':
				m.board[a-1][b] = '-'
				m.board[a-2][b] = '0'
				m.board[a][b]='-'
				v.display(m.board)
				print "Computer Won"
				exit()


		  elif (m.board[a+1][b] == '1' and (m.board[a+2][b] == '-' or m.board[a+2][b] == 'Y')):
			  if m.board[a+2][b] == '-':
				v, m = set_human_vec(a+1,b,v,m)
				v, m = set_comp_vec(a,b,a+2,b,v,m)
				m.board[a+1][b] = '-'
				m.board[a+2][b] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v, m, 1
			  elif m.board[a+2][b] == 'Y':
				m.board[a+1][b] = '-'
				m.board[a+2][b] = '0'
				m.board[a][b]='-'
				v.dispaly(m.board)
				print "Computer Won"
				exit()


		  elif (m.board[a][b-1] == '1' and (m.board[a][b-2] == '-' or m.board[a][b-2] == 'Y')):
			  if m.board[a][b-2] == '-':
				v, m = set_human_vec(a,b-1,v,m)
				v, m = set_comp_vec(a,b,a,b-2,v,m)
				m.board[a][b-1] = '-'
				m.board[a][b-2] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v, m, 1
			  elif m.board[a][b-2] == 'Y':
				m.board[a][b-1] = '-'
				m.board[a][b-2] = '0'
				m.board[a][b]='-'
				v.display(m.board)
				print "Computer Won"
				exit()


		  elif (m.board[a][b+1] == '1' and (m.board[a][b+2] == '-' or m.board[a][b+2] == 'Y')):
			  if m.board[a][b+2] == '-':
				v, m = set_human_vec(a,b+1,v,m)
				v, m = set_comp_vec(a,b,a,b+2,v,m)
				m.board[a][b+1] = '-'
				m.board[a][b+2] = '0'
				m.board[a][b] = '-'
				m.humancount=m.humancount+1
				return v, m, 1

			  elif m.board[a][b+2] == 'Y':
				m.board[a][b+1] = '-'
				m.board[a][b+2] = '0'
				m.board[a][b]='-'
				v.display(m.board)
				print "Computer Won"
				exit()
	return v, m, 0


####################################################
#setting the vector postion to 100 if there is a capture

def set_human_vec(a,b,v,m):

	for i in range(6):
		
		if (m.human[i][0] == a and m.human[i][1] == b):
			m.human[i][0] = 100
			m.human[i][1] = 100
	return v, m

#####################################################
#Setting the vector postion to new postion after capture

def set_comp_vec(a,b,c,d,v,m):


	for i in range(6): 
		if (m.computer[i][0] == a and m.computer[i][1] == b):
			m.computer[i][0] = c
			m.computer[i][1] = d
	return v, m


############################################################
#The below three functions give all possible moves for plain move

def call_plain(v,m):

	for i in range(6):
		a=m.computer[i][0]
		b=m.computer[i][1] 
		if(a != 100 and b != 100):


		   if m.board[a+1][b-1] == '-' or m.board[a+1][b-1] == 'Y':

			if(m.board[a+1][b-1] == '-'):
				m.board[a+1][b-1] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a+1,b-1,v,m) 
				return v, m, 1
			elif(m.board[a+1][b-1] == 'Y'):
				m.board[a+1][b-1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


		   elif m.board[a+1][b+1] == '-' or m.board[a+1][b+1] == 'Y':

			if(m.board[a+1][b+1] == '-'):
				m.board[a+1][b+1] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a+1,b+1,v,m) 
				return v,m,1
			elif(m.board[a+1][b+1] == 'Y'):
				m.board[a+1][b+1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


		   elif m.board[a+1][b] == '-' or m.board[a+1][b] == 'Y':

			if(m.board[a+1][b] == '-'):
				m.board[a+1][b] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a+1,b,v,m) 
				return v, m, 1
			elif(m.board[a+1][b] == 'Y'):
				m.board[a+1][b] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


	return v, m, 0



#####################################################################################

def call_plain_samerow(v,m):


	for i in range(6):
		a=m.computer[i][0]
		b=m.computer[i][1] 
		if(a != 100 and b != 100):

		   if m.board[a][b+1] == '-' or m.board[a][b+1] == 'Y':

			if(m.board[a][b+1] == '-'):
				m.board[a][b+1] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a,b+1,v,m) 
				return v,m,1
			elif(m.board[a][b+1] == 'Y'):
				m.board[a][b+1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()

		   elif m.board[a][b-1] == '-' or m.board[a][b-1] == 'Y':

			if(m.board[a][b-1] == '-'):
				m.board[a][b-1] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a,b-1,v,m) 
				return v,m,1
			elif(m.board[a][b-1] == 'Y'):
				m.board[a][b-1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()

	return v, m, 0



###################################################################################


def call_plain_back(v,m):

	for i in range(6):
		a=m.computer[i][0]
		b=m.computer[i][1] 
		if(a != 100 and b != 100):


		   if m.board[a-1][b-1] == '-' or m.board[a-1][b-1] == 'Y':
			if(m.board[a-1][b-1] == '-'):
				m.board[a-1][b-1] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a-1,b-1,v,m) 
				return v, m, 1
			elif(m.board[a-1][b-1] == 'Y'):
				m.board[a-1][b-1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()

		   if m.board[a-1][b] == '-' or m.board[a-1][b] == 'Y':

			if(m.board[a-1][b] == '-'):
				m.board[a-1][b] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a-1,b,v,m) 
				return v,m,1
			elif(m.board[a-1][b] == 'Y'):
				m.board[a-1][b] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()

		   if m.board[a-1][b+1] == '-' or m.board[a-1][b+1] == 'Y':

			if(m.board[a-1][b+1] == '-'):
				m.board[a-1][b+1] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a-1,b+1,v,m) 
				return v, m, 1
			elif(m.board[a-1][b+1] == 'Y'):
				m.board[a-1][b+1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()

	return v,m,0



###################################################################################################
#The below three functions check for opponents postion before generating 8 possible plain moves

def call_plain_back_check(v,m):

	for i in range(6):
		a=m.computer[i][0]
		b=m.computer[i][1]


		if(a != 100 and b != 100):

		   if m.board[a-1][b-1] == '-' or m.board[a-1][b-1] == 'Y':

			if(m.board[a-1][b-1] == '-'):
			   if(m.board[a-1][b-2] != '1' and m.board[a-1][b] != '1' and m.board[a][b-2] != '1' and m.board[a][b-1] != \
					   '1' and m.board[a-2][b-2] != '1' and m.board[a-2][b-1] != '1' and m.board[a-2][b] != '1'):
				m.board[a-1][b-1] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a-1,b-1,v,m) 
				return v, m, 1
			elif(m.board[a-1][b-1] == 'Y'):
				m.board[a-1][b-1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


		   elif m.board[a-1][b] == '-' or m.board[a-1][b] == 'Y':


			if(m.board[a-1][b] == '-'):
			   if(m.board[a-2][b-1] != '1' and m.board[a-2][b] != '1'and m.board[a-2][b+1] != '1' and m.board[a-1][b-1] != '1'  \
					  and m.board[a-1][b+1] != '1' and m.board[a][b-1] != '1' and m.board[a][b+1] != '1'):
				m.board[a-1][b] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a-1,b,v,m) 
				return v,m,1
			elif(m.board[a-1][b] == 'Y'):
				m.board[a-1][b] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


		   elif m.board[a-1][b+1] == '-' or m.board[a-1][b+1] == 'Y':

			if(m.board[a-1][b+1] == '-'):
			   if(m.board[a-1][b] != '1' and m.board[a-1][b+2] != '1'and m.board[a][b+1] != '1' and m.board[a][b+2] != \
					   '1' and m.board[a-2][b] != '1' and m.board[a-2][b+1] != '1' and m.board[a-2][b+2] != '1'):
				m.board[a-1][b+1] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a-1,b+1,v,m) 
				return v, m, 1
			elif(m.board[a-1][b+1] == 'Y'):
				m.board[a-1][b+1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


	return v,m,0



##################################################################################################


def call_plain_check(v,m):


	for i in range(6):
		a=m.computer[i][0]
		b=m.computer[i][1]


		if(a != 100 and b != 100):

			if(m.board[a+1][b-1] == '-'):
			   if(m.board[a+1][b-2] != '1' and m.board[a+1][b] != '1' and m.board[a+2][b-2] != '1' and m.board[a+2][b-1] != \
					   '1' and m.board[a+2][b] != '1' and m.board[a][b-2] != '1' and m.board[a][b-1] != '1'):
				m.board[a+1][b-1] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a+1,b-1,v,m) 
				return v, m, 1
			elif(m.board[a+1][b-1] == 'Y'):
				m.board[a+1][b-1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


			if(m.board[a+1][b+1] == '-'):
			   if(m.board[a+1][b] != '1' and m.board[a+1][b+2] != '1'and m.board[a][b+1] != '1' and m.board[a][b+2] != '1'  \
					  and m.board[a+2][b] != '1' and m.board[a+2][b+1] != '1' and m.board[a+2][b+2] != '1'):
				m.board[a+1][b+1] = '0'
				m.board[a][b] = '-'
				v, m = set_comp_vec(a,b,a+1,b+1,v,m) 
				return v,m,1
			elif(m.board[a+1][b+1] == 'Y'):
				m.board[a+1][b+1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()

			if(m.board[a+1][b] == '-'):
			   if(m.board[a+1][b-1] != '1' and m.board[a+1][b+1] != '1'and m.board[a][b-1] != '1' and m.board[a][b+1] != \
					   '1' and m.board[a+2][b-1] != '1' and m.board[a+2][b] != '1' and m.board[a+2][b+1] != '1'):
				m.board[a+1][b] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a+1,b,v,m) 
				return v, m, 1
			elif(m.board[a+1][b] == 'Y'):
				m.board[a+1][b] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


	return v,m,0


####################################################################################



def call_plain_samerow_check(v,m):


	for i in range(6):
		a=m.computer[i][0]
		b=m.computer[i][1]


		if(a != 100 and b != 100):


			if(m.board[a][b+1] == '-'):
			   if(m.board[a+1][b] != '1' and m.board[a+1][b+1] != '1' and m.board[a+1][b+2] != \
				   '1' and m.board[a][b+2] != '1' and m.board[a-1][b] != '1' and m.board[a-1][b+1] != '1' and m.board[a-1][b+2] != '1'):
				m.board[a][b+1] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a,b+1,v,m) 
				return v,m,1
			elif(m.board[a][b+1] == 'Y'):
				m.board[a][b+1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()


		if(a != 100 and b != 100):

			if(m.board[a][b-1] == '-'):
			   if(m.board[a][b-2] != '1' and m.board[a-1][b-2] != '1' and m.board[a-1][b-1] != \
				   '1' and m.board[a-1][b] != '1' and m.board[a+1][b-2] != '1' and m.board[a+1][b-1] != '1' and m.board[a+1][b] != '1'):
				m.board[a][b-1] = '0'
				m.board[a][b] = '-'
				v,m = set_comp_vec(a,b,a,b-1,v,m) 
				return v,m,1
			elif(m.board[a][b-1] == 'Y'):
				m.board[a][b-1] = '0'
				m.board[a][b] = '-'
				v.display(m.board)
				print ("Computer Won")
				exit()

	return v,m,0



#####################################################################################



def main():


 m=Model()
 v=View()
 v.display(m.board)

 print "\nYour pieces are marked as 1, Computer pieces are marked as 0 \n\n"

 level_inp = input("\n\nPress 1 for easy level, press 2 for not easy level\n\n")

 m.level = level_inp

 inp = input("\n\nPress 1 if you want to play first else press 2 if you let computer to play first \n\n")

 if inp == 1:
	call_human(v,m);
 else:
	call_computer(v,m);


########################################################
def alp_bet():
	m=Model()
	v=View()
	x,y = call_alpha_beta(v,m,m.ninf,m.pinf)

########################################################


def call_alpha_beta(v,m,alp,bet):
	v1=deepcopy(v)
	m1=deepcopy(m)
	v,m,vout = max_value(v1,m1,alp,bet,level)
	v.display(m.board)


#########################################################
#This is the max function of the alpha beta algorithm

def max_value(v,m,alp,bet,level):

	if m.humancount == 6 :
		m.win = 500
		return v,m
	for i in range (6):
		a = m.computer[i][0]
		b = m.computer[i][1]
		if a ==13 and (b == 4 or b== 5):
			m.win = 500
			return v,m
	algov = m.ninf

	for i in range(6):
		a = m.computer[i][0]
		b = m.computer[i][1]

		if a != 100 and b != 100:
			
			v,m,val2 = call_capturing(v,m,a,b)
			if val1 == 1:
				return v,m,1000

			v,m,val2 = call_plain(v,m,alp,a,b)
			level = level-1
			v,m,algores = min_value(v,m,alp,bet,level)
			algov = max(algov,algores)

			if algov >= bet:
				return v,m,algov
			alp = max(alp,algov)


	if (m.level == 0):
		res = call_eval(v,m,0)	
		return v,m,res


#######################################################################

#This is the min function of the alpha beta algorithm

def min_value(v,m,alp,bet,level):


	if m.humancount == 6:
		m.win = 500
		return v,m
	for i in range (6):
		a = m.human[i][0]
		b = m.human[i][1]
		if a ==13 and (b == 4 or b== 5):
			m.win = 500
			return v,m
	algov = m.ninf

	for i in range(6):
		a = m.human[i][0]
		b = m.human[i][1]

		if a != 100 and b != 100:
			
			v,m,val2 = call_capturing(v,m,a,b)
			if val1 == 1:
				return v,m,1000

			v,m,val2 = call_plain(v,m,alp,a,b)
			level = level-1
			v,m,algores = min_value(v,m,alp,bet,level)
			algov = max(algov,algores)

			if algov >= bet:
				return v,m,algov
			alp = max(alp,algov)



	if (m.level == 0):
		res = call_eval(v,m,1)
		return v,m,res
	
		
#########################################################



def get_possible_moves(a,b):
	x= []
	x.append([])
	x.append([])
	x.append([])
	x.append([])
	x.append([])
	x.append([])
	x.append([])
	x.append([])


	x[0][0] = a-1
	x[0][1] = b-1
	x[1][0] = a-1
	x[1][1] = b
	x[2][0] = a-1
	x[2][1] = b+1
	x[3][0] = a
	x[3][1] = b-1
	x[4][0] = a
	x[4][1] = b+1
	x[5][0] = a+1
	x[5][1] = b-1
	x[6][0] = a+1
	x[6][1] = b
	x[7][0] = a+1
	x[7][1] = b-1

	return x


##########################################################################
#This is the evaluation function

def call_eval(v,m,typeval):

 if typeval == 0:


	a=m.computer[0][0]
	b=m.computer[0][1]
	c=m.computer[1][0]
	d=m.computer[1][1]
	e=m.computer[2][0]
	f=m.computer[2][1]
	g=m.computer[3][0]
	h=m.computer[3][1]
	i=m.computer[4][0]
	j=m.computer[4][1]
	k=m.computer[5][0]
	l=m.computer[6][1]

	p=13
	q=4
	r=5

	castle1 = math.sqrt((a-p)*(a-p) + (b-q)*(b-q)) + math.sqrt((c-p)*(c-p)+(d-q)*(d-q)) + math.sqrt((e-p)*(e-p) + (f-q)*(f-q)) \
		+ math.sqrt((g-p)*(g-p) + (h-q)*(h-q)) + math.sqrt((i-p)*(i-p)+(j-q)*(j-q)) + math.sqrt((k-p)*(k-p) + (l-q)*(l-q))
	
	castle2 = math.sqrt((a-p)*(a-p) + (b-r)*(b-r)) + math.sqrt((c-p)*(c-p)+(d-r)*(d-r)) + math.sqrt((e-p)*(e-p) + (f-r)*(f-r)) \
			+ math.sqrt((g-p)*(g-p) + (h-r)*(h-r)) + math.sqrt((i-p)*(i-p)+(j-r)*(j-r)) + math.sqrt((k-p)*(k-p) + (l-r)*(l-r))

	return (castle1+castle2/m.pinf)

 else:

	a=m.human[0][0]
	b=m.human[0][1]
	a=m.human[1][0]
	b=m.human[1][1]
	a=m.human[2][0]
	b=m.human[2][1]
	a=m.human[3][0]
	b=m.human[3][1]
	a=m.human[4][0]
	b=m.human[4][1]
	a=m.human[5][0]
	b=m.human[6][1]


	p=0
	q=4
	r=5

	castle1 = math.sqrt((a-p)*(a-p) + (b-q)*(b-q)) + math.sqrt((c-p)*(c-p)+(d-q)*(d-q)) + math.sqrt((e-p)*(e-p) + (f-q)*(f-q)) \
		  + math.sqrt((g-p)*(g-p) + (h-q)*(h-q)) + math.sqrt((i-p)*(i-p)+(j-q)*(j-q)) + math.sqrt((k-p)*(k-p) + (l-q)*(l-q))
	
	castle2 = math.sqrt((a-p)*(a-p) + (b-r)*(b-r)) + math.sqrt((c-p)*(c-p)+(d-r)*(d-r)) + math.sqrt((e-p)*(e-p) + (f-r)*(f-r)) \
		  + math.sqrt((g-p)*(g-p) + (h-r)*(h-r)) + math.sqrt((i-p)*(i-p)+(j-r)*(j-r)) + math.sqrt((k-p)*(k-p) + (l-r)*(l-r))

	return (castle1+castle2/m.pinf)



##########################################################################

main()

##########################################################################
