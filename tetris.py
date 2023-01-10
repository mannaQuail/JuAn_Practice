import pygame as pg
from random import randint
import math
import time

pg.init()

black = (0,0,0)
orange = (255, 165, 0)
fuchsia = (255, 0, 255)
yellow = (255, 255, 0)
aqua = (0, 255, 255) 
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gray = (128,128,128)
white = (255,255,255)
colors = (white, orange, fuchsia, aqua, yellow, red, green, blue, gray, black)

size = [600,550]
screen = pg.display.set_mode(size)
font = pg.font.SysFont("arial", 30, True, True)
done = False
clock = pg.time.Clock()

block_type = (
	(
		(0, 0, 1,
		1, 1, 1,
		0, 0, 0),
		(0, 1, 0,
		0, 1, 0,
		0, 1, 1),
		(0, 0, 0,
		1, 1, 1,
		1, 0, 0),
		(1, 1, 0,
		0, 1, 0,
		0, 1, 0)
	), (
		(2, 0, 0,
		2, 2, 2,
		0, 0, 0),
		(0, 2, 2,
		0, 2, 0,
		0, 2, 0),
		(0, 0, 0,
		2, 2, 2,
		0, 0, 2),
		(0, 2, 0,
		0, 2, 0,
		2, 2, 0)
	), (
		(0, 3, 0,
		3, 3, 3,
		0, 0, 0),
		(0, 3, 0,
		0, 3, 3,
		0, 3, 0),
		(0, 0, 0,
		3, 3, 3,
		0, 3, 0),
		(0, 3, 0,
		3, 3, 0,
		0, 3, 0)
	), (
		(4, 4, 0,
		0, 4, 4,
		0, 0, 0),
		(0, 0, 4,
		0, 4, 4,
		0, 4, 0),
		(0, 0, 0,
		4, 4, 0,
		0, 4, 4),
		(0, 4, 0,
		4, 4, 0,
		4, 0, 0)
	), (
		(0, 5, 5,
		5, 5, 0,
		0, 0, 0),
		(0, 5, 0,
		0, 5, 5,
		0, 0, 5),
		(0, 0, 0,
		0, 5, 5,
		5, 5, 0),
		(5, 0, 0,
		5, 5, 0,
		0, 5, 0)
	), (
		(6, 6,
		6, 6),
		(6, 6,
		6, 6),
		(6, 6,
		6, 6),
		(6, 6,
		6, 6)
	), (
		(0, 7, 0, 0,
		0, 7, 0, 0,
		0, 7, 0, 0,
		0, 7, 0, 0),
		(0, 0, 0, 0,
		7, 7, 7, 7,
		0, 0, 0, 0,
		0, 0, 0, 0),
		(0, 0, 7, 0,
		0, 0, 7, 0,
		0, 0, 7, 0,
		0, 0, 7, 0),
		(0, 0, 0, 0,
		0, 0, 0, 0,
		7, 7, 7, 7,
		0, 0, 0, 0)
	)
)

field = []

def setting_init_field():
	global field
	field = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 10,
		10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10,
		10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

def draw(color,x,y):
	pg.draw.rect(screen,colors[color],[x,y,25,25])

