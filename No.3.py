print("MENENTUKAN MASSA BADAN")
T= float(input("Masukkan tinggi badan anda=  "))
B= float(input("Masukkan berat badan anda=  "))
Tinggi=T/100.00
BMI=(B/(Tinggi*Tinggi))
           
if BMI<=18.5:
    print ("Berat badan kurang")
elif BMI >=18.5 and BMI <=22.9:
    print ("Berat badan normal")
elif BMI >=23 and BMI <=29.9:
    print ("Berat badan berlebih(kecenderungan obesitas)")
else:
    print ("Obesitas")
