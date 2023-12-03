import cv2
import face_recognition
import urllib.request
import numpy as np
import firebase_admin
from firebase_admin import credentials, db

# Load ảnh chứa khuôn mặt cần nhận diện
known_image = face_recognition.load_image_file("bac.jpg")

# Xác định các khuôn mặt trong ảnh đã biết
known_face_encoding = face_recognition.face_encodings(known_image)[0]



# Kết hợp danh sách tên và mã số của các khuôn mặt đã biết
known_face_names = ["Ten bac"]

# Khởi tạo webcam hoặc đường dẫn tới video
video_capture = cv2.VideoCapture(0)  # Sử dụng 0 để sử dụng webcam mặc định, hoặc bạn có thể điền đường dẫn tới video.
#url = "http://172.20.10.4/cam-lo.jpg"
# Tạo một đối tượng VideoCapture để đọc video từ đường link
cred = credentials.Certificate('demontm-b4d91-firebase-adminsdk-w7byl-283e372f9a.json')

# Khởi tạo ứng dụng Firebase với xác thực
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://demontm-b4d91-default-rtdb.firebaseio.com/'
})

# Đối tượng tham chiếu đến Realtime Database
ref = db.reference('/ntm/khoacua')

cap = cv2.VideoCapture(0)
while True:
    # Đọc frame từ video
    #doc tu cam laptop
    ret, frame = cap.read() 
    
    #response = urllib.request.urlopen(url)
    #img_array = np.array(bytearray(response.read()), dtype=np.uint8)
    #frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # Tìm tất cả các khuôn mặt trong frame hiện tại
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    if not face_locations:
        tm =0
    else:
        tm=1
    if tm == 0:
            data_to_upload = {'state': 0}
            ref.set(data_to_upload) 
    print(tm)
    # Kiểm tra từng khuôn mặt trong frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # So sánh khuôn mặt này với các khuôn mặt đã biết
        matches = face_recognition.compare_faces([known_face_encoding], face_encoding)

        name = "khong xac dinh"  # Mặc định nếu không tìm thấy khuôn mặt đã biết nào
        tmp =4
        # Nếu có ít nhất một khuôn mặt đã biết khớp với khuôn mặt trong frame
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            tmp =3
        # Vẽ khung xung quanh khuôn mặt và đặt tên
        print(tmp)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        
        if (tmp == 3):
            data_to_upload = {'state': 1}
            ref.set(data_to_upload)
        if (tmp == 4):
            data_to_upload = {'state': 0}
            ref.set(data_to_upload)
    # Hiển thị frame kết quả
    cv2.imshow('Video', frame)

    # Thoát khỏi vòng lặp nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        data_to_upload = {'state': 0}
        ref.set(data_to_upload)
        break

# Giải phóng các tài nguyên và đóng cửa sổ video
cap.release()
cv2.destroyAllWindows()
