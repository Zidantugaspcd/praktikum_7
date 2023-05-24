import matplotlib.pyplot as plt # import library matplotlib
from skimage import data # import library skimage
from skimage.io import imread # import library imread
from skimage.color import rgb2gray  # import library rgb2gray
import numpy as np # import library numpy
import cv2# import library cv2

catsamurai= cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\samuraicat.jpg") # import gambar dari file direktori
cat = cv2.cvtColor(catsamurai, cv2.COLOR_BGR2GRAY)# ubah citra catsamurai menjadi bentuk grayscale agar dapat dibaca oleh program
kktu= cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\kakatue.jpg") # import gambar dari file direktori
kktua = cv2.cvtColor(kktu, cv2.COLOR_BGR2GRAY)# ubah citra kakatua menjadi bentuk grayscale agar dapat dibaca oleh program
print('Shape citra 1 : ', cat.shape)# print nilai dimensi pada terminal
print('Shape citra 2 : ', kktua.shape)# print nilai dimensi pada terminal

copycat = cat.copy().astype(float) # salinan dari array cat dan mengubah tipe datanya menjadi float
copykktua = kktua.copy().astype(float) # salin array  dan diubah menjadi float type data

m1,n1 = copycat.shape # pisahkan dimensi dari kolom dan baris citra copycat 
output1 = np.empty([m1, n1]) # kosongkan nilai matriks

m2,n2 = copykktua.shape # buat dimensi menjadi terpisah antara kolom dan baris
output2 = np.empty([m2, n2]) # kosongkan matrix dari kktua

print('Shape copy citra 1 : ', copycat.shape) # print ke terminal dimensi copycat
print('Shape output citra 1 : ', output1.shape) # print dimensi output1

print('m1 : ',m1) # tentukan berapa nilai m1 (baris) dan tampilkan di terminal
print('n1 : ',n1) # tentukan berapa nilai n1 (kolom) dan tampilkan di terminal
print() # print

print('Shape copy citra 2 : ', copykktua.shape) # print ke terminal dimensi kktuacopy
print('Shape output citra 2 : ', output2.shape) # print dimensi output2
print('m2 : ',m2) # tentukan berapa nilai m2 (baris) dan tampilkan di terminal
print('n2 : ',n2) # tentukan berapa nilai n2 (kolom) dan tampilkan di terminal
print() # print

for baris in range(0, m1-1): # melakukan perulangan setiap baris matriks
    for kolom in range(0, n1-1): # Melakukan perulangan untuk setiap kolom pada matriks
        a1 = baris # menyatakan baris  ke variabel a1 
        b1 = kolom # menyatakan kolom ke variabel b1 
        dataA = [copycat[a1-1, b1-1], copycat[a1-1, b1], copycat[a1-1, b1+1], \
              copycat[a1, b1-1], copycat[a1, b1], copycat[a1, b1+1], \
              copycat[a1+1, b1-1], copycat[a1+1, b1], copycat[a1+1, b1+1]]
        # menentukan dataA sebagai inisialisasi dari tiap piksel tetangga a1 dan b1 pada matriks copycat
        # Urutkan
        for i in range(1, 8): # Melakukan perulangan dari 1 hingga 7
            for j in range(i, 9): # Melakukan perulangan dari i hingga 8
                if dataA[i] > dataA[j]: # Memeriksa apakah elemen dataA[i] lebih besar dari elemen dataA[j]
                    tmpA = dataA[i]; # Menyimpan nilai elemen dataA[i] ke dalam variabel sementara tmpA
                    dataA[i] = dataA[j]; # Memindahkan nilai elemen dataA[j] ke elemen dataA[i]
                    dataA[j]= tmpA; # Memindahkan nilai yang tersimpan dalam variabel sementara tmpA ke elemen dataA[j]
                    
        output1[a1, b1] = dataA[5] # digunakan untuk mengassign nilai elemen ke-5 dari dataA ke elemen output1 pada posisi [a1, b1].

for baris in range(0, m2-1):# melakukan perulangan setiap baris matriks
    for kolom in range(0, n2-1):  # Melakukan perulangan untuk setiap kolom pada matriks
        a1 = baris # menyatakan baris  ke variabel a1 
        b1 = kolom # menyatakan kolom ke variabel b1 
        dataA = [copykktua[a1-1, b1-1], copykktua[a1-1, b1], copykktua[a1-1, b1+1], \
              copykktua[a1, b1-1], copykktua[a1, b1], copykktua[a1, b1+1], \
              copykktua[a1+1, b1-1], copykktua[a1+1, b1], copykktua[a1+1, b1+1]]
        # menentukan dataA sebagai inisialisasi dari tiap piksel tetangga a1 dan b1 pada matriks kakatua
        
        # Urutkan
        for i in range(1, 8): # Melakukan perulangan dari 1 hingga 7
            for j in range(i, 9): # Melakukan perulangan dari i hingga 8
                if dataA[i] > dataA[j]: # Memeriksa apakah elemen dataA[i] lebih besar dari elemen dataA[j]
                    tmpA = dataA[i]; # Menyimpan nilai elemen dataA[i] ke dalam variabel sementara tmpA
                    dataA[i] = dataA[j]; # Memindahkan nilai elemen dataA[j] ke elemen dataA[i]
                    dataA[j]= tmpA; # Memindahkan nilai yang tersimpan dalam variabel sementara tmpA ke elemen dataA[j]
        
        output2[a1, b1] = dataA[5] # digunakan untuk mengassign nilai elemen ke-5 dari dataA ke elemen output1 pada posisi [a1, b1].

fig, axes = plt.subplots(2, 2, figsize=(10, 10))# buat figur yang barisi 4 buah plot dengan dimensi 2 baris 2 kolom dan ukuran 10 x 10
ax = axes.ravel() # buat ax sebagai identifikasi kordinat pada tiap plot

ax[0].imshow(copycat, cmap = 'gray') # tammpilkan gambar input 1 copycat
ax[0].set_title("Input Citra 1")# buat tittle

ax[1].imshow(copykktua, cmap = 'gray')# tampilkan gambar input 2 copykakatua
ax[1].set_title("Input Citra 2")# buat tittle

ax[2].imshow(output1, cmap = 'gray')# tampilkan hasil output 1
ax[2].set_title("Output Citra 1")# buat tittle untuk gambar output 1

ax[3].imshow(output2, cmap = 'gray')# # tampilkan hasil output 2
ax[3].set_title("Output Citra 2")# buat tittle untuk gambar output 2

plt.show()# tampilkan