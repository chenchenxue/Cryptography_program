from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
accept_eth_k = generate_eth_key()
accept = input("輸入收件者名稱：")
key = get_random_bytes(32)
print(key)
keyPath = "AES_key.bin"                  #金鑰儲存位置
with open(keyPath, "wb") as f:           #儲存金鑰
    f.write(key)
#收件者方資料
accept_sk_hex = accept_eth_k.to_hex()                            # hex string # 收件者私鑰 
accept_pk_hex = accept_eth_k.public_key.to_hex()                 # hex string # 收件者公鑰
#處理收件者ECC私鑰
f = open("{}_ECC_accept_secret_key.pem".format(accept),'wt')     #儲存收件者ECC私鑰
f.write(accept_sk_hex)
f.close()
#處理收件者ECC公鑰
f = open("{}_ECC_accept_public_key.pem".format(accept),'wt')     #儲存收件者ECC公鑰
f.write(accept_pk_hex)
f.close()