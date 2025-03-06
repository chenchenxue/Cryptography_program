from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
#用收件者的公鑰加密AES金鑰
user = "薛辰辰"
f = open("{}_ECC_accept_public_key.pem".format(user),'rt')#儲存收件者ECC公鑰
send_public_key = f.read()
f.close()
with open("AES_key.bin","rb") as ouo:                #讀取AES金鑰
    AES_key = ouo.read()
print(AES_key)
encrypt_text = encrypt(send_public_key,AES_key)      #已加密的AES金鑰
print(encrypt_text)
AES_encrypt_outputFile = 'encrypted_AES_text.bin'
f = open(AES_encrypt_outputFile,'wb')                #儲存收件者加密後ECC公鑰
f.write(encrypt_text)
f.close()
