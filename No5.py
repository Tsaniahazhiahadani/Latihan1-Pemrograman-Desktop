Username="Tsania"
Password="tsania321"
i=0
while True:
    Name=input("Masukkan username= ")
    if Name == Username:
        break
    else:
        print("Username invalid")
while i <= 3:
    Pswd=input("Masukkan password= ")
    if Pswd==Password:
        print("Anda berhasil login")
        break
    else:
        print("Password salah")
    i += 1
    if i == 3:
        print ("Anda salah memasukkan password sebanyak tiga kali,silahkan coba lagi nanti")
        break
