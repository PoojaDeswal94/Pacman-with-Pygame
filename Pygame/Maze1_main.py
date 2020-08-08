import pygame,sys
import constants
import time

output=[]
PATH = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7)]
for elem in PATH:
    tempx=elem[0]*53
    tempy=elem[1]*53
    output.append((tempx,tempy))
        
print(PATH)
print(output)

def add_image(maze1):
    x=0
    y=0
   
    for i in range(0,len(maze1)):
        x=0
        for j in range(0,len(maze1[0])):
            if maze1[i][j]== '1':
                wall_image=pygame.image.load('block.png')
                def wall_img():
                    screen.blit(wall_image,(x,y))
                wall_img()
            elif maze1[i][j]== '0':
                path_image=pygame.image.load('path.png')
                def path_img():
                    screen.blit(path_image,(x,y))
                path_img()
            elif maze1[i][j]== 's':
                start_image=pygame.image.load('Pacman.png')
                def start_img():
                    screen.blit(start_image,(x,y))
                start_img()
            elif maze1[i][j]== 'e':
                end_image=pygame.image.load('reward.png')
                def end_img():
                    screen.blit(end_image,(x,y))
                end_img()
            else:
                break
            x+=53

        y+=53

    
        
        


def draw_grid(screen):
    for i in range(constants.column):
        new_height= round(i * constants.block_height)
        new_width= round(i * constants.block_width)
        pygame.draw.line(screen, constants.background, (0, new_height), (constants.screen_width, new_height), 2)
        pygame.draw.line(screen, constants.background, (new_width,0), (new_width, constants.screen_height), 2)

def game_loop(screen):
    gameExit=False
    gameOver=False
    sx=53
    sy=53
    sx_change=0
    sy_change=0
   
    while not gameExit:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                if event.key == pygame.K_c:
                        gameLoop()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sx_change = -block_size
                    sy_change = 0
                elif event.key == pygame.K_RIGHT:
                    sx_change = block_size
                    sy_change = 0
                elif event.key == pygame.K_UP:
                    sy_change = -block_size
                    sx_change = 0
                elif event.key == pygame.K_DOWN:
                    sy_change = block_size
                    sx_change = 0

        if sx >= constants.block_width or sx < 0 or sy >= constants.block_height or sy < 0:
            gameOver = True
      
        clock = pygame.time.Clock()
        blocksize=53
        FPS=30
        sx += sx_change
        sy += sy_change
        pygame.draw.rect(screen, constants.gold, [sx,sy,blocksize,blocksize])
        add_image(maze1)
        draw_grid(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
    pygame.display.set_caption(constants.title)
    icon = pygame.image.load('game.png')
    pygame.display.set_icon(icon)
    screen.fill(constants.background) 
    
    return screen


def loadMaze2(input_file):
    #load the data from the file into a 2D list
    with open(input_file) as i:
        maze2 = []
        for line in i:
            line = line.split()
            maze2.append(line)
            #print(line)
    return maze2

def loadMaze1(input_file):
    maze3=[]
    l=len(input_file)
    ln=len(input_file[0])
    for i in range(0,l):
        for j in range(0,ln):
            if input_file[i][j]== "1" :
                maze3.append(input_file[i][j])
            elif input_file[i][j]== "0" :
                maze3.append(input_file[i][j])
            elif input_file[i][j]== "s" :
                maze3.append(input_file[i][j])
            elif input_file[i][j]== "e" :
                maze3.append(input_file[i][j])
            else:
                continue
    def to_matrix(list1, n):
        return [list1[i:i+n] for i in range(0,len(list1),n)]
    
    maze1=to_matrix(maze3,10)
    return maze1



def main():
    global maze1
    global maze2
    global screen
    global PATH
    global blocksize
    maze2=loadMaze2(constants.input_file)
    maze1=loadMaze1(maze2)
    screen=initialize_game()
    game_loop(screen)


if __name__=="__main__":
    main()




