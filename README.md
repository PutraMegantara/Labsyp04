#### Labspy04

### Program Latihan 

   <p> Program sederhana untuk menambahkan data kedalam sebuah list 

   ### Penjelasan:
### List
     • Membuat list
       sebuah list didefinisikan menggunakan tanda kurung siku ([])
   ![1](https://user-images.githubusercontent.com/92736847/143836737-bb59d15b-3764-4fe0-b755-abd64f8b28f7.png)
       
 ```bash
       # list kosong
         list_kosong = []
       # list yang berisi kumpulan integer
         list_nilai = [2, 4, 8, 16, 32]
       # list campuran berbagai tipe data
         list_jawaban = [50, 32.3, 'Hello',]    
 ```
    • Mengakses List
      Kita bisa menggunakan perintah print() untuk melihat isi dari sebuah list, baik secara menyeluruh maupun sebagian.
  ![1](https://user-images.githubusercontent.com/92736847/143836737-bb59d15b-3764-4fe0-b755-abd64f8b28f7.png)
      
```bash
   print('list_kosong:', list_kosong)
   print('list_nilai:', list_nilai)
   print('list_jawaban:', list_jawaban)
```
### List
    • Mengubah elemen list
      tipe data yang bersifat changable alias bisa diubah.
   ![Screenshot (63)](https://user-images.githubusercontent.com/92736847/143837110-99dd8527-b6a6-4d6c-8a72-4dec104baa07.png)
  
```bash
   print("Ubah Elemen List_nilai")
   print (List_nilai)
   List_nilai [4] = 80
   print (List_nilai)
   List_nilai [4:5] = [64, 128]
   print (List_nilai)
```
    • Menambah elemen list
      - Menambah data di belakang
        kita bisa menggunakan fungsi append(). Fungsi ini menerima satu parameter, yang mana parameter tersebut akan dimasukkan sebagai nilai baru pada list, dan nilai baru tersebut berada pada akhir item.
      - Menambah data di depan
        Selain fungsi append(), kita juga bisa menambahkan item ke dalam list dengan menggunakan fungsi insert().
   ![Screenshot (64)](https://user-images.githubusercontent.com/92736847/143837170-9a70bd8e-257a-4d3e-b83f-52f7003c8a10.png)

```bash
     print("Menambahkan Elemen List_nilai")
     print(List_nilai)
     a = List_nilai
     print(a)
     b = a[2:4]
     print(b)
     # tambahkan satu item ke elemen terakhir
     b.append(64)
     # tambahkan beberapa item ke elemen terakhir
     b.extend([128, 256, 512])
     print(b)
```
     • Menggabungkan list
```bash
     # gabungkan daftar a dan b ke c
     c = a + b
     # tambahkan beberapa item b ke dalam a
     a.extend(b)
     print(c)
```
![Screenshot (62)](https://user-images.githubusercontent.com/92736847/143837309-9c745623-db23-48bb-b5e8-240ab3918be3.png)

## Program Pratikum

![praktikumpy](https://user-images.githubusercontent.com/92736847/143838159-0053b4ab-7106-41d3-b794-597a9a8bf164.png)

### Penjelasan:

     1. Mendeklarasikan list
        NSL=[], NIML=[], NTSL=[], NUTSL=[], NUASL=[], NAL=[], KetL=[]
     2. Gunakan perulangan while loop dengan nilai "True"
        while True:
     3. Membuat inputan data
   ![INPUTAN DATA](https://user-images.githubusercontent.com/92736847/143839541-3e7c68b2-fc05-43be-898d-f62caf42380b.png)
     4. Membuat hasil inputan
   ![hasil inputan data](https://user-images.githubusercontent.com/92736847/143839846-4ac246bd-9e2e-4c47-aa27-5fba07028a87.png)
   
 # Hasilnya
 ![program mengitung](https://user-images.githubusercontent.com/92736847/143840001-45ffcfac-4928-4684-9a90-c084997d5b1c.png)

# flowchart
![flow chart](https://user-images.githubusercontent.com/92736847/143840209-016b1448-66d0-4cf4-a909-eb5bb61332f1.png)
