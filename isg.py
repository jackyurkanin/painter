##### infinte square generator
#
#
##### Imports #######
from PIL import Image, ImageDraw
from screeninfo import get_monitors
import keyboard
import random
import cv2
import numpy as np
# 
#
#
#

def blank_slate():
    """
    returns a white image
    """
    monitors = get_monitors()
    width = monitors[0].width
    height = monitors[0].height
    return Image.new("RGB", (width, height), "white") , width, height


def isg_normal():
    """
    makes an image to display using random pixel colors.
    grows out from center 
    """
    img, width, height = blank_slate()
    origin = (width//2, height//2)
    is_pressed = True
    draw = ImageDraw.Draw(img)
    list_of_colors = []
    length = -2
    while is_pressed:
    # for w in range(4):
        pixel = [0,0,0]
        for i in range(3):
            pixel[i] = random.randint(0, 255)
        pixel = tuple(pixel)
        draw.point((origin[0], origin[1]), fill=pixel)
        list_of_colors.append(pixel)
        length+=1
        ind=length
        x_1 = width//2 - 1
        x_2 = width//2 + 1
        y_1 = height//2 - 1
        y_2 = height//2 + 1
        while ind >= 0: # DRAW FOUR LINES
            start_point = (x_1, y_1)
            end_point = (x_2, y_1)
            line_color = list_of_colors[ind]  # RGB color (red)
            draw.line([start_point, end_point], fill=line_color, width=1)
            start_point = (x_1, y_2)
            end_point = (x_2, y_2)
            draw.line([start_point, end_point], fill=line_color, width=1)
            start_point = (x_1, y_1)
            end_point = (x_1, y_2)
            draw.line([start_point, end_point], fill=line_color, width=1)
            start_point = (x_2, y_1)
            end_point = (x_2, y_2)
            draw.line([start_point, end_point], fill=line_color, width=1)
            
            if y_1 >= 0:
                y_1-=1
            if y_2<height:
                y_2+=1
            if x_1>=0:
                x_1-=1
            if x_2 <width:
                x_2+=1
            ind-=1
        
        image_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        cv2.imshow("Image", image_cv)
        if length > width//2:
            length-=1
            list_of_colors.pop(0)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            is_pressed = False
    img.close()
    cv2.destroyAllWindows()
    




def isg_multi():
    """
    generates similar to normal except growth rate is different 
    and need to generate multiple layers per turn
    """
    pass

def isg_random():
    """
    makes an image to display using random pixel colors.
    grows out of random point from center
    """
    pass

def isg_randmove():
    img, width, height = blank_slate()
    origin = (width//2, height//2)
    is_pressed = True
    draw = ImageDraw.Draw(img)
    list_of_colors = []
    x_1 = width//2 - 1
    x_2 = width//2 + 1
    y_1 = height//2 - 1
    y_2 = height//2 + 1
    x_1_o = width//2 - 1
    x_2_o = width//2 + 1
    y_1_o = height//2 - 1
    y_2_o = height//2 + 1


    while is_pressed:
    # for w in range(4):
        pixel = [0,0,0]
        for i in range(3):
            pixel[i] = random.randint(0, 255)
        pixel = tuple(pixel)
        draw.point((origin[0], origin[1]), fill=pixel)
        list_of_colors.append(pixel)
        ind=len(list_of_colors)-2
        x_change = random.randint(-20,20)
        y_change = random.randint(-20,20)
        x_1_o += x_change
        x_2_o += x_change
        y_1_o += y_change
        y_2_o += y_change
        x_1 = x_1_o
        x_2 = x_2_o
        y_1 = y_1_o
        y_2 = y_2_o

        while ind >= 0: # DRAW FOUR LINES
            start_point = (x_1, y_1)
            end_point = (x_2, y_1)
            line_color = list_of_colors[ind]  # RGB color (red)
            draw.line([start_point, end_point], fill=line_color, width=1)
            start_point = (x_1, y_2)
            end_point = (x_2, y_2)
            draw.line([start_point, end_point], fill=line_color, width=1)
            start_point = (x_1, y_1)
            end_point = (x_1, y_2)
            draw.line([start_point, end_point], fill=line_color, width=1)
            start_point = (x_2, y_1)
            end_point = (x_2, y_2)
            draw.line([start_point, end_point], fill=line_color, width=1)

            if y_1 >= 0:
                y_1-=1
            if y_2<height:
                y_2+=1
            if x_1>=0:
                x_1-=1
            if x_2 <width:
                x_2+=1
            ind-=1
        
        image_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        cv2.imshow("Image", image_cv)
        if len(list_of_colors) > width//2:
            list_of_colors.pop(0)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            is_pressed = False
    img.close()
    cv2.destroyAllWindows()


def isg(t='normal'):
    if t == 'normal':
        isg_normal()
    elif t =='multi':
        isg_multi()

if __name__ =='__main__':
    isg()