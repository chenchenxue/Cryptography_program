from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

#用私鑰解密AES金鑰
user = "薛辰辰"
inputFile = 'encrypted_AES_text.bin'                   #加密AES金鑰

with open(inputFile,"rb") as ouo:                      #讀取AES金鑰
    encrypt_text = ouo.read()

#儲存收件者ECC私鑰
with open("{}_ECC_accept_secret_key.pem".format(user),'rt') as owo:
    ECC_secret_key = owo.read()

decrypt_text=decrypt(ECC_secret_key,encrypt_text)
print(decrypt_text)

inputFile = 'AES_encrypted_text.bin'

with open(inputFile, "rb") as f:
    iv = f.read(16)         # 讀取 16 位元組的初始向量
    cipheredData = f.read() # 讀取其餘的密文
    
cipher = AES.new(decrypt_text, AES.MODE_CBC, iv=iv)
originalData = unpad(cipher.decrypt(cipheredData), AES.block_size)
print("解開的密文為：",originalData)