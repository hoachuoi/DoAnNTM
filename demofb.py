from firebase import firebase

# Khởi tạo kết nối đến Firebase Realtime Database
firebase_url = 'https://esp8266-5e2f2-default-rtdb.firebaseio.com'  # Thay thế bằng URL cơ sở dữ liệu Firebase của bạn
fb = firebase.FirebaseApplication(firebase_url, None)

# Gửi dữ liệu lên Firebase
data_to_send = {
    'temperature': 25,
    'humidity': 60
}



result = fb.post('/demo', data_to_send)  # Thay thế '/data' bằng đường dẫn trong cơ sở dữ liệu của bạn

print(f"Data sent. Result: {result}")

# Nhận dữ liệu từ Firebase
data = fb.get('/led', None)  # Thay thế '/data' bằng đường dẫn trong cơ sở dữ liệu của bạn

print("Data received:")
print(data)
