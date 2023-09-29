##### Natural INF square generator #
#
#
##### Imports ######################
from isg import blank_slate
import random
import cv2
import numpy as np
####################################


def random_color_natural_growth(growth=10):
    """
    grows out naturally and blends when colors overlap
    start drawing from origin and use color map to draw
    update map on each turn

    EXAMPLE
    start:

            x


    next: 
            x
           xbx
            x

    next:
            x
           xbx
          xbcbx
           xbx
            x
    next:
            x
           xbx
          xbcbx
         xbcdcbx
          xbcbx
           xbx
            x

    """
    width, height = blank_slate(False)
    width, height = width//5, height//5
    img = np.zeros((height, width, 3), dtype=np.uint8)
    origin = (height//2, width//2)  
    is_pressed = True
    coord2color = {}
    length_of_zone = 0
    while is_pressed:        
        if length_of_zone == 0:
            length_of_zone = random.randint(1,10) # here to change how long each zone could be
            pixel = [0,0,0]
            for i in range(3):
                pixel[i] = random.randint(0, 255)
            pixel = tuple(pixel)
        length_of_zone -= 1
        coord2color[origin] = pixel

        new_coord_map = {}
        for coord in coord2color.keys():
            color = coord2color[coord]
            img[coord[0],coord[1]] = color

            x_1 = coord[1] - 1
            x_2 = coord[1] + 1
            y_1 = coord[0] - 1
            y_2 = coord[0] + 1
            if coord ==origin:
                update = {(coord[0],x_2), (y_1, coord[1]), (y_2, coord[1]), (coord[0],x_1)}
            elif coord[0] < origin[0] and coord[1] == origin[1]: #if coord straight up from origin
                update = {(coord[0],x_2), (y_1, coord[1]), (coord[0],x_1)} #grow up, left, and right
            elif coord[0] > origin[0] and coord[1] == origin[1]: #if coord straight down from origin
                update = {(coord[0],x_2), (y_2, coord[1]), (coord[0],x_1)} #grow down, left, and right
            elif coord[1] < origin[1] and coord[0] == origin[0]: #if coord straight left from origin
                update = {(y_1, coord[1]), (y_2, coord[1]), (coord[0],x_1)} #grow up, left, and down
            elif coord[1] > origin[1] and coord[0] == origin[0]: #if coord straight right from origin
                update = {(coord[0],x_2), (y_1, coord[1]), (y_2, coord[1])} #grow up, down, and right
            elif coord[0] < origin[0] and coord[1] < origin[1]: # if coord is up and left from origin
                update = {(y_1, coord[1]), (coord[0],x_1)}  #grow up and left
            elif coord[0] > origin[0] and coord[1] < origin[1]: # if coord is down and left from origin
                update = {(y_2, coord[1]), (coord[0],x_1)}  #grow down and left
            elif coord[0] < origin[0] and coord[1] > origin[1]: # if coord is up and right from origin
                update = {(y_1, coord[1]), (coord[0],x_2)}  #grow up and right
            elif coord[0] > origin[0] and coord[1] > origin[1]: # if coord is down and right from origin
                update = {(y_2, coord[1]), (coord[0],x_2)}  #grow down and right
            else:
                print("missed",coord)
            for i in update:
                if i[0] >=0 and i[0] < height and i[1] >= 0 and i[1]< width:
                    if i not in new_coord_map:
                        new_coord_map[i] = color
                
        coord2color = new_coord_map.copy()
        cv2.imshow("Image", img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            is_pressed = False
    cv2.destroyAllWindows()





def rcngg(t='rcng'):
    if t=='rcng':
        random_color_natural_growth()


if __name__ =='__main__':
    # type_of_painting = input('Enter the type of drawing that you would like: ')
    rcngg()