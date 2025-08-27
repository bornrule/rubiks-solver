# capture_face.py
import cv2
import numpy as np

COLOR_CENTERS_HSV = {
    'W': (0, 0, 255),    
    'Y': (30, 200, 200),  
    'R': (0, 200, 200),   
    'O': (15, 200, 200),  
    'G': (60, 150, 150),  
    'B': (120, 150, 150), 
}


def extract_face_cells(img, grid_size=3):
    h, w = img.shape[:2]
    cell_h = h // grid_size
    cell_w = w // grid_size
    cells = []
    for r in range(grid_size):
        for c in range(grid_size):
            y0, x0 = r*cell_h, c*cell_w
            cell = img[y0+int(0.08*cell_h):y0+int(0.92*cell_h), x0+int(0.08*cell_w):x0+int(0.92*cell_w)]
            cells.append(cell)
    return cells


def avg_hsv_color(cell):
    hsv = cv2.cvtColor(cell, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.mean(hsv)[:3]
    return (h, s, v)


def simple_classify(hsv):
    
    best = None
    bestd = float('inf')
    for k, c in COLOR_CENTERS_HSV.items():
        d = (hsv[0]-c[0])**2 + (hsv[1]-c[1])**2 + (hsv[2]-c[2])**2
        if d < bestd:
            bestd = d
            best = k
    return best