class Block:
	def __init__(self, num):
		self.turn = 0
		self.shape = num
		self.x = 5
		self.y = 1

	def turn_block(self):
		no_problem = True
		check_no_problem = []
		count_no_problem = 0
		save = self.turn
		check = []
		count = 0

		if self.turn==3:
			future = 0
		else:
			future = self.turn + 1

		for i in block_type[self.shape-1][future]:
			if i!=0:
				check_no_problem.append(count_no_problem)
			count_no_problem += 1
		for i in check_no_problem:
			xx = i%int(math.sqrt(len(block_type[self.shape-1][future])))
			yy = i/int(math.sqrt(len(block_type[self.shape-1][future])))
			if block_type[self.shape-1][self.turn][xx+yy*int(math.sqrt(len(block_type[self.shape-1][future])))]==0:
				if field[self.x+xx+(self.y+yy)*14]!=0:
					no_problem = False

		if no_problem==True:
			if self.turn==3:
				self.turn = 0
			else:
				self.turn += 1

			for i in block_type[self.shape-1][save]:
				if i!=0:
					check.append(11)
				else:
					check.append(0)
			for i in block_type[self.shape-1][self.turn]:
				if i!=0:
					check[count] = block_type[self.shape-1][self.turn][count]
				count += 1
			for i in range(0,len(block_type[self.shape-1][self.turn])):
				if check[i]==self.shape:
					check[i] = 0

			for i in range(0,int(math.sqrt(len(block_type[self.shape-1][self.turn])))):
				for j in range(0,int(math.sqrt(len(block_type[self.shape-1][self.turn])))):
					if check[i*int(math.sqrt(len(block_type[self.shape-1][self.turn])))+j]!=0:
						field[self.x+j+(self.y+i)*14] = 0

	def real_block(self, way):
		if way=="up":
			check = []
			for i in range(0,len(block_type[self.shape-1][self.turn])):
				if block_type[self.shape-1][self.turn][i]!=0:
					check.append(i)
			sudo_check = check[:]
			for i in sudo_check:
				if i-int(math.sqrt(len(block_type[self.shape-1][self.turn]))) in check:
					check.pop(check.index(i))

			return check
		elif way=="down":
			check = []
			for i in range(0,len(block_type[self.shape-1][self.turn])):
				if block_type[self.shape-1][self.turn][i]!=0:
					check.append(i)
			sudo_check = check[:]
			for i in sudo_check:
				if i+int(math.sqrt(len(block_type[self.shape-1][self.turn]))) in check:
					check.pop(check.index(i))

			return check

		elif way=="right":
			check = []
			count = 0
			for i in range(0,int(math.sqrt(len(block_type[self.shape-1][self.turn])))):
				save = None
				for j in range(0,int(math.sqrt(len(block_type[self.shape-1][self.turn])))):
					if block_type[self.shape-1][self.turn][i*int(math.sqrt(len(block_type[self.shape-1][self.turn])))+j]!=0:
						if save==None:
							save = count
						elif save<count:
							save = count
					count += 1
				check.append(save)

			return check

		elif way=="left":
			check = []
			count = 0
			for i in range(0,int(math.sqrt(len(block_type[self.shape-1][self.turn])))):
				save = None
				for j in range(0,int(math.sqrt(len(block_type[self.shape-1][self.turn])))):
					if block_type[self.shape-1][self.turn][i*int(math.sqrt(len(block_type[self.shape-1][self.turn])))+j]!=0:
						if save==None:
							save = count
					count += 1
				check.append(save)
			
			return check
				

	def update_block(self):
		if self.shape==6:
			for i in range(0,2):
				for j in range(0,2):
					field[self.x+j+(self.y+i)*14] = block_type[self.shape-1][self.turn][j+i*2]

		elif self.shape==7:
			for i in range(0,4):
				for j in range(0,4):
					if block_type[self.shape-1][self.turn][j+i*4]!=0:
						field[self.x+j+(self.y+i)*14] = block_type[self.shape-1][self.turn][j+i*4]

		else:
			for i in range(0,3):
				for j in range(0,3):
					if block_type[self.shape-1][self.turn][j+i*3]!=0:
						field[self.x+j+(self.y+i)*14] = block_type[self.shape-1][self.turn][j+i*3]

	def down_block(self):
		check = True
		real_up = self.real_block("up")
		real_down = self.real_block("down")
		for i in real_down:
			xx = i%int(math.sqrt(len(block_type[self.shape-1][self.turn])))
			yy = i/int(math.sqrt(len(block_type[self.shape-1][self.turn])))

			if field[self.x+xx+(self.y+yy+1)*14]!=0:
				check = False

		if check==True:
			self.y += 1
			for i in real_up:
				xx = i%int(math.sqrt(len(block_type[self.shape-1][self.turn])))
				yy = i/int(math.sqrt(len(block_type[self.shape-1][self.turn])))

				field[self.x+xx+(self.y+yy-1)*14] = 0
			return False

		elif check==False:
			return True

	def move_block_2_left(self):
		check = True
		real_left = self.real_block("left")
		while None in real_left:
			real_left.pop(real_left.index(None))
		real_right = self.real_block("right")
		while None in real_right:
			real_right.pop(real_right.index(None))
		for i in real_left:
			xx = i%int(math.sqrt(len(block_type[self.shape-1][self.turn])))
			yy = i/int(math.sqrt(len(block_type[self.shape-1][self.turn])))

			if field[self.x+xx-1+(self.y+yy)*14]!=0:
				check = False

		if check==True:
			self.x -= 1
			for i in real_right:
				xx = i%int(math.sqrt(len(block_type[self.shape-1][self.turn])))
				yy = i/int(math.sqrt(len(block_type[self.shape-1][self.turn])))

				field[self.x+xx+1+(self.y+yy)*14] = 0
		

	def move_block_2_right(self):
		check = True
		real_left = self.real_block("left")
		while None in real_left:
			real_left.pop(real_left.index(None))
		real_right = self.real_block("right")
		while None in real_right:
			real_right.pop(real_right.index(None))

		for i in real_right:
			xx = i%int(math.sqrt(len(block_type[self.shape-1][self.turn])))
			yy = i/int(math.sqrt(len(block_type[self.shape-1][self.turn])))

			if field[self.x+xx+1+(self.y+yy)*14]!=0:
				check = False

		if check==True:
			self.x += 1
			for i in real_left:
				xx = i%int(math.sqrt(len(block_type[self.shape-1][self.turn])))
				yy = i/int(math.sqrt(len(block_type[self.shape-1][self.turn])))

				field[self.x+xx-1+(self.y+yy)*14] = 0

