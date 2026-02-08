from collections import deque
import pygame
import time
import random
# инициализируем библиотеку Pygame
pygame.init()

class ClickableSprite(pygame.sprite.Sprite):
    def update(self):
        pass
# определяем размеры окна
window_size = (1200, 800)

# задаем название окна
pygame.display.set_caption("Синий фон")

# создаем окно
screen = pygame.display.set_mode(window_size)

# задаем цвет фона
background_color = (200, 200, 200)  # синий

# заполняем фон заданным цветом
screen.fill(background_color)
cam1 = pygame.image.load('1.png')
cam1 = pygame.transform.scale(cam1, (1200, 800))

cam2 = pygame.image.load('2.png')
cam2 = pygame.transform.scale(cam2, (1200, 800))

cam3 = pygame.image.load('3.png')
cam3 = pygame.transform.scale(cam3, (1200, 800))

cam4 = pygame.image.load('4.png')
cam4 = pygame.transform.scale(cam4, (1200, 800))

cam5 = pygame.image.load('5.png')
cam5 = pygame.transform.scale(cam5, (1200, 800))

office_open = pygame.image.load('office_open.png')
office_open = pygame.transform.scale(office_open, (1200, 800))

office = pygame.image.load('office.png')
office = pygame.transform.scale(office, (1200, 800))

quest = pygame.image.load('quest.png')
quest = pygame.transform.scale(quest, (1200, 800))

vent = pygame.image.load('vent.png')
vent = pygame.transform.scale(vent, (1200, 800))

roman = pygame.image.load('roman.png')
roman_screamer = pygame.transform.scale(roman, (350, 700))
roman_smol = pygame.transform.scale(roman, (40, 80))
roman = pygame.transform.scale(roman, (80, 150))
roman_mid = pygame.transform.scale(roman, (120, 240))
roman_big = pygame.transform.scale(roman, (200, 400))
roman_office = pygame.transform.scale(roman, (259, 500))
# обновляем экран для отображения изменений
win = 'win'
graph = {'1' : ('2'), \
         '2' : (win), \
        '3' : ('4', '5'), \
        '4' : ('2'), \
        '5' : ('2')}
ur_ded = False
door = True
mpos = pygame.mouse.get_pos
chance_to_move = 0.5
in_office = True
in_quest = False
in_vent = False
in_cams = False
player_look = '2'
goal = 100
current_press = '1'
last_press = '2'
pressed = '0'
mini_romans = []
current_time = time.time()
dec = random.random()
time_for_minis = time.time()
font = pygame.font.Font('freesansbold.ttf', 32)
quest_press = '100'
roman_move_time = 15
roman_ttk_time = time.time()
roman_ttk = 6
roman_win = False

def bfs(graph, start):
    global door
    where_to_go = []
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        if vertex == win:
            break
        if graph[vertex] == win:
            if graph[vertex] not in visited:
                visited.add(graph[vertex])
                where_to_go.append(graph[vertex])
                queue.append(graph[vertex])
            continue
        print(where_to_go)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                where_to_go.append(neighbor)
                queue.append(neighbor)
    print('роман в комнате', where_to_go[0],  '\n')
    # if where_to_go[0] == 'target':
    #     return 'target'
    return where_to_go[0]
def roll_quest():
    global current_press
    global last_press
    rand = random.random()
    if rand <= 0.25:
        current_press = '1'
    if rand <= 0.50 and rand > 0.25:
        current_press = '2'
    if rand <= 0.75 and rand > 0.5:
        current_press = '3'
    if rand <= 1 and rand > 0.75:
        current_press = '4' 
    while current_press == last_press:
        rand = random.random()
        if rand <= 0.25:
            current_press = '1'
        if rand <= 0.50 and rand > 0.25:
            current_press = '2'
        if rand <= 0.75 and rand > 0.5:
            current_press = '3'
        if rand <= 1 and rand > 0.75:
            current_press = '4'  
                     

def draw_rect(x, y, w, h):
    pygame.draw.rect(screen, (100, 100, 100), [x, y, w, h])
def draw_active(x, y, w, h):
    pygame.draw.rect(screen, (0, 255, 0), [x, y, w, h])
def draw_inactive(x, y, w, h):
    pygame.draw.rect(screen, (255, 0, 0), [x, y, w, h])
# показываем окно, пока пользователь не нажмет кнопку "Закрыть"

def dif_check():
    global roman_move_time, quest_press, roman_ttk
    if int(quest_press) < 101 and int(quest_press) > 75:
        roman_move_time = 15
        roman_ttk = 6
    if int(quest_press) < 76 and int(quest_press) > 50:
        roman_move_time = 10
        roman_ttk = 5
    if int(quest_press) < 51 and int(quest_press) > 25:
        roman_move_time = 6
        roman_ttk = 4
    if int(quest_press) < 26 and int(quest_press) > 0:
        roman_move_time = 3
        roman_ttk = 3
