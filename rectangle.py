def intersection(rectangle1, rectangle2):
    x1, y1, w1, h1 = rectangle1
    x2, y2, w2, h2 = rectangle2
    return (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2)

rectangle1 = (0, 0, 4, 4)
rectangle2 = (2, 2, 4, 4)

print("Rectangles are intersecting" if intersection(rectangle1, rectangle2) else "Rectangles are not intersecting")
