#Pygame is a free and open-source cross-platform library used for the development of multimedia applications like video games using Python.
import pygame

#Pygame.init() initializes all imported pygame modules. No exceptions will be raised if a module fails, but the total number of successful and failed inits will be returned as a tuple. You can always initialize individual modules manually, but pygame.init() initializess all the imported pygame modules. It is used to raise exceptions when the module fails. The init() functions for individual modules will raise exceptions when they fail
pygame.init()

#In Pygame, colors are expressed according to how much volumne of red, green, and blue they have in them, hence we use the term RGB color code. You provide three values in the parentheses: one for each color (red, green, and blue), ranging from 0 for none, up to 255 for the maximum. To understand hexcolors in detail, refer to "https://www.pygame.org/docs/ref/color.html"
WHITE = (255,255,255)                                                           #Hex code for white color
DARKBLUE = (36,90,190)                                                          #Hex code for darkblue color
LIGHTBLUE = (0,176,240)                                                         #Hex code for lightblue color
RED = (255,0,0)                                                                 #Hex code for red color

#Pygame uses Rect objects to store and manipulate rectangular areas. By using Rect, we can specify a combination of left, top, width, and height values. Rects can also be created from python objects that are already a Rect or have an attribute named "rect". 
#Here we are drawing templates for bricks in a horizontal manner where bricks1 is the lowermost layer. We are drawing 6 blocks by using "list comprehension"==> used for creating new lists from other iterables. As list comprehensions return lists, they consist of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.
bricks1=[pygame.Rect(10 + i* 100,60,80,30) for i in range(6)]
bricks2=[pygame.Rect(10 + i* 100,100,80,30) for i in range(6)]
bricks3=[pygame.Rect(10 + i* 100,140,80,30) for i in range(6)]

#A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity to your application and a high degree of code reusing functionality.
#As you already know, Python gives you many built-in functions like print(), etc., but you can also create your own functions. These functions are called user-defined functions.
def draw_brick(brick_list):                                                     #Drawing the brick using a function

#For Loop: It has the ability to iterate over the items of any sequence, such as a list or a string.
    for i in brick_list:                                                        #Passing the bricks as a list in the for loop
        pygame.draw.rect(screen,RED,i)                                          #Draws a rectangle on the given surface.

#Variables are nothing but reserved memory locations to store values. This means that when you create a variable, you reserve some space in memory.
#Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.
score = 0                                                                       #Assign a variable named score value = 0. This is also called as "variable initialization"


#The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. One important thing about a list is that items in a list need not be of the same type. For example: L1=[“python”, 3]
velocity=[1,1]                                                                  #A list is created to control the velocity of ball, paddle in further code to come

#Pygame can only have a single display active at any time. Creating a new one with pygame.display.set_mode() will close the previous display. 
size = (600, 600)                                                               #Variable for setting the display
screen = pygame.display.set_mode(size)

#If the display has a window title, this function will change the name on the window
pygame.display.set_caption("Breakout Game")

paddle=pygame.Rect(300,550,60,10)                                               #Draw a template for paddle
ball=pygame.Rect(200,250,10,10)                                                 #Draw a template for ball
carryOn = True                                                                  #A flag variable which will later be used in while loop

#A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true.
while carryOn:                                                                  #Run as long as carryOn is set to "True"
    for event in pygame.event.get():                                            # User did something
        if event.type == pygame.QUIT:                                           # If user clicked close
            carryOn = False                                                     #Flag is set to "False" so that it could exit the "while loop"

#fill function which fills the surface object, our screen, with the red colour. This makes everything we have drawn on the screen surface visible and updates the contents of the entire display. Without this line, the user wouldn't see anything on their pygame screen.
    screen.fill(DARKBLUE)

    pygame.draw.rect(screen,LIGHTBLUE,paddle)                                   #A paddle is being drawn of lightblue color

#font. get_fonts() will return a list of all the names of the fonts it can find on your system which you can then use with it.
    font = pygame.font.Font(None, 34)                                           #font for score

#render(text, antialias, color, background=None) -> Surface. This creates a new Surface with the specified text rendered on it. pygame provides no way to directly draw text on an existing Surface: instead you must use Font. render() is used to create an image (Surface) of the text
    text = font.render("Score: " + str(score), 1, WHITE)                        #Display the text of score

#The screen object represents your game screen. It is a thin wrapper around a Pygame surface that allows you to easily draw images to the screen (“blit” them). The raw Pygame surface represents the screen buffer.
    screen.blit(text, (20,10))                                                  #To show the written block of text on the screen

