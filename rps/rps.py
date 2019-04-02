import pygame,time
import random

pygame.init()

w,h=(800,600)
bg_color=(255,255,255)

rock_img = pygame.image.load('ro.jpg')
paper_img = pygame.image.load('pa.jpg')
scissor_img = pygame.image.load('sc.png')


def set_text(string,_font,_size):
	global w,h,bg_color
	
	font = pygame.font.Font(_font, _size)
	text = font.render(string, True, (0,0,0), (256,256,256))
	textRect = text.get_rect()
	textRect.center = (400, 300)
	screen.fill(bg_color)
	screen.blit(text,textRect)
	pygame.display.update()


def call_act(n):
    global w,h
    x=w/2
    y=h/2
    if(n==1):
        set_text("ROCK",'m_font.ttf',30)
    elif(n==2):
        set_text("PAPER",'m_font.ttf',30)
    else:
        set_text("SCISSOR",'m_font.ttf',30)   


screen=pygame.display.set_mode((w,h))
pygame.display.set_caption('Rock Paper Scissor')
set_text("ROCK, PAPER, SCISSORS!","m_font.ttf",50)
time.sleep(5)


set_text("3","n_font.ttf",60)
time.sleep(1)
set_text("2","n_font.ttf",60)
time.sleep(1)
set_text("1","n_font.ttf",60)
time.sleep(1)
while(1):

    n=random.randint(1,3)
    call_act(n)
    time.sleep(3)
