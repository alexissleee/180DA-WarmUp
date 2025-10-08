import numpy as np
import cv2

from sklearn.cluster import KMeans

cap = cv2.VideoCapture(0)

# designated rectangle size 
des_rect_size = 125  # pixels

cluster_n = 5

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Display the resulting frame
    # cv2.imshow('frame',gray)

    if not ret:
        break

    h, w, _ = frame.shape
    cx, cy = w // 2, h // 2 # calc center coords of central rect

    # central rectangle bounding points
    x1, y1 = cx - des_rect_size // 2, cy - des_rect_size // 2
    x2, y2 = cx + des_rect_size // 2, cy + des_rect_size // 2

    area = frame[y1:y2, x1:x2]  # square 
    area_pixels = area.reshape((-1, 3))  # np reshaping to 3

    # Apply KMeans to find dominant color
    kmeans = KMeans(n_clusters=cluster_n, n_init=10)
    labels = kmeans.fit_predict(area_pixels)
    counts = np.bincount(labels)
    dominant_color = kmeans.cluster_centers_[np.argmax(counts)].astype(int)

    # Draw rectangle and dominant color patch
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.rectangle(frame, (10, 10), (60, 60), tuple(dominant_color.tolist()), -1)

    # show the values of the "dominant color"
    cv2.putText(frame, f"BGR: {tuple(dominant_color)}", (70, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Dominant Color", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()