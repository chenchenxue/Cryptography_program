from Crypto.PublicKey import ECC
from cryptography.fernet import Fernet
key = ECC.generate(curve='P-384')
#user = str(input("請輸入使用者名稱："))
user = "薛辰辰"
keyPath_private = '{}_private_key.pem'.format(user)
keyPath_public = '{}_public_key.pem'.format(user)

f = open(keyPath_private,'wt')
f.write(key.export_key(format='PEM'))
f.close()

f = open(keyPath_public,'wt')
f.write(key.public_key().export_key(format='PEM'))
f.close()

private_key = key.export_key(format='PEM')              #私鑰
public_key = key.public_key().export_key(format='PEM')  #公鑰
print(private_key)
print(public_key)

