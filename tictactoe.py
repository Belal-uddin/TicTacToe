import pygame
from pygame.locals import*

pygame.init()


screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")


line_width = 6
markers = []
player = 1
game_over = False
winner  = 0
clicked = False
pos = (0, 0)
player = 1
green = (0, 255, 0)
red = (255, 0, 0)
cross_color = (0,0,128)
circle_color = 	(255,140,0)
font = pygame.font.SysFont(None,40)
replay_rect = Rect(screen_width//2-80,screen_height//2,160,50)

def draw_grid():
    bg = (60,179,113)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x*100),
                         (screen_width, x*100), line_width)
        pygame.draw.line(screen, grid, (x*100, 0),
                         (x*100, screen_height), line_width)


for x in range(3):
    row = [0]*3
    markers.append(row)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, cross_color, (x_pos*100+15, y_pos*100+15),(x_pos*100+85, y_pos*100+85), line_width)
                pygame.draw.line(screen, cross_color, (x_pos*100+15, y_pos*100+85),(x_pos*100+85, y_pos*100+15), line_width)
            if y == -1:
                pygame.draw.circle(screen, circle_color, (x_pos*100+50, y_pos*100+50), 38, 4)
            y_pos += 1
        x_pos += 1

def check_winner():
    global game_over
    global winner
    y = 0
    for x in markers:
        if sum(x) ==3:
            winner = 1
            game_over = True
        if sum(x)==-3:
            winner = 2
            game_over = True
        if markers[0][y]+markers[1][y]+markers[2][y] == 3:
            winner =1
            game_over = True
        if markers[0][y]+markers[1][y]+markers[2][y] == -3:
            winner =2
            game_over = True
        y+=1
    if markers[0][0]+markers[1][1]+markers[2][2]==3 or markers[0][2]+markers[1][1]+markers[2][0]==3:
        winner =1
        game_over = True
    if markers[0][0]+markers[1][1]+markers[2][2]==-3 or markers[0][2]+markers[1][1]+markers[2][0]==-3:
        winner =2
        game_over = True
    

    if game_over == False:
        tie = True
        for row in markers:
            for cell in row:
                if cell == 0:
                    tie = False
        if tie == True:
            winner =0
            game_over = True
        


def draw_winner(winner):
    if winner!=0:
         win_text = "Belal,You won!"
    elif winner == 0:
         win_text = "You have a tie!"  
    
    win_im = font.render(win_text,True,(0,0,255))
    pygame.draw.rect(screen,green,(screen_width//2 -100,screen_height//2-60,200,50))
    screen.blit(win_im,(screen_width//2-100,screen_height//2-50))
    
    replay_text = "Play again?"
    replay_im = font.render(replay_text,True,(0,0,255))
    pygame.draw.rect(screen,green,replay_rect)
    screen.blit(replay_im,(screen_width//2-80,screen_height//2+10))
    
    
    
run = True
while run:
    # events handling...
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over ==0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0] // 100
                cell_y = pos[1] // 100 
                if markers[cell_x][cell_y] == 0:
                    markers[cell_x][cell_y] = player
                    player *= -1
                    check_winner()
                    
                    
    if game_over ==True:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if replay_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0]*3
                    markers.append(row)
    pygame.display.update()

pygame.quit()
