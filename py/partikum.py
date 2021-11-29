print("\t\tProgram Menghitung Nilai Akhir Siswa\t\t")

NSL=[]
NIML=[]
NTSL=[]
NUTSL=[]
NUASL=[]
NAL=[]
KetL=[]
totNA, totNB, totNC, totND, totNE=0,0,0,0,0
jawab="y"
while jawab=='y':

    NS=input("Nama Siswa : ")
    NIM=input("NIM Siswa : ")
    TUGAS=float(input("Nilai Tugas : "))
    UTS=float(input("Nilai UTS : "))
    UAS=float(input("Nilai UAS : "))
    nilai=float(TUGAS)*30/100 + (UTS)*35/100 + (UAS)*35/100

    if nilai<55:
        ket="E"
        totNE +=1
    elif 55<=nilai and nilai<60:
        ket="D"
        totND +=1
    elif 60<=nilai and nilai<70:
        ket="C"
        totNC +=1
    elif 70<=nilai and nilai<80:
        ket="B"
        totNB +=1
    else:
        ket="A"
        totNA +=1

    NSL.append(NS)
    NIML.append(NIM)
    NTSL.append(TUGAS)
    NUTSL.append(UTS)
    NUASL.append(UAS)
    NAL.append(nilai)
    KetL.append(ket)
    
    jawab = input("Ingin menambah data(y/t)? ")

    if jawab=="t":
        break

print(75*"=")
print("|","NO.","|","NAMA SISWA","|","NIM","|","TUGAS","|","UTS ","|","UAS","|","NIlAI AKHIR","|"," KETERANGAN","|")
print(75*"=")

for j in range(len(NSL)):

 print("|",j+1,"|",NSL[j],"|",NIML[j],"|",NTSL[j],"|",NUTSL[j],"|",NUASL[j],"|", NAL[j],"|",KetL[j],"|")
print(75*"=")
print()
