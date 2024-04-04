import numpy as np

def calculate_angle(a,b,c):
    a = np.array(a) # first
    b = np.array(b) # mid
    c = np.array(c) # end
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0 :
        angle = 360 - angle
    
    return angle

def position_valid(angles,position,tolerance):
    difference = [0,0,0,0]
    for i in range(4):
        difference[i] = abs(angles[i] - position[i])
    if max(difference) > tolerance:
        return False 
    return True


position_valid((0,0,0,0),(0,0,0,0),15)
print(position_valid((0,0,0,-14),(0,0,0,0),15))