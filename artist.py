###### Main Painter code #######
#       METHODS:
#   1. infinte square generator
#
#
#
#
#################################
###### IMPORTS ######
from isg import isg
from rcngg import rcngg

#################################

class Artist:
    def __init__(self):
        print("Today was the dawn of a new creator")

    def paint(self):
        type_of_painting = input('Enter the type of drawing that you would like: ')
        parsed = type_of_painting.split(' ')
        if parsed[0] == 'isg':
            isg(parsed[1])
        elif parsed[0] == 'rcngg':
            rcngg()
if __name__ == "__main__":
    coibdun = Artist()
    coibdun.paint()

