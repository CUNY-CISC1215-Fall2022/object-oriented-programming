import math
import random
import turtle
import copy

# Create two classes: One for Points (an (x, y) coordinate) and a
# Rectangle (a geometric shape)
class Point:
    pass


class Rectangle:
    pass

# A function for computing the distance between two Point objects
def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.sqrt(dx**2 + dy**2)
    return dist

# A function to create a new object of type Point with the given x, y coordinates
def create_point(x, y):
    p = Point()
    p.x = x
    p.y = y

    return p

# A function to create a new object of type Rectangle with the given width and
# height, with a corner point at a given point object.
def create_rectangle(width, height, p):
    r = Rectangle()
    r.width = width
    r.height = height
    r.corner = p

    return r

# A function to print out a Point object, since Python cannot do it natively
def print_point(p):
    print("(" + str(p.x) + ", " + str(p.y) + ")")

# A function to print out a Rectangle object, since Python cannot do it natively
def print_rectangle(r):
    print("Rectangle Width: ", r.width, "Height: ", r.height)
    print_point(r.corner)


# A destructive function for resizing a rectgangle object by a specified amount
def resize_rectangle(rectangle, dh, dw):
    rectangle.width = rectangle.width + dw
    rectangle.height = rectangle.height + dh

# A nondestructive function for resizing a rectangle object. The function returns
# a new Rectangle with updated dimensions.
def resize_rectangle_nondestructive(rectangle, dh, dw):
    # To make this nondestructive, we have to do a deep copy on the Rectangle.
    # This means that Python will make a copy of both the Rectangle object (so
    # we do not modify the original) and its embedded Point object (so our new
    # rectangle does not alias the old rectangle's corner point)
    #
    # If we perform a shallow copy instead (i.e., copy.copy(rectangle)), then
    # both the new recangle and old rectangle will share the same point. That
    # means that moving one will move the other, too!
    r2 = copy.deepcopy(rectangle)
    r2.width += dw
    r2.height += dh
    return r2

# A destructive function for changing the position of a rectangle by a specified amount
def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x = rectangle.corner.x + dx
    rectangle.corner.y = rectangle.corner.y + dy


# A nondestructive function for moving a rectangle object by a specified amount
def move_rectangle_nondestructive(rectangle, dx, dy):
    # Like resizing, we have to make a deep copy so the new Rectangle object
    # does not share the same corner point as the original!
    r2 = copy.deepcopy(rectangle)
    r2.corner.x = rectangle.corner.x + dx
    r2.corner.y = rectangle.corner.y + dy

    return r2

# An example of nondestructively changing rectangles:
r1 = create_rectangle(100, 100, create_point(1,1))
print_rectangle(r1)

# Nondestructively resize the rectangle, making a copy
r2 = resize_rectangle_nondestructive(r1, 3, 2)
print_rectangle(r2)

# Now destructively move the copied rectangle.
# r2 (the copy) and r1 (the original) should be at different
# positions, but this is only because we make a deep copy in the
# resize_rectangle_nondestructive() function!
move_rectangle(r2, 40, 40)
print_rectangle(r2)
print_rectangle(r1)





# Having a little fun with this: Generate 100 random points,
# create a turtle and draw them, then compute how far the turtle
# traveled.
#
# Commented out since some people may be running in Python Anywhere.
# Uncomment everything below to run the turtle example:

# rand_points = []
# for i in range(100):
#     x_rand = random.randint(0, 100)
#     y_rand = random.randint(0, 100)

#     p = create_point(x_rand, y_rand)
#     rand_points.append(p)

# t = turtle.Turtle()

# last_point = create_point(0,0)
# total_distance = 0
# for p in rand_points:
#     total_distance = total_distance + distance(last_point, p)
#     last_point = p
#     t.goto(p.x, p.y)

# print("Total: ", total_distance)
# turtle.mainloop()
