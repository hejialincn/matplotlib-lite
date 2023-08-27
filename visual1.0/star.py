import turtle as t
def draw_star(t, size):
    t.pendown()
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()

def draw_polygon(t, num_sides, side_length):
    for _ in range(num_sides):
        t.forward(side_length)
        t.right(360/num_sides)

def draw_polygons(t, num_sides, side_length, num_polygons):
    for _ in range(num_polygons):
        draw_polygon(t, num_sides, side_length)
        t.forward(side_length)
        t.right(360/num_sides)
    
def draw_star_polygon(t, num_sides, side_length, num_polygons):
    for _ in range(num_polygons):
        draw_star(t, side_length)
        t.forward(side_length)
        t.right(360/num_sides)
def draw_polygons_with_stars(t, num_sides, side_length, num_polygons):
    for _ in range(num_polygons):
        draw_polygon(t, num_sides, side_length)
        t.forward(side_length)
        t.right(360/num_sides)
        draw_star(t, side_length)
        t.forward(side_length)
        t.right(360/num_sides)
draw_polygons_with_stars(t,20,10,20)
