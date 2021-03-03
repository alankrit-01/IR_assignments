#Name: Amandeep Nokhwal
#Roll no: 2019BCS-005
import numpy as np
import math

matrix = np.ones((4, 1))
matrix[0] = float(input('Enter X coordinate: '))
matrix[1] = float(input('Enter Y coordinate: '))
matrix[2] = float(input('Enter Z coordinate: '))
ch = 'y'
while ch == 'y':
    axis = input('Enter axis for rotation: ')
    theta = float(input('Enter angle of rotation: '))
    rot = np.zeros((4, 4))
    rot[3][3] = 1
    if axis == 'x':
        rot[0][0] = 1;
        rot[1][1] = math.cos(math.radians(theta))
        rot[1][2] = -math.sin(math.radians(theta))
        rot[2][1] = math.sin(math.radians(theta))
        rot[2][2] = math.cos(math.radians(theta))
    if axis == 'y':
        rot[0][0] = math.cos(math.radians(theta))
        rot[0][2] = math.sin(math.radians(theta))
        rot[2][0] = -math.sin(math.radians(theta))
        rot[2][2] = math.cos(math.radians(theta))
        rot[1][1] = 1
    if axis == 'z':
        rot[0][0] = math.cos(math.radians(theta))
        rot[1][0] = math.sin(math.radians(theta))
        rot[0][1] = -math.sin(math.radians(theta))
        rot[1][1] = math.cos(math.radians(theta))
        rot[2][2] = 1
    rot[0][3] = float(input('Input translation for x axis(0 if none): '))
    rot[1][3] = float(input('Input translation for y axis(0 if none): '))
    rot[2][3] = float(input('Input translation for z axis(0 if none): '))
    result = np.zeros((4, 1))
    for i in range(len(rot)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                result[i][j] += rot[i][k] * matrix[k][j]
    matrix = result
    ch = input("press (y) for another set of translation ,otherwise press (n) ")

print('Coordinates w.r.t original frame are: ')
print('X: {}'.format(float(matrix[0])))
print('Y: {}'.format(float(matrix[1])))
print('Z: {}'.format(float(matrix[2])))
