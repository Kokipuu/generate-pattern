import cv2
import numpy as np
import math
from shapely.geometry import Polygon


def judge_rect_overlap(rect1, rect2):
    for rect in rect2:
        if (rect1[0] < rect[0] + rect[2] and rect1[0] + rect1[2] > rect[0] and
            rect1[1] < rect[1] + rect[3] and rect1[1] + rect1[3] > rect[1]):
            return True
    return False

def judge_circle_overlap(circle1, circle2):
    for circle in circle2:
        d = math.sqrt(abs(circle1[0] - circle[0])**2 + abs(circle1[1] - circle[1])**2)
        if(d < (circle1[2] + circle[2])):
            return True
    return False

def judge_triangle_overlap(tri1, tri2):
    if(len(tri1) == 0 or len(tri2) == 0):
        return False
    tri1 = Polygon(tri1)
    for tri in tri2:
        tri = Polygon(tri)
        if tri.intersects(tri1) or tri1.intersects(tri):
            return True
    return False

def triangle_get_point(x, y, size):
    # Calculate the height of the equilateral triangle
    height = size * 0.5
    width =  size * (np.sqrt(3) / 2)

    # Calculate the coordinates of the three vertices
    vertex1 = (x, y + size)
    vertex2 = (x + width, y - height)
    vertex3 = (x - width, y - height)

    return vertex1, vertex2, vertex3



def generate_nan_overlap_position(shape, shape_size, num, x_range, y_range):

    # shapeの中心座標
    position_set = []
    # 最初の1点をランダムにプロット
    x1,y1 = generate_random_point(x_range, y_range, shape_size)
    position_set.append([x1,y1])

    if shape == 'circle':
        for i in range(num-1):
            flag = True
            try_count = 0
            while flag:
                x,y = generate_random_point(x_range, y_range, shape_size)
                distance = []
                for j in range(i+1):
                    dis = (x - position_set[j][0])**2 + (y - position_set[j][1])**2
                    distance.append(dis)
                
                criteria = shape_size*2
                if distance_check(distance, criteria)==False:
                    flag = False
                    break                

                try_count += 1     
                if try_count>50:
                    print("cannot find suitable position.")
                    print("Please decrease the number of the object or the size of the object. ")
                    return "error"

            position_set.append([x,y])
        
    elif shape == 'triangle':
        for i in range(num-1):
            flag = True
            try_count = 0
            while flag:
                x,y = generate_random_point(x_range, y_range, shape_size)
                distance = []
                for j in range(i+1):
                    dis = (x - position_set[j][0])**2 + (y - position_set[j][1])**2
                    distance.append(dis)
                
                criteria = shape_size*2
                if distance_check(distance, criteria)==False:
                    flag = False
                    break                

                try_count += 1     
                if try_count>100:
                    print("cannot find suitable position.")
                    print("Please decrease the number of the object or the size of the object. ")
                    return "error"

            position_set.append([x,y])

    elif shape == 'rectangle':
        for i in range(num-1):
            flag = True
            try_count = 0
            while flag:
                x,y = generate_random_point(x_range, y_range, shape_size)
                distance = []
                for j in range(i+1):
                    dis = (x - position_set[j][0])**2 + (y - position_set[j][1])**2
                    distance.append(dis)
                
                criteria = (shape_size/2)*np.sqrt(2)
                if distance_check(distance, criteria)==False:
                    flag = False
                    break                

                try_count += 1     
                if try_count>50:
                    print("cannot find suitable position.")
                    print("Please decrease the number of the object or the size of the object. ")
                    return "error"

            position_set.append([x,y])

    return position_set


def generate_random_point(x_range, y_range, size):
    x = np.random.uniform(size/2, x_range-size/2)
    y = np.random.uniform(size/2, y_range-size/2)
    return x, y


def distance_check(distance, criteria):
    for i in range(len(distance)):
        if distance[i] < criteria:
            return True
    return False    
    