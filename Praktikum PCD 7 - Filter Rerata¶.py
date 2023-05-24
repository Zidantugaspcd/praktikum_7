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

fig, axes = plt.subplots(1, 2, figsize=(10, 10))# buat subplot yang terdiri dari 2 gambar dan ukuran 10 x 10
ax = axes.ravel() # buat perintah ravel untuk memposisikan kordinat tiap urutan gambar

ax[0].imshow(cat, cmap = 'gray')# ax 0 diisi dengan image cat grayscale
ax[0].set_title("Citra 1")# dibuat title cat sebagai citra 1
ax[1].imshow(kktua, cmap = 'gray')# ax 1 diisi dengan image kakatua grayscale
ax[1].set_title("Citra 2")# dibuat title cat sebagai citra 2

plt.show()# tampilkan

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

for baris in range(0, m1-1): #dibuat looping untuk iterasi setiap nomor baris dalam rentang 0 sampai m1-1
    for kolom in range(0, n1-1):#Loop ini akan mengiterasi melalui setiap nomor kolom dalam rentang dari 0 hingga n1-1.
        a1 = baris # buat  a1 sebagai variabel baris
        b1 = kolom  # buat  b1 sebagai variabel kolom
        # tiap matrix tetanga dari matriks copycat dijulahakn dengan indeks a1 dan b1 sebagai inisial kolom dan baris tiap matrix
        jumlah = copycat[a1-1, b1-1] + copycat[a1-1, b1] + copycat[a1-1, b1-1] + \
                 copycat[a1, b1-1] + copycat[a1, b1] + copycat[a1, b1+1] + \
                 copycat[a1+1, b1-1] + copycat[a1+1, b1] + copycat[a1+1, b1+1];   #tiap inisialisasi nilai a1 dan b1 matrix tetangga
        output1[a1, b1] = (1/9 * jumlah) #Nilai di output1[a1, b1] diatur sebagai rata-rata (1/9 * jumlah) dari nilai tetangga.

for baris1 in range(0, m2-1):# dibuat looping untuk iterasi setiap nomor baris dalam rentang 0 sampai m2-1
    for kolom1 in range(0, n2-1): #Loop ini akan mengiterasi melalui setiap nomor kolom dalam rentang dari 0 hingga n2-1.
        a2 = baris1 # buat  a2 sebagai variabel baris
        b2 = kolom1 # buat  b2 sebagai variabel kolom
        # tiap matrix tetanga dari matriks copycat dijulahakn dengan indeks a1 dan b1 sebagai inisial kolom dan baris tiap matrix
        jumlah = copykktua[a2-1, b2-1] + copykktua[a2-1, b2] + copykktua[a2-1, b2-1] + \
                 copykktua[a2, b2-1] + copykktua[a2, b2] + copykktua[a2, b2+1] + \
                 copykktua[a2+1, b2-1] + copykktua[a2+1, b2] + copykktua[a2+1, b2+1];  #tiap inisialisasi nilai a2 dan b2 matrix tetangga
        output2[a2, b2] = (1/9 * jumlah) #Nilai di output1[a1, b1] diatur sebagai rata-rata (1/9 * jumlah) dari nilai tetangga.

fig, axes = plt.subplots(2, 2, figsize=(10, 10))# buat figur untuk subplot dengan ukuran 10x 10 berisi 4 buah plot dengan posisi 2 kolom 2 baris
ax = axes.ravel() # buat perintah ravel untuk urutan plot

ax[0].imshow(cat, cmap = 'gray')# ax 0 untuk menampilkan gambar cat
ax[0].set_title("Input Citra 1")# beri title

ax[1].imshow(kktua, cmap = 'gray')# ax 1 untuk menampilkan gambar kakatua
ax[1].set_title("Input Citra 1") # beri title

ax[2].imshow(output1, cmap = 'gray')#ax 2 untuk menampilkan hasil gambar output 1
ax[2].set_title("Output Citra 1")# beri title

ax[3].imshow(output2, cmap = 'gray')#ax 3 untuk menampilkan hasil gambar output 2
ax[3].set_title("Output Citra 2")# beri title

plt.show()# tampilkan


