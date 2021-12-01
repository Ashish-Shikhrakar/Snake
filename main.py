import pygame, sys, random

def snake_char(): #the main snake
    global get_position, snake_back
    if direction == "left":
        snake_front = pygame.image.load("assets/snake_left.png").convert()
    if direction == "right":
        snake_front = pygame.image.load("assets/snake_right.png").convert()
    if direction == "down":
        snake_front = pygame.image.load("assets/snake_down.png").convert()
    if direction == "up":
        snake_front = pygame.image.load("assets/snake_up.png").convert()
    
    snake_front_rect = snake_front.get_rect(center = (snake_x_pos,snake_fy_pos))
    snake_back = pygame.image.load("assets/snake_back.png").convert()
    snake_back_rect = snake_back.get_rect(center = (snake_x_pos + snake_back_x_tracker,snake_by_pos + snake_back_y_tracker))
    # get_position = snake_back.get_rect(center = (snake_x_pos + (snake_back_x_tracker)*2,snake_by_pos + (snake_back_y_tracker)*2))
    screen.blit(snake_front,snake_front_rect)
    screen.blit(snake_back,snake_back_rect)
    # screen.blit(snake_back,get_position)

    return snake_back_rect,snake_front_rect

def food(snake_food):#food for snake
    global count, score, food_item_rect
    food_item = pygame.image.load("assets/food.png").convert()

    for tracker in snake_food:
        if  count== 1:
            random_spawn1 = random.choice(range_food_spawn)
            random_spawn2 = random.choice(range_food_spawn)
            food_item_rect = food_item.get_rect(center = (random_spawn1,random_spawn2))
            count= 0

        if food_item_rect.colliderect(tracker):
            score = score +1
            count = 1
        # snake_length_add(snake_food,score)
        screen.blit(food_item,food_item_rect)
            

# def snake_length_add(snake_rectangles,score):
#     snake_length = [1]
#     for i in snake_length:
#         get_position[0] = get_position[0] * 2
#         screen.blit(snake_back,get_position)


        

pygame.init()
screen = pygame.display.set_mode((700,700)) #main screen
clock = pygame.time.Clock() #for screen refresh rate

#game variables
range_food_spawn = range(1,700,1)
count = 1
score = 0
snake_x_pos = 328
snake_fy_pos = 328
snake_by_pos = 328
snake_back_x_tracker = 44
snake_back_y_tracker = 0
direction = "left"


bg_surface = pygame.image.load("assets/image.png").convert()
snake_rectangles = []



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if direction!="right" and event.key == pygame.K_a: #move left set direction
                snake_back_x_tracker = 44
                if direction == "up":
                    snake_back_y_tracker-=44
                if direction =="down":
                    snake_back_y_tracker+=44
                direction = "left"

            if direction!="down" and event.key == pygame.K_w: #move up set direction
                if direction == "left":
                    snake_back_x_tracker-=44
                if direction == "right":
                    snake_back_x_tracker+=44
                snake_back_y_tracker = 0
                snake_by_pos = snake_fy_pos+44
                direction = "up"

            if direction!="up" and event.key == pygame.K_s: #move down set direction
                if direction == "left":
                    snake_back_x_tracker-=44
                if direction == "right":
                    snake_back_x_tracker+=44
                snake_back_y_tracker = 0
                snake_by_pos = snake_fy_pos-44
                direction = "down"

            if direction!="left" and event.key == pygame.K_d: #move right set direction
                snake_back_x_tracker = -44
                if direction == "up":
                    snake_back_y_tracker-=44
                if direction =="down":
                    snake_back_y_tracker+=44
                direction = "right"


    screen.blit(bg_surface,(0,0))

    
    #animate snake movement

    if direction=="left":
        snake_x_pos-=1
    elif direction=="up":
        snake_fy_pos-=1
        snake_by_pos = snake_fy_pos+44
    elif direction=="down":
        snake_fy_pos+=1
        snake_by_pos = snake_fy_pos-44
    else:
        snake_x_pos+=1

    snake_rectangles.extend(snake_char())
    food(snake_rectangles)

    pygame.display.update()
    clock.tick(144) #controlling screen refresh rate