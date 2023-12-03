import urllib.request
import cv2

import numpy as np

# Đường link đến video
#url = 'https://streaming-cms-tpo.epicdn.me/0dbd6e8955918dc941d279f75508e5a6/6518fcd0/2023_09_29/tieu_diem_309_9697.mp4'
url = 'http://172.20.10.4/cam-hi.jpg'
# Tạo một đối tượng VideoCapture để đọc video từ đường link
cap = cv2.VideoCapture(url)

# Kiểm tra xem có mở được video không
if not cap.isOpened():
    print("Không thể mở video từ đường link.")
    exit()

while True:
    # Đọc một frame từ video
    #ret, frame = cap.read()
    response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(response.read()), dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # Kiểm tra nếu đọc frame thành công
   
    #if not ret:
     #   break

    # Hiển thị frame
    cv2.imshow('Video', frame)

    # Để thoát vòng lặp khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
