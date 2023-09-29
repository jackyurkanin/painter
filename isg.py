##### infinte square generator
#
#
##### Imports #######
from PIL import Image, ImageDraw
from screeninfo import get_monitors
import random
import cv2
import numpy as np
import objc
from Quartz.CoreGraphics import CGDisplayBounds
# 
#
#
#

def blank_slate(im=True):
    """
    returns a white image
    """
    # ###### MAC ########## No Need to adjust the windows works fine
    # objc.loadBundle('Cocoa', globals(), bundle_path=objc.pathForFramework("/System/Library/Frameworks/Cocoa.framework"))
    # primary_display_id = CGDisplayBounds(0)
    # width = int(primary_display_id.size.width)
    # height = int(primary_display_id.size.height)
    # print(width, height)

    ###### Windows ######
    monitors = get_monitors()
    width = monitors[0].width+57 # no idea why we need the 57 but it fills the fullscreen without a gray bar
    height = monitors[0].height
    if im:
        return Image.new("RGB", (width, height), "white") , width, height
    else:
        return width, height


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
        cv2.namedWindow("Fullscreen Window", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("Fullscreen Window", image_cv)
        if length > width//2:
            length-=1
            list_of_colors.pop(0)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            is_pressed = False
    img.close()
    cv2.destroyAllWindows()

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

def isg_normal_rand_len_zones():
    """
    Like normal but it draws a random length of a the randomly
    chosen pixel color creating random length zones
    """
    img, width, height = blank_slate()
    origin = (width//2, height//2)  
    is_pressed = True
    draw = ImageDraw.Draw(img)
    list_of_colors = []
    length = -2
    length_of_zone = 0
    while is_pressed:        
        if length_of_zone == 0:
            length_of_zone = random.randint(1,round(width/8)) # here to change how long each zone could be
            pixel = [0,0,0]
            for i in range(3):
                pixel[i] = random.randint(0, 255)
            pixel = tuple(pixel)
        length_of_zone -= 1
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

def isg_normal_rand_len_zones_with_edges():
    """
    same as rand_len_zone but adds wall edges
    """
    width, height = blank_slate(False)
    img = np.zeros((height, width, 3), dtype=np.uint8)
    origin = (width//2, height//2)  
    is_pressed = True
    list_of_colors = []
    length = -2
    length_of_zone = 0
    while is_pressed:        
        if length_of_zone == 0:
            length_of_zone = random.randint(1,round(width/8)) # here to change how long each zone could be
            pixel = [0,0,0]
            for i in range(3):
                pixel[i] = random.randint(0, 255)
            pixel = tuple(pixel)
        length_of_zone -= 1
        img[origin[1], origin[0]] = pixel 
        list_of_colors.append(pixel)
        length+=1
        ind=length
        x_1 = width//2 - 1
        x_2 = width//2 + 1
        y_1 = height//2 - 1
        y_2 = height//2 + 1
        while ind >= 0: # DRAW FOUR LINES
            line_color = list_of_colors[ind]  # RGB color (red)
            new_color = [0,0,0]
            for i in range(3):
                if line_color[i]-10 < 0:
                    new_color[i] = 0
                else:
                    new_color[i] = line_color[i]-10


            
            new_color = tuple(new_color)
            img[y_1:y_2, x_1] = line_color
            img[y_1:y_2, x_2] = line_color
            img[y_1, x_1:x_2] = line_color
            img[y_2, x_1:x_2] = line_color
            img[y_1,x_1] = new_color
            img[y_2,x_1] = new_color
            img[y_1,x_2] = new_color
            img[y_2,x_2] = new_color
            if y_1 >0:
                y_1-=1
            if y_2<height-1:
                y_2+=1
            if x_1>0:
                x_1-=1
            if x_2 <width-1:
                x_2+=1
            ind-=1
        
        cv2.imshow("Image", img)
        if length > width//2:
            length-=1
            list_of_colors.pop(0)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            is_pressed = False
    cv2.destroyAllWindows()

def isg_normal_rand_len_zones_with_edges_and_realism(growth=10):
    """
    same as normal rand len zone with edges but wall length grows as they get closer
    every 10 steps it grows 1 length
    """
    width, height = blank_slate(False)
    img = np.zeros((height, width, 3), dtype=np.uint8)
    origin = (width//2, height//2)  
    is_pressed = True
    list_of_colors = []
    length_of_zone = 0
    while is_pressed:        
        if length_of_zone == 0:
            length_of_zone = random.randint(1,10) # here to change how long each zone could be
            pixel = [0,0,0]
            for i in range(3):
                pixel[i] = random.randint(0, 255)
            pixel = tuple(pixel)
        length_of_zone -= 1
        img[origin[1], origin[0]] = pixel 
        list_of_colors.append(pixel)
        ind=len(list_of_colors)-1

        x_1 = width//2 - 1
        x_2 = width//2 + 1
        y_1 = height//2 - 1
        y_2 = height//2 + 1
        tracker = 0
        while ind >1 and tracker< width//2: 
            line_color = list_of_colors[ind]  # RGB color (red)
            if tracker%growth == 0:
                # push out and increase
                ind+=1
                list_of_colors.insert(ind, line_color)
            
            new_color = [0,0,0]
            for i in range(3):
                if line_color[i]-growth < 0:
                    new_color[i] = 0
                else:
                    new_color[i] = line_color[i]-growth

            new_color = tuple(new_color)
            img[y_1:y_2, x_1] = line_color
            img[y_1:y_2, x_2] = line_color
            img[y_1, x_1:x_2] = line_color
            img[y_2, x_1:x_2] = line_color
            img[y_1,x_1] = new_color
            img[y_2,x_1] = new_color
            img[y_1,x_2] = new_color
            img[y_2,x_2] = new_color
            if y_1 >0:
                y_1-=1
            if y_2<height-1:
                y_2+=1
            if x_1>0:
                x_1-=1
            if x_2 <width-1:
                x_2+=1
            ind-=1
            tracker +=1
        
        cv2.imshow("Image", img)
        l = len(list_of_colors)
        if l > width//2:
            skip = l - width//2
            
            list_of_colors = list_of_colors[skip:]
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            is_pressed = False
    cv2.destroyAllWindows()


def isg(t='normal'):
    if t == 'normal':
        isg_normal()
    elif t == 'nrlz':
        isg_normal_rand_len_zones()
    elif t =='nrlzwe':
        isg_normal_rand_len_zones_with_edges()
    elif t =='nrlzwear':
        isg_normal_rand_len_zones_with_edges_and_realism()

if __name__ =='__main__':
    type_of_painting = input('Enter the type of drawing that you would like: ')
    isg(type_of_painting)