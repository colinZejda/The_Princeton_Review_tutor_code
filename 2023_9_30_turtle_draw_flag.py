# paste your code below
import turtle

# create a function called draw_rectangle
# inputs: coordinates, width, height, color
def draw_rectangle(x, y, w, h, color):
  
  	# setup
    turtle.penup()            # lift pen up first
    turtle.goto(x, y)         # go to coordinates
	turtle.fillcolor(color)   # set fill color to color
    turtle.begin_fill()
    
    # now, actually draw the rectangle 
  	turtle.foward(width)      # draw line L->R, width
    turtle.right()            # turns right, doesn't draw
    
    turtle.forward(height)
    turtle.right()
    
    turtle.forward(width)     
    turtle.right()
    
    turtle.forward(height)
    
    # complete the fill
    turtle.end_fill()
    
# the main function that runs (calls all other functions)
def main():
  
    # get user input
    width = input('Enter a width: ')
    height = input('Enter a height: ')
    
    # set up graphics window (our canvas to write on)
    # make it dynamic with w, h, add buffer of 200
    buffer = 200
   	turtle.setup(width + buffer, height + buffer)
    turtle.speed(10)
    
    # setup done, time to draw
    for i in range(5):             # 5 rects
        next_x = (i+1) * (w/5)     # when drawing next rectangle, we don't need to move up/down, just L/R
        
    # new coordinates: dependent on buffer in order to center the "flag" of 5 different colored rectangles
    # buffer/2 = space above and below this "flag"
    # width/5 bc we have 5 rectangles
    # height/1 bc all rectangles are the same height of "flag"
    draw_rectangle(next_x + buffer/2, buffer/2, width/5, height, color)
        
    