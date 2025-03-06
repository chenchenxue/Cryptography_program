from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
counter = 0
while True:
    mode = input("請輸入工作模式(1.產生寄件者公私鑰 2.產生數位信封並加密文件 3:解密文件 4:退出程式):")
    if mode == "1":
        accept_eth_k = generate_eth_key()
        accept = input("請輸入收件者名稱：")
        key = get_random_bytes(16)
        #print(key)
        keyPath = "AES_key.bin"                                          #金鑰儲存位置
        with open(keyPath, "wb") as f:                                   #儲存金鑰
            f.write(key)
        #收件者方資料
        accept_sk_hex = accept_eth_k.to_hex()                            # 收件者私鑰 
        accept_pk_hex = accept_eth_k.public_key.to_hex()                 # 收件者公鑰
        #處理收件者ECC私鑰
        f = open("{}_ECC_accept_secret_key.pem".format(accept),'wt')     #儲存收件者ECC私鑰
        f.write(accept_sk_hex)
        f.close()
        #處理收件者ECC公鑰
        f = open("{}_ECC_accept_public_key.pem".format(accept),'wt')     #儲存收件者ECC公鑰
        f.write(accept_pk_hex)
        f.close()  
    if mode == "2":
        user = str(input("請輸入收件者名稱："))
        file = str(input("輸入檔案名稱(限.txt檔)："))
        with open("{}.txt".format(file),"rb") as ouo:                    #讀取要加密的文件
            data = ouo.read()
        print("要加密的文字為：",data)
        keyPath = "AES_key.bin"                                          #金鑰儲存位置
        with open(keyPath,"rb") as f:
            AES_key =f.read()
        #print(AES_key)
        cipher = AES.new(AES_key, AES.MODE_CBC)                          #以金鑰搭配CBC模式建立cipher物件
        cipheredData = cipher.encrypt(pad(data, AES.block_size)) #加密
        #print(cipheredData)
        outputFile = 'AES_encrypted_text.bin'                            #輸出的加密檔案名稱
        with open(outputFile, "wb") as f:
            f.write(cipher.iv)
            f.write(cipheredData)
        print("加密的檔案已轉存到{}>>>>>".format(outputFile))
        f = open("{}_ECC_accept_public_key.pem".format(user),'rt+')      #儲存收件者ECC公鑰
        send_public_key = f.read()
        f.close()
        with open("AES_key.bin","rb") as ouo:                            #讀取AES金鑰
            AES_key = ouo.read()
        #print(AES_key)
        encrypt_text = encrypt(send_public_key,AES_key)                  #已加密的AES金鑰
        #print(encrypt_text)
        AES_encrypt_outputFile = 'encrypted_AES_key.bin'
        f = open(AES_encrypt_outputFile,'wb')                            #儲存收件者加密後ECC公鑰
        f.write(encrypt_text)
        f.close()
        print("加密的AES金鑰檔已轉存到>>>>>{}".format(AES_encrypt_outputFile))
    if mode == "3":
        inputFile = input("輸入加密後的AES金鑰bin檔：")
        #inputFile = 'encrypted_AES_key.bin'                             #加密後AES金鑰檔
        with open(inputFile,"rb") as ouo:                                #讀取加密AES金鑰
            encrypt_text = ouo.read()
        #儲存收件者ECC私鑰
        with open("{}_ECC_accept_secret_key.pem".format(user),'rt') as owo:
            ECC_secret_key = owo.read()
        decrypt_text=decrypt(ECC_secret_key,encrypt_text)
        #print(decrypt_text)
        inputFile = 'AES_encrypted_text.bin'
        with open(inputFile, "rb") as f:
            iv = f.read(16)                                              #讀取 16 位元組的初始向量
            cipheredData = f.read()                                      #讀取其餘的密文
        cipher = AES.new(decrypt_text, AES.MODE_CBC, iv=iv)
        originalData = unpad(cipher.decrypt(cipheredData), AES.block_size)
        print("解開的密文為：",originalData)
        f = open("decrypt_text.txt",'w+')                                #儲存解密後文件
        output = originalData.decode('utf-8')
        f.write(output)
        f.close()
        print("解開的密文已轉存到>>>>>decrypt.txt")
    if mode == "4" :
        print("~感謝使用~")
        break
    if counter == 3 :
        print("~你484眼瞎ㄌOuO~")
        print("~感謝使用~")
        break
    
    