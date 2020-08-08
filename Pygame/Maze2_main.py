import pygame,sys
import constants
from python_settings import settings

output=[]
PATH = [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (3, 3), (2, 3), (2, 4), (2, 5), (1, 5), (2, 5), (2, 4), (2, 3), (3, 3), (4, 3), (4, 2), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (8, 2), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 7)]
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
            elif maze1[i][j]== 'b':
                door_image=pygame.image.load('yellow_door.png')
                def door_img():
                    screen.blit(door_image,(x,y))
                door_img()
            elif maze1[i][j]== 'a':
                key_image=pygame.image.load('yellow_key.png')
                def key_img():
                    screen.blit(key_image,(x,y))
                key_img()
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
    running= True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    sys.exit()
        
        add_image(maze1)
        draw_grid(screen)
        pygame.display.update()

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
    pygame.display.set_caption(constants.title)
    icon = pygame.image.load('game.png')
    pygame.display.set_icon(icon)
    screen.fill(constants.background)
    return screen

def loadMaze2(input_file2):
    #load the data from the file into a 2D list
    with open(input_file2) as i:
        maze2 = []
        for line in i:
            line = line.split()
            maze2.append(line)
            #print(line)
    return maze2

def loadMaze1(input_file2):
    maze3=[]
    l=len(input_file2)
    ln=len(input_file2[0])
    for i in range(0,l):
        for j in range(0,ln):
            if input_file2[i][j]== "1" :
                maze3.append(input_file2[i][j])
            elif input_file2[i][j]== "0" :
                maze3.append(input_file2[i][j])
            elif input_file2[i][j]== "s" :
                maze3.append(input_file2[i][j])
            elif input_file2[i][j]== "e" :
                maze3.append(input_file2[i][j])
            elif input_file2[i][j]== "a" :
                maze3.append(input_file2[i][j])
            elif input_file2[i][j]== "b" :
                maze3.append(input_file2[i][j])
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
    maze2=loadMaze2(constants.input_file2)
    maze1=loadMaze1(maze2)
    screen=initialize_game()
    game_loop(screen)


if __name__=="__main__":
    main()





