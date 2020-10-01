data = int(input("Berapa banyak list angka= "))
List=[]
for i in range(data):
    List.append(int(input("Masukkan angka ke{}= ".format(i))))
print('nilai terbesar pada list: {}'.format(max(List)))
print('nilai terkecil pada list: {}'.format(min(List)))
