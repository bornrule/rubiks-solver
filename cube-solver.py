# cube_solver.py
import kociemba


def build_kociemba_string(face_labels):
    
    order = ['U','R','F','D','L','B']
    s = ''
    for face in order:
        s += ''.join(face_labels[face])
    return s


def solve_from_faces(face_labels):
    cube_str = build_kociemba_string(face_labels)
    sol = kociemba.solve(cube_str)
    return sol
