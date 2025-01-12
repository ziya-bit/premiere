import secretcode

user={
secretcode.encrypt("admin1", 132):secretcode.encrypt("123", 132),secretcode.encrypt("admin2", 132):secretcode.encrypt("456", 132),secretcode.encrypt("admin3", 132):secretcode.encrypt("789", 132)
}

def login():
    inputuser=input("masukkan username: ")
    inputpass=input("masukkan password: ")
    inputpass=secretcode.encrypt(inputpass, 132)
    inputuser=secretcode.encrypt(inputuser, 132)
    useronly=user.keys()
    passonly=user[inputuser]
    # print(inputuser in useronly, inputpass in passonly)
    if (inputuser in useronly) and (inputpass in passonly):
        print("login berhasil")
        return True
    else:
        print("login gagal")
        return False