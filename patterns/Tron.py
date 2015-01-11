from Graphics import *

class TronPlayer(object):
	def __init__(self, color, game, pos=(5,5)):
		self.game = game
		self.color = color
		
		self.pos = pos
		self.speed = 1
		self.deltax,self.deltay = 0,0
		
		self.body = []
		#put our head on our body
		self.body.append(self.pos)
		
		self.moveKeys = [K_LEFT, K_RIGHT, K_UP, K_DOWN]
		
		self.debug = False
		
	def inputHandling(self, event):
		pass
	def bindKey(self, key, action):
		self.moveKeys[action] = key
	def update(self, other):
		x,y = self.pos
		#update position
		x += self.deltax
		y += self.deltay
		#if tail goes offscreenit appears on the other side.
		if x >= matrix_width:
			x = 0
			self.pos = x,y
		elif x < 0:
			x = matrix_width-1
			self.pos = x,y
		elif y >= matrix_height:
			y = 0
			self.pos = x,y
		elif y < 0:
			y = matrix_height-1
			self.pos = x,y
		else:
			self.pos = x,y
		if self.debug:
			print self.deltax,self.deltay
			print x,y
	def draw(self):
		for x,y in self.body:
			self.game.graphics.drawPixel(x,y,self.color)

class Tron(object):
	pass

class OldTron(object): #version before creating players that handle processing on thier own.
	def __init__(self):
		self.graphics = Graphics(matrix_width, matrix_height)
		
		self.color = BLUE
		
		self.pos = random.randint(1,matrix_width-1), random.randint(1,matrix_height-1)
		self.speed = 1
		self.deltax,self.deltay = 0,0
		
		self.body = []
		
		#add our head to our body :)
		self.body.append(self.pos)
		
		self.player1 = TronPlayer(BLUE, self)
		self.player1.update(self)
		self.player1.draw()
		
		pygame.init()
		self.window = pygame.display.set_mode((80,60))
	def inputHandling(self):
		pass
	def update(self):
		x,y = self.pos
		#update position
		x += self.deltax
		y += self.deltay
		#if the tail goes offscreen it appears on the other side.
		if x >= matrix_width:
			x = 0
			self.pos = x,y
		elif x < 0:
			x = matrix_width-1
			self.pos = x,y
		elif y >= matrix_height:
			y = 0
			self.pos = x,y
		elif y < 0:
			y = matrix_height-1
			self.pos = x,y
		else:
			self.pos = x,y
		print self.deltax,self.deltay
		print x,y
		
		#look if our "tail is in the way" and only if we have a tail.
		if len(self.body) > 2:
			if len(self.body) != len(set(self.body)):
				print "GameOver!"
				self.body = [self.pos]
				self.deltax = 0; self.deltay = 0;
		#add current point to tail
		#only if we moved though
		if self.deltax or self.deltay:
			self.body.append(self.pos)
		
	def draw(self):
		for x,y in self.body:
			self.graphics.drawPixel(x,y,self.color)
	def generate(self):
		self.graphics.fill(BLACK)
		self.inputHandling()
		self.update()
		self.draw()
		self.player1.draw()
		return self.graphics.getSurface()
