from PIL import Image
import random


def build(height, width):
    """ grabs a point at random and will paint from that point for a
    random number of pixels afterwards it will repeat. To paint the
    points nearby will be averaged, added to a random number between
    0 & 256, then divided by 2."""
    artwork = Image.new("RGB", (width, height), "White")
    pixel_dict, neighbors = make_pixel_dict(height, width)
    queue = neighbors.keys()
    while queue:
        coord = mapped.pop()
        values = pixel_dict[coord]
        neighs = neighbors[coord]
        averages = get_avg(coord, neighs, pixel_dict)
        ind = random.randint(0, 3)
        avg = averages[ind]
        if avg >0:
            new = round((255*random.random() + avg)/2)
        else:
            new = round(255*random.random())

        if ind == 0:
            newd = (new, values[1], values[2])
        elif ind == 1:
            newd = (values[0], new, values[2])
        else:
            newd = (values[0], values[1], new)
        pixel_dict[coord] = newd


def get_avg(coord, neighbors, mapy):
    """check the neighbors and get avg rgb"""
    scores_r = []
    scores_g = []
    scores_b = []
    for neigh in neighbors[coord]:
        scores_r.append(mapy[neigh][0])
        scores_g.append(mapy[neigh][1])
        scores_b.append(mapy[neigh][2])
    return sum(scores_r) / len(scores_r), sum(scores_g) / len(scores_g), sum(scores_b) / len(scores_b)


def make_pixel_dict(height, width):
    """makes a coordinate for every pixel
        tbd- looks like a dictionary with tuple keys that access points in the graph
    """
    neighbors = {}
    mapped = {}
    for h in range(height-1):
        for w in range(width-1):
            key = (h,w)
            mapped[key] = (0, 0, 0)
    for coord in mapped:
        neighs = set()
        for i in range(3):
            if coord[0] - 1 + i > 0 and coord[0] - 1 + i != height: # first check h is not below 0 nd not the height
                for k in range(3):
                    if coord[1] - 1 + k > 0 and coord[1] - 1 + k != width:# check its not below 0 and not the width
                        neighs.add((coord[0] - 1 + i, coord[1] - 1 + k))
        neighbors[coord] = neighs

    return mapped, neighbors


if __name__ == "__main__":
    first = build(4, 4)
    pixel_dict = make_pixel_dict()
    first.save("/Desktop/" + first.title + ".jpg")
    first.show()

    # ma = make_pixel_list([2, 2, 2])
    # print(ma)
