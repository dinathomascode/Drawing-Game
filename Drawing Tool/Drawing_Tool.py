# import libraries
import pygame, random

# initialize
pygame.init()
pygame.font.init()
pygame.display.init()

# window
window = pygame.display.set_mode((660,495), pygame.RESIZABLE)

# caption
pygame.display.set_caption("Drawing Game")

# icon
image = pygame.image.load('draw.png').convert_alpha()
pygame.display.set_icon(image)

# image
scaled_image = pygame.transform.scale(image,(72,72))
scaled_image_rect = image.get_rect()

# font size
font72 = pygame.font.Font(None,72)
font48 = pygame.font.Font(None,48)
font36 = pygame.font.Font(None,36)

# color
foreground = "white"
background = "black"

# spacing utilizing font36
textsize = 36

# text
# title
title = font72.render("Drawing Game",True,foreground,background)
title_rect = title.get_rect()
# controls
controls = font48.render("Controls",True,foreground,background)
controls_rect = controls.get_rect()
# draw
draw = font48.render("Draw",True,foreground,background)
draw_rect = draw.get_rect()
# lobby
lobby = font48.render("Lobby",True,foreground,background)
lobby_rect = lobby.get_rect()
# velocity
velocity = font48.render("Velocity",True,foreground,background)
velocity_rect = velocity.get_rect()
# instructions
move = font36.render("Use WASD and arrow keys.",True,foreground,background)
move_rect = move.get_rect()
move_rect.top = 0*textsize
follow = font36.render("Press spacebar to bring dot to cursor location.",True,foreground,background)
follow_rect = follow.get_rect()
follow_rect.top = 1*textsize
erase = font36.render("Press backspace or right click to erase.",True,foreground,background)
erase_rect = erase.get_rect()
erase_rect.top = 2*textsize
clear = font36.render("Press delete or mouse scroll to clear.",True,foreground,background)
clear_rect = clear.get_rect()
clear_rect.top = 3*textsize
change = font36.render("Left click or press enter to select a random color.",True,foreground,background)
change_rect = change.get_rect()
change_rect.top = 4*textsize
shift = font36.render("Press shift to set background.",True,foreground,background)
shift_rect = shift.get_rect()
shift_rect.top = 5*textsize
exit = font36.render("You may press CTRL and W keys simultaneously to exit.",True,foreground,background)
exit_rect = exit.get_rect()
exit_rect.top = 6*textsize
# speed
maxspeed = font48.render("Max Speed",True,foreground,background)
maxspeed_rect = maxspeed.get_rect()
sixty = font48.render("60",True,foreground,background)
sixty_rect = sixty.get_rect()
oneeighty = font48.render("180",True,foreground,background)
oneeighty_rect = oneeighty.get_rect()
sixhundred = font48.render("600",True,foreground,background)
sixhundred_rect = sixhundred.get_rect()
delta = font48.render("Delta",True,foreground,background)
delta_rect = delta.get_rect()

# values
fps = 60
radius = 6

