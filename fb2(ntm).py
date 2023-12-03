import firebase_admin
from firebase_admin import credentials, db

# Đường dẫn đến tệp JSON chứa thông tin xác thực
cred = credentials.Certificate('demontm-b4d91-firebase-adminsdk-w7byl-283e372f9a.json')

# Khởi tạo ứng dụng Firebase với xác thực
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://demontm-b4d91-default-rtdb.firebaseio.com/'
})

# Đối tượng tham chiếu đến Realtime Database
ref = db.reference('/ntm/khoacua')

# Dữ liệu để tải lên
data_to_upload = {'sate': 1}

# Sử dụng set để tải dữ liệu lên
ref.set(data_to_upload)
