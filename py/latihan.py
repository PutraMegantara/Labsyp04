List_nilai = [2, 4, 8, 16, 32]
print('List_nilai:',[2, 4, 8, 16, 32])

#Akses List_nilai
print("Akses List_nilai")
Data1 = List_nilai[2]
Data2 = List_nilai[1:4]
Data3 = List_nilai[-1]
print(Data1)
print(Data2)
print(Data3)

#Ubah Elemen List
print("Ubah Elemen List_nilai")
print(List_nilai)
List_nilai[4] = 80
print(List_nilai)
List_nilai [4:5] = [64, 128]
print(List_nilai)

#Menambahkan Elemen List
print("Menambahkan Elemen List_nilai")
print(List_nilai)
a = List_nilai
print(a)
b = a[2:4]
print(b)
b.append(64)
b.extend([128, 256, 512])
print(b)
c = a + b
a.extend(b)
print(c)
