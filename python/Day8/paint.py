import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    can = math.ceil(area / cover)

    return print(f"You need {int(can)} number of cans to paint your wall")


paint_calc(height=test_h, width=test_w, cover=coverage)