def draw_field():
	for i in range(0, 23):
		for j in range(0, 14):
			if field[i*14+j]==0:
				draw(0,j*25,i*25)
			elif field[i*14+j]==1:
				draw(1,j*25,i*25)
			elif field[i*14+j]==2:
				draw(2,j*25,i*25)
			elif field[i*14+j]==3:
				draw(3,j*25,i*25)
			elif field[i*14+j]==4:
				draw(4,j*25,i*25)
			elif field[i*14+j]==5:
				draw(5,j*25,i*25)
			elif field[i*14+j]==6:
				draw(6,j*25,i*25)
			elif field[i*14+j]==7:
				draw(7,j*25,i*25)
			elif field[i*14+j]==8:
				draw(8,j*25,i*25)	
			elif field[i*14+j]==9:
				draw(9,j*25,i*25)

# def set_new_block():
# 	rand = randint(1,7)


def creat_new_block():
	rand = randint(1,7)
	new_block = Block(rand)
	new_block.update_block()
	return new_block

def check_line():
	result = 0
	for i in range(1,21):
		check = True
		for j in range(2,12):
			if field[i*14+j]==0:
				check = False
		if check==True:
			if i!=1:
				return i
				break
		else:
			result += 1
	if result==20:
		return None

def delete_line(line):
	l = range(2,line+1)
	l.reverse()
	for i in l:
		for j in range(2,12):
			field[j+i*14] = field[j+(i-1)*14]

def death_check():
	check = False
	for i in range(2, 12):
		if field[i+28]!=0:
			check = True
	if check==True:
		return True

def runGame():
	global done
	reach = True
	setting_init_field()
	time_check = 0
	score = 0
	level = 9
	new_block = Block(1)
	while not done:
		clock.tick(20)
		screen.fill(black)
		if score>=300 and score<600:
			while level>=9:
				level-=1
		elif score>=600 and score<900:
			while level>=8:
				level-=1
		elif score>=900 and score<1200:
			while level>=7:
				level-=1
		elif score>=1200 and score<1500:
			while level>=6:
				level-=1
		elif score>=1500 and score<1800:
			while level>=5:
				level-=1
		elif score>=1800 and score<2100:
			while level>=4:
				level-=1
		elif score>=2100 and score<2400:
			while level>=3:
				level-=1
		elif score>=2400:
			while level>=2:
				level-=1


		if time_check==level:
			if reach==True:
				if death_check()==True:
					done = True
				while check_line()!=None:
					line = check_line()
					delete_line(line)
					score += 100

				new_block = creat_new_block()
				reach = False
				
			reach = new_block.down_block()
			new_block.update_block()

			time_check = 0
			continue
		else:
			time_check+=1


		for event in pg.event.get():
			if event.type==pg.KEYDOWN:
				if event.key==pg.K_LEFT:
					new_block.move_block_2_left()
					new_block.update_block()

				elif event.key==pg.K_RIGHT:
					new_block.move_block_2_right()
					new_block.update_block()

				if event.key==pg.K_UP:
					new_block.turn_block()
					new_block.update_block()

				if event.key==pg.K_DOWN:
					continue

			if event.type == pg.QUIT:
				done = True

		text = font.render(str(score), True, colors[1])
		if score==0:
			screen.blit(text, (450, 25))
		elif score>=100 and score<1000:
			screen.blit(text, (440, 25))
		elif score>=1000 and score<10000:
			screen.blit(text, (430, 25))	

		draw_field()
		pg.display.update()

runGame()
pg.quit()