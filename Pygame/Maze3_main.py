import pygame,sys
import constants3
from python_settings import settings

output=[]
PATH = [(1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (5, 2), (6, 2), (6, 1), (7, 1), (8, 1), (8, 2), (9, 2), (10, 2), (10, 1), (11, 1), (12, 1), (13, 1), (13, 2), (14, 2), (15, 2), (15, 1), (15, 1), (15, 2), (14, 2), (13, 2), (13, 1), (12, 1), (11, 1), (10, 1), (10, 2), (9, 2), (8, 2), (8, 3), (7, 3), (7, 4), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8), (7, 8), (6, 8), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (9, 5), (10, 5), (10, 4), (11, 4), (12, 4), (13, 4), (13, 5), (13, 6), (13, 7), (13, 8), (12, 8), (11, 8), (11, 9), (11, 10), (11, 11), (10, 11), (9, 11), (9, 12), (9, 13), (10, 13), (10, 14), (11, 14), (12, 14), (12, 13), (12, 12), (13, 12), (13, 11), (13, 10), (14, 10), (15, 10), (15, 11), (15, 11), (15, 10), (14, 10), (13, 10), (13, 11), (13, 12), (12, 12), (12, 13), (12, 14), (11, 14), (10, 14), (10, 13), (9, 13), (9, 12), (9, 11), (10, 11), (11, 11), (11, 10), (11, 9), (11, 8), (12, 8), (13, 8), (13, 7), (13, 6), (13, 5), (13, 4), (12, 4), (11, 4), (10, 4), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (4, 6), (4, 7), (3, 7), (2, 7), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (2, 13), (2, 14), (1, 14), (1, 15), (1, 16), (2, 16), (3, 16), (3, 15), (4, 15), (3, 15), (3, 16), (2, 16), (1, 16), (1, 15), (1, 14), (2, 14), (2, 13), (2, 12), (1, 12), (1, 11), (1, 10), (1, 9), (2, 9), (3, 9), (3, 10), (3, 11), (4, 11), (5, 11), (5, 12), (6, 12), (7, 12), (7, 13), (7, 14), (7, 15), (8, 15), (9, 15), (9, 16), (10, 16), (11, 16), (12, 16), (13, 16), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13), (14, 13), (14, 13), (15, 13), (15, 14), (15, 15), (14, 15), (13, 15), (13, 16), (12, 16), (11, 16), (10, 16), (9, 16), (9, 15), (8, 15), (7, 15), (7, 14), (7, 13), (7, 12), (6, 12), (5, 12), (5, 11), (4, 11), (3, 11), (3, 10), (3, 9), (2, 9), (1, 9), (1, 10), (1, 11), (1, 12), (2, 12), (2, 13), (2, 14), (1, 14), (1, 15), (1, 16), (2, 16), (3, 16), (3, 15), (4, 15), (5, 15), (5, 16)]
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
                ydoor_image=pygame.image.load('yellow_door.png')
                def ydoor_img():
                    screen.blit(ydoor_image,(x,y))
                ydoor_img()
            elif maze1[i][j]== 'a':
                ykey_image=pygame.image.load('yellow_key.png')
                def ykey_img():
                    screen.blit(ykey_image,(x,y))
                ykey_img()
            elif maze1[i][j]== 'c':
                gdoor_image=pygame.image.load('green_door.png')
                def gdoor_img():
                    screen.blit(gdoor_image,(x,y))
                gdoor_img()
            elif maze1[i][j]== 'd':
                gkey_image=pygame.image.load('green_key.png')
                def gkey_img():
                    screen.blit(gkey_image,(x,y))
                gkey_img()
            elif maze1[i][j]== 'g':
                rdoor_image=pygame.image.load('red_door.png')
                def rdoor_img():
                    screen.blit(rdoor_image,(x,y))
                rdoor_img()
            elif maze1[i][j]== 'f':
                rkey_image=pygame.image.load('red_key.png')
                def rkey_img():
                    screen.blit(rkey_image,(x,y))
                rkey_img()
            elif maze1[i][j]== 'i':
                bdoor_image=pygame.image.load('blue_door.png')
                def bdoor_img():
                    screen.blit(bdoor_image,(x,y))
                bdoor_img()
            elif maze1[i][j]== 'h':
                bkey_image=pygame.image.load('blue_key.png')
                def bkey_img():
                    screen.blit(bkey_image,(x,y))
                bkey_img()
            else:
                break
            x+=53

        y+=53



def draw_grid(screen):
    for i in range(constants3.column):
        new_height= round(i * constants3.block_height)
        new_width= round(i * constants3.block_width)
        pygame.draw.line(screen, constants3.background, (0, new_height), (constants3.screen_width, new_height), 2)
        pygame.draw.line(screen, constants3.background, (new_width,0), (new_width, constants3.screen_height), 2)

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
    screen = pygame.display.set_mode((constants3.screen_width, constants3.screen_height))
    pygame.display.set_caption(constants3.title)
    icon = pygame.image.load('game.png')
    pygame.display.set_icon(icon)
    screen.fill(constants3.background)
    return screen

def loadMaze2(input_file3):
    #load the data from the file into a 2D list
    with open(input_file3) as i:
        maze2 = []
        for line in i:
            line = line.split()
            maze2.append(line)
            #print(line)
    return maze2

def loadMaze1(input_file3):
    maze3=[]
    l=len(input_file3)
    ln=len(input_file3[0])
    for i in range(0,l):
        for j in range(0,ln):
            if input_file3[i][j]== "1" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "0" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "s" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "e" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "a" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "b" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "c" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "d" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "f" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "g" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "h" :
                maze3.append(input_file3[i][j])
            elif input_file3[i][j]== "i" :
                maze3.append(input_file3[i][j])
            else:
                continue
    def to_matrix(list1, n):
        return [list1[i:i+n] for i in range(0,len(list1),n)]
    
    maze1=to_matrix(maze3,18)
    return maze1



def main():
    global maze1
    global maze2
    global screen
    maze2=loadMaze2(constants3.input_file3)
    maze1=loadMaze1(maze2)
    screen=initialize_game()
    game_loop(screen)


if __name__=="__main__":
    main()






