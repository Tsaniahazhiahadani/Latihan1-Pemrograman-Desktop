def luas_segitiga(alas,tinggi):
    return alas*tinggi/2
def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1+sisi2+sisi3
def menu():
    print ("1. Luas Segitiga")
    print ("2. Keliling Segitiga")
    pilih = int(input("Masukkan angka pilihan="))
    if pilih==1:
        alas=int(input("Masukkan alas="))
        tinggi=int(input("Masukkan tinggi="))
        print ("Luas segitiga =",luas_segitiga(alas,tinggi))
    elif pilih==2:
        sisi1=int(input("Masukkan sisi1="))
        sisi2=int(input("Masukkan sisi2="))
        sisi3=int(input("Masukkan sisi3="))
        print ("Keliling segitiga =",keliling_segitiga(sisi1, sisi2, sisi3))
    else:
        print ("Tidak ada pilihan")
menu()
