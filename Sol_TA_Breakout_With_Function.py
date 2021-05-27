import pygame #The library used to make games in python
pygame.init()#It initializes all imported pygame modules
 
WHITE = (255,255,255)#Hex code for white color
DARKBLUE = (36,90,190)#Hex code for darkblue color
LIGHTBLUE = (0,176,240)#Hex code for lightblue color
RED = (255,0,0)#Hex code for red color

bricks1=[pygame.Rect(10 + i* 100,60,80,30) for i in range(6)]#A method to decide where to place the brick i.e 4 bricks using list comprehension
bricks2=[pygame.Rect(10 + i* 100,100,80,30) for i in range(6)]#A method to decide where to place the brick i.e 4 bricks using list comprehension
bricks3=[pygame.Rect(10 + i* 100,140,80,30) for i in range(6)]#A method to decide where to place the brick i.e 4 bricks using list comprehension

def draw_brick(brick_list):#Drawing the brick using a function
    for i in brick_list:#Passing the bricks as a list in the for loop
        pygame.draw.rect(screen,RED,i)#A method to draw rectangle in pygame

score = 0#Initialize score variable

velocity=[1,1]#Initialize the speed vector
size = (600, 600)#Variable for setting the screen size
screen = pygame.display.set_mode(size)#Setting the screen size
pygame.display.set_caption("Breakout Game")#Title on the screen
paddle=pygame.Rect(300,550,60,10) #paddle dimensions(x,y,width,height)
ball=pygame.Rect(200,250,10,10)#ball dimensions
carryOn = True#A flag variable for while loop
while carryOn:#Used just like (while True:) loop
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)#Screen color placed here so that even when the ball hits the bricks and comes back the color of the screen should not change
    pygame.draw.rect(screen,LIGHTBLUE,paddle)#Rectangle for paddle
    font = pygame.font.Font(None, 34)#font for score
    text = font.render("Score: " + str(score), 1, WHITE)#Display the text of score
    screen.blit(text, (20,10))#To show the written block of text on the screen
    #paddle movement
    if event.type == pygame.KEYDOWN:#If any key is pressed
        if event.key == pygame.K_RIGHT:#If right arrow key is pressed
            if paddle.x<540:#Checking the movement of paddle according to the position of paddle on the screen. 540 is the maximum position to which paddle can move
                paddle.x+=5#Increase the x co-ordinate by 5 pixels
        if event.key == pygame.K_LEFT:#If left arrow key is pressed
            if paddle.x>0:#Checking the movement of paddle according to the position of paddle on the screen. 0 is the min position to which the paddle can move
                paddle.x-=5#Decrease the x co-ordinate by 5 pixels 
    # brick wall   
    draw_brick(bricks1)#Call the function for drawing the bricks1
    draw_brick(bricks2)#Call the function for drawing the bricks2
    draw_brick(bricks3)#Call the function for drawing the bricks3

    #ball movement    
    ball.x+=velocity[0]#Changing the ball's x position by adding a value through velocity 0th element i.e 1
    ball.y+=velocity[1]#Changing the ball's y position by adding a value through velocity 0th element i.e 1  
    
    if ball.x>=590 or ball.x<=0:#Check for maximum and minimum pixels
        velocity[0] = -velocity[0]#Making the velocity negative
    if ball.y<=3:#Check for ball's y co-ordinate
        velocity[1] = -velocity[1]#Making the velocity negative
    if paddle.collidepoint(ball.x,ball.y):#Check for collision
         velocity[1]=-velocity[1]#Making the velocity negative
    if ball.y>=590:#Check for y co-ordinate max pixel
        font = pygame.font.Font(None, 74)#Using font for the text
        text = font.render("GAME OVER", 1, RED)#Showing the text and using color to display the text
        screen.blit(text, (150,350))#Showing the text on the screen
        pygame.display.flip()#Updating the display on the screen
        pygame.time.wait(2000)#Wait
        break#loop exit
    pygame.draw.rect(screen,WHITE ,ball)#Draw the ball
    #score
    for i in bricks1:
        if i.collidepoint(ball.x,ball.y):#if the ball touches bricks1
            bricks1.remove(i)#Remove the brick
            velocity[0] = -velocity[0]#Change the velocity to negative
            velocity[1]=-velocity[1]#Change the velocity to negative
            score+=1#Increment the score
    for i in bricks2:
        if i.collidepoint(ball.x,ball.y):#if the ball touches bricks2
            bricks2.remove(i)#Remove the brick
            velocity[0] = -velocity[0]#Change the velocity to negative
            velocity[1]=-velocity[1]#Change the velocity to negative
            score+=1Increment the score
    for i in bricks3:
        if i.collidepoint(ball.x,ball.y):#if the ball touches bricks3
        	bricks3.remove(i)#Remove the brick
            velocity[0] = -velocity[0]#Change the velocity to negative
            velocity[1]=-velocity[1]#Change the velocity to negative
            score+=1Increment the score
                
    if score==18:#Checking if highest score is reached
        font = pygame.font.Font(None, 74)#Using font for the text
        text = font.render("YOU WON!!", 1, RED)#Showing the text and using color to display the text
        screen.blit(text, (150,350))#Showing the text on the screen
        pygame.display.flip()#Updating the display on the screen
        pygame.time.wait(2000)#Wait to end the game
        break#Loop break to come out of the game
    pygame.time.wait(1)#Wait to end the game graphics
    pygame.display.flip()#Update the display on the screen  
pygame.quit(  )#End the game
