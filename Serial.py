import serial
import binascii
import requests
import http.client
import urllib.parse
import urllib.request
import json

ser = serial.Serial("com3",115200,timeout=20)
ser.write("Debug".encode())
ser_str = ser.readline()
print(ser_str.decode("utf-8"))

# url = "http://183.134.109.181:8800/zhimakaimen_v2"
# payload = "{\n\t\"username\":\"linzhixin\",\n\t\"password\":\"LIN.SWE14058\",\n\t\"message\":\"AwAAAGTy+327tziwIxk=\"\n}"
# headers = {
#     'Content-Type': "application/json",
#     'User-Agent': "PostmanRuntime/7.11.0",
#     'Accept': "*/*",
#     'Host': "183.134.109.181:8800",
#     'accept-encoding': "gzip, deflate",
#     'content-length': "90",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache",
#     'Postman-Token': "151f35e6-a2ce-4c78-b057-50a6f7710d90"
#     }
# response = requests.request("POST", url, data=payload, headers=headers)
# response_encode = response.text.encode("utf-8")
# print(type(response_encode))
# ser.write(response_encode)



