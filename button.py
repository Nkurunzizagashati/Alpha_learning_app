import pygame
import pygame_gui
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ALPHA KIDS")
main_font = pygame.font.SysFont("cambria", 50)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):   #defining attributes for our button
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)       #drawing an image on the screen, where the rect is
		screen.blit(self.text, self.text_rect)   #writing our text where the rect is

	def checkForInput(self, position):     #checks for our mouse position and checks if it is in the relms of our button object
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position): #if we are hovering over our button, its textcolor changes to green, while if not, its textcolor changes to white
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

button_image = pygame.image.load("button.png")   #loading our button
button_image = pygame.transform.scale(button_image, (300, 100))   #scaling our button

button = Button(button_image, 400, 500, "NEXT")  #creating an instance of our button

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:  #chcking if user pressed the mouse button
			button.checkForInput(pygame.mouse.get_pos())    #checking for input

	screen.fill("white")  #filling our background with a color

	button.update()   #calling our method
	button.changeColor(pygame.mouse.get_pos())      #calling our method

	pygame.display.update()   #updating the display