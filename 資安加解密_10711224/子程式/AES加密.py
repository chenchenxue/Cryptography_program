from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
#產生256位元金鑰（16位元組=128位元）
key = b'\xea\xc5\xf4\x12sB\xba\xc5\xe1\xd4\xa4(\xcd\x9e0A' #AES固定金鑰
#print(key)

keyPath = "AES_key.bin"                        #金鑰儲存位置
with open(keyPath, "wb") as f:                 #儲存金鑰
    f.write(key)

outputFile = 'encrypted_text.bin'              #輸出的加密檔案名稱
with open("test_text.txt","rb") as ouo:
    data = ouo.read()
print(data)

cipher = AES.new(key, AES.MODE_CBC)  #以金鑰搭配CBC模式建立cipher物件
cipheredData = cipher.encrypt(pad(data, AES.block_size)) #加密

print(cipheredData)
with open(outputFile, "wb") as f:
    f.write(cipher.iv)
    f.write(cipheredData)