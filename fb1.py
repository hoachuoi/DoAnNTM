from firebase import firebase
firebase = firebase.FirebaseApplication('https://demotaidulieu-default-rtdb.firebaseio.com/', None)


data_to_upload = {'key1': 'value1111', 'key2': 'value2'}

result = firebase.put('/h', 'your-node-name', data_to_upload)