def foyer():
    
    foreground = "white"
    background = "black"
    window.fill(background)
    switch = "none"
    global fps

    while True:
        
        # clock
        clock = pygame.time.Clock()

        # event handler
        input = pygame.key.get_pressed()
        for event in pygame.event.get():

            if (event.type == pygame.QUIT or ((input[pygame.K_RCTRL] or input[pygame.K_LCTRL]) and input[pygame.K_w])):
                pygame.display.quit()
                pygame.font.quit()
                pygame.quit()

        # initial screen     
        title = font72.render("Drawing Game",True,foreground,background)
        controls = font48.render("Controls",True,foreground,background)
        draw = font48.render("Draw",True,foreground,background)

        title_rect.center = (window.get_width()//2,window.get_height()//3)
        controls_rect.midtop = (window.get_width()//3,2*window.get_height()//3)
        draw_rect.midtop = (2*window.get_width()//3,2*window.get_height()//3)

        # interactions
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(5)

        left = (input[pygame.K_a] or input[pygame.K_LEFT]) and not (input[pygame.K_d] or input[pygame.K_RIGHT])
        right = (input[pygame.K_d] or input[pygame.K_RIGHT]) and not (input[pygame.K_a] or input[pygame.K_LEFT])
        
        if left or switch == "left" or controls_rect.collidepoint(cursor):
            controls = font48.render("Controls",True,background,foreground)
            draw = font48.render("Draw",True,foreground,background)
            if left: switch = "left"
        if right or switch == "right" or draw_rect.collidepoint(cursor):
            controls = font48.render("Controls",True,foreground,background)
            draw = font48.render("Draw",True,background,foreground)
            if right: switch = "right"
            
        if (switch == "left" or (controls_rect.collidepoint(cursor) and not draw_rect.collidepoint(cursor))) and (input[pygame.K_RETURN] or click[0]):
            instructions()
        if (switch == "right" or (draw_rect.collidepoint(cursor) and not controls_rect.collidepoint(cursor))) and (input[pygame.K_RETURN] or click[0]):
            game()

        # final screen
        window.blit(scaled_image,((title_rect.left)-72,(title_rect.centery)-36))
        window.blit(title,title_rect)
        window.blit(controls,controls_rect)
        window.blit(draw,draw_rect)

        # clock
        clock.tick(fps)

        # print screen
        pygame.display.flip()

def instructions():

    global foreground
    global background
    window.fill(background)
    switch = "none"
    previous_switch = "none"
    global fps

    while True:
        
        # clock
        clock = pygame.time.Clock()

        # event handler
        input = pygame.key.get_pressed()
        for event in pygame.event.get():

            if (event.type == pygame.QUIT or ((input[pygame.K_RCTRL] or input[pygame.K_LCTRL]) and input[pygame.K_w])):
                pygame.display.quit()
                pygame.font.quit()
                pygame.quit()

        # initial screen
        move = font36.render("Use WASD and arrow keys.",True,foreground,background)
        follow = font36.render("Press spacebar to bring dot to cursor location.",True,foreground,background)
        erase = font36.render("Press backspace or right click to erase.",True,foreground,background)
        clear = font36.render("Press delete or mouse scroll to clear.",True,foreground,background)
        change = font36.render("Left click or press enter to select a random color.",True,foreground,background)
        shift = font36.render("Press shift to set background.",True,foreground,background)
        exit = font36.render("You may press CTRL and W keys simultaneously to exit.",True,foreground,background)

        lobby = font48.render("Lobby",True,foreground,background)
        velocity = font48.render("Velocity",True,foreground,background)
        draw = font48.render("Draw",True,foreground,background)

        lobby_rect.bottomright = (window.get_width()//2-(draw_rect[2]//4),2*window.get_height()//3)
        velocity_rect.bottomleft = (window.get_width()//2+(draw_rect[2]//4),2*window.get_height()//3)
        draw_rect.midtop = (window.get_width()//2,(2*window.get_height()//3)+draw_rect[3]//2)

        # interactions
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(5)
        
        left = (input[pygame.K_a] or input[pygame.K_LEFT]) and not (input[pygame.K_d] or input[pygame.K_RIGHT])
        right = (input[pygame.K_d] or input[pygame.K_RIGHT]) and not (input[pygame.K_a] or input[pygame.K_LEFT])
        up = (input[pygame.K_w] or input[pygame.K_UP])  and not (input[pygame.K_s] or input[pygame.K_DOWN])
        down = (input[pygame.K_s] or input[pygame.K_DOWN]) and not (input[pygame.K_w] or input[pygame.K_UP])

        if (up and previous_switch == "lobby") or left: switch = "lobby"
        if (up and previous_switch == "velocity") or right: switch = "velocity"
        if down: switch = "draw"

        if switch == "lobby" or lobby_rect.collidepoint(cursor):
            lobby = font48.render("Lobby",True,background,foreground)
            velocity = font48.render("Velocity",True,foreground,background)
            draw = font48.render("Draw",True,foreground,background)
            previous_switch = "lobby"
        if switch == "velocity" or velocity_rect.collidepoint(cursor):
            lobby = font48.render("Lobby",True,foreground,background)
            velocity = font48.render("Velocity",True,background,foreground)
            draw = font48.render("Draw",True,foreground,background)
            previous_switch = "velocity"
        if switch == "draw" or draw_rect.collidepoint(cursor):
            Lobby = font48.render("Lobby",True,foreground,background)
            velocity = font48.render("Velocity",True,foreground,background)
            draw = font48.render("Draw",True,background,foreground)
        
        if ((switch == "lobby" or lobby_rect.collidepoint(cursor) and ((input[pygame.K_RETURN]) or click[0]))
            and ((switch != "none" and input[pygame.K_RETURN]) or click[0])):
            foyer()
        if (switch == "velocity" or velocity_rect.collidepoint(cursor)) and ((switch != "none" and input[pygame.K_RETURN]) or click[0]):
            speed()
        if (switch == "draw" or draw_rect.collidepoint(cursor)) and (input[pygame.K_RETURN] or click[0]):
            game()

        # final screen
        window.blit(move,move_rect)
        window.blit(follow,follow_rect)
        window.blit(erase,erase_rect)
        window.blit(clear,clear_rect)
        window.blit(change,change_rect)
        window.blit(shift,shift_rect)
        window.blit(exit,exit_rect)
        
        window.blit(lobby,lobby_rect)
        window.blit(velocity,velocity_rect)
        window.blit(draw,draw_rect)
        
        # clock
        clock.tick(fps)

        # print screen
        pygame.display.flip()

def speed():
    
    global foreground
    global background
    window.fill(background)
    d = "none"
    switch = "none"
    global fps

    while True:
        
        # clock
        clock = pygame.time.Clock()

        # event handler
        input = pygame.key.get_pressed()
        for event in pygame.event.get():

            if (event.type == pygame.QUIT or ((input[pygame.K_RCTRL] or input[pygame.K_LCTRL]) and input[pygame.K_w])):
                pygame.display.quit()
                pygame.font.quit()
                pygame.quit()
        
        # intial screen
        maxspeed = font48.render("Max Speed",True,foreground,background)
        sixty = font48.render("60",True,foreground,background)
        oneeighty = font48.render("180",True,foreground,background)
        sixhundred = font48.render("600",True,foreground,background)
        delta = font48.render(d,True,foreground,background)

        maxspeed_rect.center = (window.get_width()//2,window.get_height()//2-maxspeed_rect[2]//2)
        sixty_rect.center = (window.get_width()//2+(maxspeed_rect[2]//2),window.get_height()//2)
        oneeighty_rect.center = (window.get_width()//2,window.get_height()//2+maxspeed_rect[2]//2)
        sixhundred_rect.center = (window.get_width()//2-(maxspeed_rect[2]//2),window.get_height()//2)
        delta_rect.center = (window.get_width(),window.get_height())
        
        # interactions
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(5)

        left = (input[pygame.K_a] or input[pygame.K_LEFT]) and not (input[pygame.K_d] or input[pygame.K_RIGHT])
        right = (input[pygame.K_d] or input[pygame.K_RIGHT]) and not (input[pygame.K_a] or input[pygame.K_LEFT])
        up = (input[pygame.K_w] or input[pygame.K_UP])  and not (input[pygame.K_s] or input[pygame.K_DOWN])
        down = (input[pygame.K_s] or input[pygame.K_DOWN]) and not (input[pygame.K_w] or input[pygame.K_UP])

        if up: switch = "maxspeed"
        if down: switch = "180"
        if left: switch = "600"
        if right: switch = "60"
        
        if switch == "maxspeed" or maxspeed_rect.collidepoint(cursor):
            maxspeed = font48.render("Max Speed",True,background,foreground)
            sixty = font48.render("60",True,foreground,background)
            oneeighty = font48.render("180",True,foreground,background)
            sixhundred = font48.render("600",True,foreground,background)
        if switch == "60" or sixty_rect.collidepoint(cursor):
            maxspeed = font48.render("Max Speed",True,foreground,background)
            sixty = font48.render("60",True,background,foreground)
            oneeighty = font48.render("180",True,foreground,background)
            sixhundred = font48.render("600",True,foreground,background)
        if switch == "180" or oneeighty_rect.collidepoint(cursor):
            maxspeed = font48.render("Max Speed",True,foreground,background)
            sixty = font48.render("60",True,foreground,background)
            oneeighty = font48.render("180",True,background,foreground)
            sixhundred = font48.render("600",True,foreground,background)
        if switch == "600" or sixhundred_rect.collidepoint(cursor):
            maxspeed = font48.render("Max Speed",True,foreground,background)
            sixty = font48.render("60",True,foreground,background)
            oneeighty = font48.render("180",True,foreground,background)
            sixhundred = font48.render("600",True,background,foreground)
        
        if (switch == "maxspeed" or maxspeed_rect.collidepoint(cursor)) and (input[pygame.K_RETURN] or click[0]):
            fps = pygame.time.Clock.get_fps(clock)
            instructions()
        if (switch == "60" or sixty_rect.collidepoint(cursor)) and (input[pygame.K_RETURN] or click[0]):
            fps = 60
            instructions()
        if (switch == "180" or oneeighty_rect.collidepoint(cursor)) and (input[pygame.K_RETURN] or click[0]):
            fps = 180
            instructions()
        if (switch == "600" or sixhundred_rect.collidepoint(cursor)) and (input[pygame.K_RETURN] or click[0]):
            fps = 600
            instructions()
        
        # final screen
        window.blit(maxspeed,maxspeed_rect)
        window.blit(sixty,sixty_rect)
        window.blit(oneeighty,oneeighty_rect)
        window.blit(sixhundred,sixhundred_rect)
        
        # clock
        clock.tick(fps)

        # print screen
        pygame.display.flip()

def game():

    global foreground
    global background
    window.fill(background)
    dot = pygame.rect.Rect((window.get_width()//2),(window.get_height()//2),radius,radius)
    dotx, doty = dot.center
    global fps

    while True:
        
        # clock
        clock = pygame.time.Clock()

        # event handler
        input = pygame.key.get_pressed()
        for event in pygame.event.get():

            if (event.type == pygame.QUIT or ((input[pygame.K_RCTRL] or input[pygame.K_LCTRL]) and input[pygame.K_w])):
                pygame.display.quit()
                pygame.font.quit()
                pygame.quit()

        # interactions
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(5)

        if (input[pygame.K_a] or input[pygame.K_LEFT]) and dotx > 0:
            dotx -= 1
        if (input[pygame.K_d] or input[pygame.K_RIGHT]) and dotx < window.get_width():
            dotx += 1
        if (input[pygame.K_w] or input[pygame.K_UP]) and doty > 0:
            doty -= 1
        if (input[pygame.K_s] or input[pygame.K_DOWN]) and doty < window.get_height():
            doty += 1
        if input[pygame.K_SPACE]:
            if dotx < cursor[0]:
                dotx += 1
            if dotx > cursor[0]:
                dotx -= 1
            if doty < cursor[1]:
                doty += 1
            if doty > cursor[1]:
                doty -= 1
        if click[2] or input[pygame.K_BACKSPACE]:
            foreground = background
        if click[1] or input[pygame.K_SCROLLOCK] or input[pygame.MOUSEWHEEL] or input[pygame.K_DELETE]:
            window.fill(background)
        if click[0] or input[pygame.K_RETURN]:
            foreground = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        if input[pygame.K_LSHIFT] or input[pygame.K_RSHIFT]:
            background = foreground
            window.fill(background)
        
        # final screen
        pygame.draw.circle(window,foreground,(dotx,doty),radius)        
        
        controls = font48.render("Controls",True,foreground,background)
        controls_rect.topleft = (0,0)
        if controls_rect.collidepoint(cursor):
            controls = font48.render("Controls",True,background,foreground)
            if click[0]:
                instructions()
        window.blit(controls,controls_rect)
        
        # clock
        clock.tick(fps)

        # print screen
        pygame.display.flip()

while True:
    foyer()