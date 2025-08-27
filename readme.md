# Rubik's Cube Solver (Linux - Python)

An experimental project that uses **OpenCV** to detect the colors of a Rubik's Cube from a webcam feed,  
then solves the cube using the **Kociemba algorithm** and generates a step-by-step video solution.

---

## ⚙️ Requirements

- Python 3.9 or later
- Python libraries:
  - `opencv-python`
  - `numpy`
  - `kociemba`

---

## 🚀 Getting Started

1. Create a project folder and move into it:
   ```bash
   
   mkdir rubiks_solver && cd rubiks_solver
``bash

2. (Optional) create a virtual environment:
``bash
python3 -m venv venv
source venv/bin/activate
``bash

3. Install requirements:
``bash
pip install -r requirements.txt
``bash

4. Run the program:
``bash
python main.py
``bash
##🎥 Usage Instructions

When the app starts, it will open a live webcam feed.

A green 3×3 grid overlay will be displayed in the center of the screen.

Place one cube face inside the grid and press SPACE to capture it.

Follow the sequence of faces: U, R, F, D, L, B.

Press r to reset and start capturing faces again.

Once all six faces are captured, press q to compute the solution.

A video file (samples/solution.avi) will be generated showing the solution step by step.

The video will also be displayed automatically. Press q in the video window to stop playback.

   
