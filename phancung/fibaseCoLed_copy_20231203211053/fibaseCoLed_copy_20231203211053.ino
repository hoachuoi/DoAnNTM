#include <Servo.h>


#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>

// Provide the token generation process info.
#include <addons/TokenHelper.h>

// Provide the RTDB payload printing info and other helper functions.
#include <addons/RTDBHelper.h>

/* 1. Define the WiFi credentials */
#define WIFI_SSID "baccc"
#define WIFI_PASSWORD "12345678"

// For the following credentials, see examples/Authentications/SignInAsUser/EmailPassword/EmailPassword.ino

/* 2. Define the API Key */
#define API_KEY "AIzaSyAsjhsNe7DYHpxJgHrdOYzsokn0_gHO03U"

/* 3. Define the RTDB URL */
#define DATABASE_URL "https://demontm-b4d91-default-rtdb.firebaseio.com" //<databaseName>.firebaseio.com or <databaseName>.<region>.firebasedatabase.app

/* 4. Define the user Email and password that alreadey registerd or added in your project */
#define USER_EMAIL "nguyenxuanbac666rt@gmail.com"
#define USER_PASSWORD "bacdz2002"

// Define Firebase Data object
FirebaseData fbdo;

FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;


#if defined(ARDUINO_RASPBERRY_PI_PICO_W)
WiFiMulti multi;
#endif
int ledpn = D3;
int ledGas =D7;
int buzzer = D8;
int servo = D6;
Servo myServo;
int kt = 0, ktLedBep = 0, ktpn = 0, khoacua = 0, baoch =1, thuchay =0,cua=0;
void setup()
{

  Serial.begin(115200);
  pinMode(ledpn, OUTPUT);
  pinMode(D4 , OUTPUT);
  pinMode(A0, INPUT);
  pinMode(ledGas, OUTPUT);
  pinMode(buzzer, OUTPUT);
  digitalWrite(ledpn, LOW);
  myServo.attach(servo);
  myServo.write(180);


  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  unsigned long ms = millis();
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Serial.printf("Firebase Client v%s\n\n", FIREBASE_CLIENT_VERSION);

  /* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the user sign in credentials */
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; // see addons/TokenHelper.h

  // Comment or pass false value when WiFi reconnection will control by your code or third party library e.g. WiFiManager
  Firebase.reconnectNetwork(true);

  // Since v4.4.x, BearSSL engine was used, the SSL buffer need to be set.
  // Large data transmission may require larger RX buffer, otherwise connection issue or data read time out can be occurred.
  fbdo.setBSSLBufferSize(4096 /* Rx buffer size in bytes from 512 - 16384 */, 1024 /* Tx buffer size in bytes from 512 - 16384 */);

  // The WiFi credentials are required for Pico W
  // due to it does not have reconnect feature.



  Firebase.begin(&config, &auth);

  Firebase.setDoubleDigits(5);

 
}



void loop()
{

  // Firebase.ready() should be called repeatedly to handle authentication tasks.
     if (WiFi.status() == WL_CONNECTED) {
    // Nếu kết nối Wi-Fi thành công, nhấp LED mỗi giây
    digitalWrite(D4, HIGH);
    delay(200);
    digitalWrite(D4, LOW);
    delay(200);
  } else {
    // Nếu không kết nối Wi-Fi, nhấp LED 2 lần mỗi giây
      digitalWrite(D4, HIGH);
      delay(1500);
      digitalWrite(D4, LOW);
      delay(1500);
    }

    sendDataPrevMillis = millis();
    fbdo.clear();

    Serial.printf("Get phong ngu... %s\n", Firebase.getInt(fbdo, F("/ntm/ledpn")) ? String(fbdo.to<int>()).c_str() : fbdo.errorReason().c_str());
     if (Firebase.getInt(fbdo, F("/ntm/ledpn"))){
      ktpn = fbdo.to<int>();
    }
    Serial.printf("KT Phong ngu");
    Serial.println(ktpn);
    if( ktpn == 1){
      digitalWrite(ledpn, HIGH);
    } else{
      digitalWrite(ledpn, LOW);
    }
   

   
    
    


  //bao chay

  Serial.printf("Get bao chay... %s\n", Firebase.getInt(fbdo, F("/ntm/baochay")) ? String(fbdo.to<int>()).c_str() : fbdo.errorReason().c_str());
    if (Firebase.getInt(fbdo, F("/ntm/baochay"))){
      baoch = fbdo.to<int>();
    }
    Serial.printf("KT bao chay");
    Serial.println(baoch);


  int value = analogRead(A0);
  Serial.println(value);
  if (value >600 && baoch == 1)
  {
    
      for(int x = 0;x<180;x++)
      {
        digitalWrite(ledGas,HIGH);
        delay(50);

        digitalWrite(ledGas,LOW);
        delay(20);
        float sinVal  = (sin(x*(3.1412/180)));
        float toneVal = 2000 + (int(sinVal *1000));
        tone(buzzer,toneVal);
        delay(2);
      }
    
    delay(10);
  }
  else 
  {
    digitalWrite(ledGas,LOW);
    noTone(buzzer);
  }
  // thu bao chay
  Serial.printf("Get thu... %s\n", Firebase.getInt(fbdo, F("/ntm/thuchay")) ? String(fbdo.to<int>()).c_str() : fbdo.errorReason().c_str());
  if (Firebase.getInt(fbdo, F("/ntm/thuchay"))){
      thuchay = fbdo.to<int>();
    }
    Serial.printf("KT thu");
    Serial.println(thuchay);
  if (thuchay == 1)
  {
   
     for(int x = 0;x<180;x++)
      {
        digitalWrite(ledGas,HIGH);
        delay(50);

        digitalWrite(ledGas,LOW);
        delay(20);
        float sinVal  = (sin(x*(3.1412/180)));
        float toneVal = 2000 + (int(sinVal *1000));
        tone(buzzer,toneVal);
        delay(2);
      }
    
    delay(10);
  }
  else 
  {
    digitalWrite(ledGas,LOW);
    noTone(buzzer);
  }
  Serial.println();

  //dong mo cua

  Serial.printf("Get khoa cua... %s\n", Firebase.getInt(fbdo, F("/ntm/khoacua/state")) ? String(fbdo.to<int>()).c_str() : fbdo.errorReason().c_str());
    if (Firebase.getInt(fbdo, F("/ntm/khoacua/state"))){
      khoacua = fbdo.to<int>();
    }
    Serial.printf("KT khoa cua");
    Serial.println(khoacua);
    
    Serial.printf("Get dong mo cua... %s\n", Firebase.getInt(fbdo, F("/ntm/cua")) ? String(fbdo.to<int>()).c_str() : fbdo.errorReason().c_str());
  if (Firebase.getInt(fbdo, F("/ntm/cua"))){
     cua = fbdo.to<int>();
    }
    Serial.printf("Cua");
    Serial.println(cua);
    
    
    if(khoacua==1 || cua ==1){
    myServo.write(0);
    delay(1000);
   }
   else {
    myServo.write(180);
    }
}
