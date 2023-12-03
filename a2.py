#day la phien ban on dinh nhat muon sua chi coppy ra file moi r sua nghe cu

import cv2
import face_recognition
import urllib.request
import numpy as np

# Load ảnh chứa khuôn mặt cần nhận diện
known_image = face_recognition.load_image_file("bac.jpg")

# Xác định các khuôn mặt trong ảnh đã biết
known_face_encoding = face_recognition.face_encodings(known_image)[0]



# Kết hợp danh sách tên và mã số của các khuôn mặt đã biết
known_face_names = ["Ten bac"]

# Khởi tạo webcam hoặc đường dẫn tới video
#video_capture = cv2.VideoCapture(0)  # Sử dụng 0 để sử dụng webcam mặc định, hoặc bạn có thể điền đường dẫn tới video.
url = "http://172.20.10.4/cam-lo.jpg"
# Tạo một đối tượng VideoCapture để đọc video từ đường link


cap = cv2.VideoCapture(url)
if not cap.isOpened():
    print("Không thể mở video từ đường link.")
    exit()
while True:
    # Đọc frame từ video
    #doc tu cam laptop
    #ret, frame = cap.read() 
    
    response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(response.read()), dtype=np.uint8)
    frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # Tìm tất cả các khuôn mặt trong frame hiện tại
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Kiểm tra từng khuôn mặt trong frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # So sánh khuôn mặt này với các khuôn mặt đã biết
        matches = face_recognition.compare_faces([known_face_encoding], face_encoding)

        name = "khong xac dinh"  # Mặc định nếu không tìm thấy khuôn mặt đã biết nào

        # Nếu có ít nhất một khuôn mặt đã biết khớp với khuôn mặt trong frame
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Vẽ khung xung quanh khuôn mặt và đặt tên
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Hiển thị frame kết quả
    cv2.imshow('Video', frame)

    # Thoát khỏi vòng lặp nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng các tài nguyên và đóng cửa sổ video
cap.release()
cv2.destroyAllWindows()
