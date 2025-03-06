from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# 輸入的加密檔案名稱
inputFile = 'encrypted_text.bin'
key = b'\xea\xc5\xf4\x12sB\xba\xc5\xe1\xd4\xa4(\xcd\x9e0A'

# 從檔案讀取初始向量與密文
with open(inputFile, "rb") as f:
    iv = f.read(16)         # 讀取 16 位元組的初始向量
    cipheredData = f.read() # 讀取其餘的密文

# 以金鑰搭配 CBC 模式與初始向量建立 cipher 物件
cipher = AES.new(key, AES.MODE_CBC, iv=iv)

# 解密後進行 unpadding
originalData = unpad(cipher.decrypt(cipheredData), AES.block_size)

# 輸出解密後的資料
print("解開的密文為：",originalData)