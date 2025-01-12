# message=input("masukkan pesan rahasiamu: ")
# # secret=""
# key=int(input("masukkan secret-key mu(input ini wajib angka): "))
def encrypt(message:str, key: int):
    jawa=1
    result=''
    for i in message:
        jawa+=1
        gritrod=(ord(i)+(key*jawa)%15000)
        result+=(chr(gritrod))
    return result
    
def decrypt(mail:str, key:int):
    # print()
    # mail=input('masukkan pesan yang diterima untuk dekripsiasi: ')
    # key=int(input("masukkan secret-key mu(input ini wajib angka): "))
    jawa=1
    result=""
    for i in mail:
        jawa+=1
        gritrod=(ord(i)-(key*jawa)%15000)   
        # print(chr(gritrod),end="")
        result+= chr(gritrod)
    return result
# encrypt("123", 145)
# decrypt("œǥɷ", 145)