import sys
import pyglet
import time
import random

def monitorQueue(number_of_people, current_time):
		number_of_people_in_the_queue = number_of_people
		atime = current_time
		label_title = pyglet.text.Label('LUNCH QUEUE',
								   font_name='Comic Sans',
								   font_size=15,
								   x=window.width//2, y=window.height-10,
								   anchor_x='center', anchor_y='center')
		label_time = pyglet.text.Label(atime,
								   font_name='Comic Sans',
								   font_size=15,
								   x=window.width-30, y=window.height-10,
								   anchor_x='center', anchor_y='center')
		@window.event
		def on_draw():
			window.clear()
			image_background.blit(0,0)
			n = 5
			line = window.height-100
			image_door.blit(n,line)
			
			for i in range(number_of_people_in_the_queue):
				if  line <= 10:
					image_error.blit(window.width//4,window.height//8)
					pyglet.app.exit()
				if n >= window.width//1.05:
					n = 15
					line -= 50
				n += 25
				randomInterget = random.randint(1,4)
				if randomInterget == 1:
					image_human1.blit(n, line)
				elif randomInterget == 2:
					image_human2.blit(n,line)
				elif randomInterget == 3:
					image_human3.blit(n,line)
				else:
					randomInterget = random.randint(1,50)
					if randomInterget == 1:
						image_door.blit(n,line)
					else:
						image_human1.blit(n,line)
					
			label_title.draw()
			label_time.draw()
			pyglet.app.exit()	
		pyglet.app.run()
		
window = pyglet.window.Window(fullscreen=False, caption='Lunch Queue - Grammar School At Leeds', width = 1000, height = 600)
icon = pyglet.image.load('icon.png')
image_background = pyglet.image.load('background.png')
window.set_icon(icon)
image_human2 = pyglet.image.load('Human2.png')
image_human1 = pyglet.resource.image('Human3.png')
image_error = pyglet.resource.image('error.png')
image_door = pyglet.resource.image('door.png')
image_human3 = pyglet.resource.image('Human1.png')
n = [10,20,30,40,300,10,5]
atime = ['12:50','12:51','12:52','12:53','12:54','12:55','12:56']

for i in range(len(n)):
		monitorQueue(n[i], atime[i])

input("ENTER\t(TO LEAVE)\t>>>")
sys.exit(0)