#paddle movement
    if event.type == pygame.KEYDOWN:                                            #If any key is pressed
        if event.key == pygame.K_RIGHT:                                         #If right arrow key is pressed
            if paddle.x<540:                                                    #Checking the movement of paddle according to the position of paddle on the screen. 540 is the maximum position to which paddle can move
                paddle.x+=5                                                     #Increase the x co-ordinate by 5 pixels
        if event.key == pygame.K_LEFT:                                          #If left arrow key is pressed
            if paddle.x>0:                                                      #Checking the movement of paddle according to the position of paddle on the screen. 0 is the min position to which the paddle can move
                paddle.x-=5                                                     #Decrease the x co-ordinate by 5 pixels

# brick wall   
    draw_brick(bricks1)                                                         #Call the function for drawing the bricks1
    draw_brick(bricks2)                                                         #Call the function for drawing the bricks2
    draw_brick(bricks3)                                                         #Call the function for drawing the bricks3

#ball movement    
    ball.x+=velocity[0]                                                         #Changing the ball's x position by adding a value through velocity 0th element i.e 1 and self
    ball.y+=velocity[1]                                                         #Changing the ball's y position by adding a value through velocity 1st element i.e 1 and self

    if ball.x>=590 or ball.x<=0:                                                #Check for maximum and minimum pixels

#Making the velocity negative (Please get yourself familiar with the game's dynamics concept i.e., physics while designing a game to understand this step. "https://www.daniweb.com/programming/game-development/threads/122431/breakout-ball-bouncing-physics" refer to "MattEvans" first answer on this post")
        velocity[0] = -velocity[0]
                                              
    if ball.y<=3:                                                               #Check for ball's y co-ordinate
        velocity[1] = -velocity[1]                                              #Making the velocity negative

#test if two rectangles overlap. Returns true if any portion of either rectangle overlap (except the top+bottom or left+right edges).
    if paddle.collidepoint(ball.x,ball.y):                                      #Check for collision

        velocity[1]=-velocity[1]                                                #Making the velocity negative
    if ball.y>=590:                                                             #Check for y co-ordinate max pixel
        font = pygame.font.Font(None, 74)                                       #Using font for the text
        text = font.render("GAME OVER", 1, RED)                                 #Showing the text and using color to display the text
        screen.blit(text, (150,350))                                            #Showing the text on the screen

#display. flip() is used for software displays. It allows only a portion of the screen to update, instead of the entire area. If no argument is passed, then it updates the entire Surface area like pygame.
        pygame.display.flip()                                                   #Updating the display on the screen

#pygame. time. delay() will pause for a given number of milliseconds based on the CPU clock for more accuracy.
        pygame.time.wait(2000)                                                  #Wait is provided before ending the game

#The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops.
#If you are using nested loops, the break statement stops the execution of the innermost loop and start executing the next line of code after the block.
        break

    pygame.draw.rect(screen,WHITE ,ball)                                        #A ball of white color is being drawn

#score
    for i in bricks1:                                                           #Applying "for loop" on bricks1
        if i.collidepoint(ball.x,ball.y):                                       #If the ball touches bricks1

#Python list method remove() searches for the given element in the list and removes the first matching element.
            bricks1.remove(i)                                                   #Remove the brick

            velocity[0] = -velocity[0]                                          #Change the velocity to negative
            velocity[1]=-velocity[1]                                            #Change the velocity to negative
            score+=1                                                            #Increment the score by 1

    for i in bricks2:                                                           #Applying "for loop" on bricks2
        if i.collidepoint(ball.x,ball.y):                                       #If the ball touches bricks2
            bricks2.remove(i)                                                   #Remove the brick
            velocity[0] = -velocity[0]                                          #Change the velocity to negative
            velocity[1]=-velocity[1]                                            #Change the velocity to negative
            score+=1                                                            #Increment the score by 1

    for i in bricks3:                                                           #Applying "for loop" on bricks1
        if i.collidepoint(ball.x,ball.y):                                       #If the ball touches bricks3
            bricks3.remove(i)                                                   #Remove the brick
            velocity[0] = -velocity[0]                                          #Change the velocity to negative
            velocity[1]=-velocity[1]                                            #Change the velocity to negative
            score+=1                                                            #Increment the score by 1

    if score==18:                                                               #Checking if highest score is reached
        font = pygame.font.Font(None, 74)                                       #Using font for the text
        text = font.render("YOU WON!!", 1, RED)                                 #Showing the text and using color to display the text
        screen.blit(text, (150,350))                                            #Showing the text on the screen
        pygame.display.flip()                                                   #Updating the display on the screen
        pygame.time.wait(2000)                                                  #Wait to end the game
        break                                                                   #Loop break to come out of the game

    pygame.time.wait(1)                                                         #Wait to end the game graphics
    pygame.display.flip()                                                       #Update the display on the screen  

#Pygame.quit runs code that deactivates the Pygame library.
pygame.quit()                                                                 #End the game