def office_closed():
    return mpos()[0] < 700 and mpos()[0] > 500 and\
            mpos()[1] < 700 and mpos()[1] > 100 and\
            pygame.mouse.get_pressed()[0]
if dec <= 0.5:
    current_room = '3'
if dec >= 0.5:
    current_room = '1'

text = font.render(quest_press, True, False, False)
textRect = text.get_rect()
textRect.center = (1100, 50)
while not ur_ded:
    if quest_press < 1:
        pygame.quit()
        exit()
    if time.time() - time_for_minis > 7:
        if 1 not in mini_romans:
            mini_romans.append(1)
        elif 2 not in mini_romans:
            mini_romans.append(2)
        elif 3 not in mini_romans:
            mini_romans.append(3)
        elif 4 not in mini_romans:
            mini_romans.append(4)
        elif 5 not in mini_romans:
            mini_romans.append(5)   
        elif 1 in mini_romans and \
            2 in mini_romans and \
            3 in mini_romans and \
            4 in mini_romans and \
            5 in mini_romans: # 120 240
            screen.blit(roman_mid, (260, 280))
            screen.blit(roman_mid, (380, 280))
            screen.blit(roman_mid, (520, 280))
            screen.blit(roman_mid, (660, 280))
            screen.blit(roman_mid, (800, 280))
            pygame.display.flip()
            time.sleep(2)
            exit()
        time_for_minis = time.time()

    if time.time() - current_time > roman_move_time:
            dif_check()
        # print(current_room, '////////////////////////')
        # if current_room == win:
        #     if not office_closed():
        #         screen.blit(roman_screamer, (425, 50))
        #         pygame.display.flip()
        #         time.sleep(2)
        #         exit()
        #     dec = random.random()
        #     if dec <= 0.5:
        #         current_room = '3'
        #     if dec >= 0.5:
        #         current_room = '1'
            # print(current_room, '|||||||||||||||||||||||||')
            # current_time = time.time()
        # else:
            current_time = time.time()
            if random.random() < chance_to_move:
                chance_to_move = 0.5
                # print(current_room, '|||||||||||||||||||||')
                current_room = bfs(graph, current_room)
                # print(current_room, '---------------')
                if current_room == '2':
                    roman_move_time = roman_ttk
                    chance_to_move = 1
                if current_room == win and office_closed():
                    dec = random.random()
                    if dec <= 0.5:
                        current_room = '3'
                    if dec >= 0.5:
                        current_room = '1'
                elif current_room == win:
                    screen.blit(roman_screamer, (425, 50))
                    pygame.display.flip()
                    time.sleep(2)
                    exit()
            # print(current_room, '---------------------------')
        


    # if current_room == '2':
    #     screen.blit(cam2, (0, 0))

    # if current_room == '3':
    #     screen.blit(cam3, (0, 0))

    # if current_room == '4':
    #     screen.blit(cam4, (0, 0))

    # if current_room == '5':
    #     screen.blit(cam5, (0, 0))
    draw_rect(0, 0, 1200, 800)

    if in_office:
        if current_room == '2':
            screen.blit(roman_office, (445, 70))
        if mpos()[0] < 700 and mpos()[0] > 500 and\
            mpos()[1] < 700 and mpos()[1] > 100 and\
            pygame.mouse.get_pressed()[0]:
            screen.blit(office, (0, 0))
        else:
            screen.blit(office_open, (0, 0))
        draw_rect(75, 100, 50, 600)
        draw_rect(1075, 100, 50, 600)

    if in_quest:
        screen.blit(quest, (0, 0))

        draw_rect(500, 300, 200, 200)
        if current_press == '1':
            draw_active(525, 325, 25, 25)
            if pressed == '1':
                last_press = '1'     
                pressed = '0'  
                quest_press = int(quest_press)
                quest_press -= 1  
                quest_press = str(quest_press)
                dif_check()
                roll_quest()   
        else:
            draw_inactive(525, 325, 25, 25)
        if current_press == '2':
            draw_active(650, 325, 25, 25)
            if pressed == '2':
                last_press = '2'        
                pressed = '0' 
                quest_press = int(quest_press)
                quest_press -= 1  
                quest_press = str(quest_press)   
                dif_check()
                roll_quest()                                   
        else:
            draw_inactive(650, 325, 25, 25)
        if current_press == '3':
            draw_active(525, 450, 25, 25)
            if pressed == '3':
                last_press = '3'   
                pressed = '0'  
                quest_press = int(quest_press)
                quest_press -= 1  
                quest_press = str(quest_press) 
                dif_check()
                roll_quest()       
        else:
            draw_inactive(525, 450, 25, 25)
        if current_press == '4':
            draw_active(650, 450, 25, 25)
            if pressed == '4':
                last_press = '4'
                pressed = '0'
                quest_press = int(quest_press)
                quest_press -= 1  
                quest_press = str(quest_press)
                dif_check()
                roll_quest()
        else:
            draw_inactive(650, 450, 25, 25)                                    
            
        draw_rect(1075, 100, 50, 600)

    if in_vent:
        screen.blit(vent, (0, 0))
        if 1 in mini_romans:
            screen.blit(roman_smol, (510, 520))
        if 2 in mini_romans:
            screen.blit(roman_smol, (585, 580))
        if 3 in mini_romans:
            screen.blit(roman_smol, (455, 440))
        if 4 in mini_romans:
            screen.blit(roman_smol, (650, 490))
        if 5 in mini_romans:
            screen.blit(roman_smol, (350, 550))
        draw_rect(75, 100, 50, 600)


    if in_cams:
        if player_look == '1':
            screen.blit(cam1, (0, 0))
            if current_room == '1':
                screen.blit(roman, (400, 400))

        if player_look == '2':
            screen.blit(cam2, (0, 0))
            if current_room == '2':
                screen.blit(roman, (550, 300))

        if player_look == '3':
            screen.blit(cam3, (0, 0))
            if current_room == '3':
                screen.blit(roman, (900, 250))

        if player_look == '4':
            screen.blit(cam4, (0, 0))
            if current_room == '4':
                screen.blit(roman_big, (500, 300))

        if player_look == '5':
            screen.blit(cam5, (0, 0))
            if current_room == '5':
                screen.blit(roman_mid, (230, 260))

        draw_rect(25, 25, 50, 50)
        draw_rect(85, 25, 50, 50)
        draw_rect(25, 85, 50, 50)
        draw_rect(85, 85, 50, 50)
        draw_rect(145, 25, 50, 50)

    draw_rect(200, 725, 800, 50)

    text = font.render(quest_press, True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1100, 50)
    screen.blit(text, textRect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 75 and event.pos[0] < 125 and \
            event.pos[1] > 100 and event.pos[1] < 700 and in_office:
                in_office = False
                in_quest = True
            if event.pos[0] > 1075 and event.pos[0] < 1175 and \
            event.pos[1] > 100 and event.pos[1] < 700 and in_office:
                in_office = False
                in_vent = True      
            if event.pos[0] > 75 and event.pos[0] < 125 and \
            event.pos[1] > 100 and event.pos[1] < 700 and in_vent:
                in_vent = False
                in_office = True   
            if event.pos[0] > 1075 and event.pos[0] < 1175 and \
            event.pos[1] > 100 and event.pos[1] < 700 and in_quest:
                in_quest = False
                in_office = True                        
            if event.pos[0] > 25 and event.pos[0] < 75\
            and event.pos[1] > 25 and event.pos[1] < 75:
                player_look = '1'
                
            if event.pos[0] > 85 and event.pos[0] < 135\
            and event.pos[1] > 25 and event.pos[1] < 75:
                player_look = '2'

            if event.pos[0] > 25 and event.pos[0] < 75\
            and event.pos[1] > 85 and event.pos[1] < 135:
                player_look = '3'

            if event.pos[0] > 85 and event.pos[0] < 135\
            and event.pos[1] > 85 and event.pos[1] < 135:
                player_look = '4'

            if event.pos[0] > 145 and event.pos[0] < 195\
            and event.pos[1] > 25 and event.pos[1] < 75:
                player_look = '5'
            
            if event.pos[0] > 200 and event.pos[0] < 1000\
            and event.pos[1] > 725 and event.pos[1] < 775:
                if in_cams:
                    in_cams = False
                else:
                    in_cams = True

            if event.pos[0] > 525 and event.pos[0] < 550\
            and event.pos[1] > 325 and event.pos[1] < 350:
                pressed = '1'
                print(1)
            if event.pos[0] > 650 and event.pos[0] < 675\
            and event.pos[1] > 325 and event.pos[1] < 350:
                pressed = '2'
                print(2)
            if event.pos[0] > 525 and event.pos[0] < 550\
            and event.pos[1] > 450 and event.pos[1] < 475:
                pressed = '3'
                print(3)
            if event.pos[0] > 650 and event.pos[0] < 675\
            and event.pos[1] > 450 and event.pos[1] < 475:
                pressed = '4'   
                print(4)

            if event.pos[0] > 510 and event.pos[0] < 550\
            and event.pos[1] > 520 and event.pos[1] < 600 and in_vent:  
                mini_romans.remove(1)
            if event.pos[0] > 585 and event.pos[0] < 625\
            and event.pos[1] > 580 and event.pos[1] < 660 and in_vent:  
                mini_romans.remove(2)
            if event.pos[0] > 455 and event.pos[0] < 495\
            and event.pos[1] > 440 and event.pos[1] < 520 and in_vent:  
                mini_romans.remove(3)
            if event.pos[0] > 650 and event.pos[0] < 690\
            and event.pos[1] > 490 and event.pos[1] < 570 and in_vent:  
                mini_romans.remove(4)
            if event.pos[0] > 350 and event.pos[0] < 390\
            and event.pos[1] > 550 and event.pos[1] < 630 and in_vent:  
                mini_romans.remove(5)                                                                
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
