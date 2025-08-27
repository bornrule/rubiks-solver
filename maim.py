# main.py
import cv2
from capture_face import extract_face_cells, avg_hsv_color, simple_classify

CAM_INDEX = 0

def main():
    cap = cv2.VideoCapture(CAM_INDEX)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    print("Press SPACE to capture a frame. Press q to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow('RubiksSolver - Live', frame)
        k = cv2.waitKey(1)
        if k % 256 == 32:  
            
            cv2.imwrite('samples/face_sample.jpg', frame)
            print('Saved sample to samples/face_sample.jpg')
            
            h, w = frame.shape[:2]
            s = min(h, w) // 2
            cx, cy = w//2, h//2
            x0, y0 = cx - s//2, cy - s//2
            square = frame[y0:y0+s, x0:x0+s]
            cells = extract_face_cells(square)
            hsvs = [avg_hsv_color(c) for c in cells]
            labels = [simple_classify(hsv) for hsv in hsvs]
            print('Cell labels:', labels)
        elif k & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
