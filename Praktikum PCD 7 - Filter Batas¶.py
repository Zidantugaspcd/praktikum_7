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
        b1 = kolom # menyatakan baris  ke variabel a1 
        
        arr = np.array([copycat[a1-1, b1-1], copycat[a1-1, b1], copycat[a1, b1+1], \
            copycat[a1, b1-1], copycat[a1, b1+1], copycat[a1+1, b1-1],  \
            copycat[a1+1, b1], copycat[a1+1, b1+1]])
        # menentukan arr sebagai inisialisasi dari tiap piksel tetangga a1 dan b1 pada array copycat
        
        minPiksel = np.amin(arr);  # Menghitung nilai minimum (piksel terkecil) dalam array arr menggunakan fungsi np.amin() dari NumPy
        maksPiksel = np.amax(arr);  # Menghitung nilai maksimum (piksel terbesar) dalam array arr menggunakan fungsi np.amax() dari NumPy
            
        if copycat[baris, kolom] < minPiksel : # Memeriksa apakah nilai elemen copycat[baris, kolom] kurang dari minPiksel
            output1[baris, kolom] = minPiksel # jika nilai elemen copycat[baris, kolom] lebih kecil dari minPiksel, maka elemen output1[baris, kolom] akan diassign nilainya menjadi minPiksel
        else : # jika nilai elemen copycat[baris, kolom] tidak kurang dari minPiksel, maka
            if copycat[baris, kolom] > maksPiksel : # Memeriksa apakah nilai elemen copycat[baris, kolom] lebih besar dari maksPiksel.
                output1[baris, kolom] = maksPiksel # jika nilai elemen copycat[baris, kolom] lebih besar dari maksPiksel, maka elemen output1[baris, kolom] akan diassign nilainya menjadi maksPiksel
            else : #Jika nilai elemen copycat[baris, kolom] tidak lebih besar dari maksPiksel, maka
                output1[baris, kolom] = copycat[baris, kolom]# ika nilai elemen copycat[baris, kolom] tidak lebih kecil dari minPiksel dan tidak lebih besar dari maksPiksel, maka elemen output1[baris, kolom] akan diassign nilainya menjadi copycat[baris, kolom]

for baris1 in range(0, m2-1): # melakukan perulangan setiap baris matriks
    for kolom1 in range(0, n2-1): # Melakukan perulangan untuk setiap kolom pada matriks
        
        a1 = baris1 # menyatakan baris  ke variabel a1
        b1 = kolom1 # menyatakan baris  ke variabel a1
        
        arr = np.array([copykktua[a1-1, b1-1], copykktua[a1-1, b1], copykktua[a1, b1+1], \
            copykktua[a1, b1-1], copykktua[a1, b1+1], copykktua[a1+1, b1-1],  \
            copykktua[a1+1, b1], copykktua[a1+1, b1+1]])
        # menentukan arr sebagai inisialisasi dari tiap piksel tetangga a1 dan b1 pada array copycat

        minPiksel = np.amin(arr);  # Menghitung nilai minimum (piksel terkecil) dalam array arr menggunakan fungsi np.amin() dari NumPy     
        maksPiksel = np.amax(arr);  # Menghitung nilai maksimum (piksel terbesar) dalam array arr menggunakan fungsi np.amax() dari NumPy
            
        if copykktua[baris1, kolom1] < minPiksel :# Memeriksa apakah nilai elemen copycat[baris, kolom] kurang dari minPiksel
            output2[baris1, kolom1] = minPiksel# jika nilai elemen copycat[baris, kolom] lebih kecil dari minPiksel, maka elemen output1[baris, kolom] akan diassign nilainya menjadi minPiksel
        else :# jika nilai elemen copycat[baris, kolom] tidak kurang dari minPiksel, maka
            if copykktua[baris1, kolom1] > maksPiksel :# Memeriksa apakah nilai elemen copycat[baris, kolom] lebih besar dari maksPiksel.
                output2[baris1, kolom1] = maksPiksel # jika nilai elemen copycat[baris, kolom] lebih besar dari maksPiksel, maka elemen output1[baris, kolom] akan diassign nilainya menjadi maksPiksel
            else : #Jika nilai elemen copycat[baris, kolom] tidak lebih besar dari maksPiksel, maka
                output2[baris1, kolom1] = copykktua[baris1, kolom1]# ika nilai elemen copycat[baris, kolom] tidak lebih kecil dari minPiksel dan tidak lebih besar dari maksPiksel, maka elemen output1[baris, kolom] akan diassign nilainya menjadi copycat[baris, kolom]

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

plt.show()# tampilka