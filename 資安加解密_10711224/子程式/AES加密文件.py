from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
with open("test_text.txt","rb") as ouo:  #讀取要加密的文件
    data = ouo.read()
print(data)
keyPath = "AES_key.bin"                  #金鑰儲存位置
with open(keyPath,"rb") as f:
    AES_key =f.read()
print(AES_key)
cipher = AES.new(AES_key, AES.MODE_CBC)  #以金鑰搭配CBC模式建立cipher物件
cipheredData = cipher.encrypt(pad(data, AES.block_size)) #加密
print(cipheredData)
outputFile = 'AES_encrypted_text.bin'    #輸出的加密檔案名稱
with open(outputFile, "wb") as f:
    f.write(cipher.iv)
    f.write(cipheredData)