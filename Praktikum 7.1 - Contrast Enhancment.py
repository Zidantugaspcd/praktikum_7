#contrast enhancment
#import library
import numpy as np # import library numpy
import matplotlib.pyplot as plt# import library matplotlib.pyplot 
import cv2# import library cv2
import matplotlib.image as mpimg# import library matplotlib.image
from skimage import data# import library skimage

catori= cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\hoam.jpg") # import gambar dari file direktori
cat = cv2.cvtColor(catori, cv2.COLOR_BGR2GRAY) # mengubah gambar menjadi grayscale
cat_equalized = cv2.equalizeHist(cat) # membuat histogram Equalization berfungsi untuk mengingkatkan kontras gambar
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))# membuat CLAHE objek dengan batasan potong 2 dan ukuran grid 8x8
cat_clahe = clahe.apply(cat)# apply CLAHE cat pada variabel cat clahe

cat_cs = np.zeros((cat.shape[0],cat.shape[1]),dtype = 'uint8') # buat matriks kosong dengan ukuran sama dengan cat

min = np.min(cat)# buat nilai minimum gambar cat
max = np.max(cat)# buat nilai maximum gambar cat

for i in range(cat.shape[0]): # looping range matrik baris [i]
    for j in range(cat.shape[1]):# looping matriks kolom [j]
        cat_cs[i,j] = 255*(cat[i,j]-min)/(max-min)# untuk rentang 0-255 dibuat nilai intensistas setiap piksel cat

copycat = cat.copy().astype(float)# copy cat dengan astype float

m1,n1 = copycat.shape # copy juga dimensi matrix dari 
output1 = np.empty([m1, n1]) #membuat matriks kosong output1 dengan ukuran yang sama dengan gambar copyCamera

for baris in range(0, m1-1): # looping nilai baris dengan -1 
    for kolom in range(0, n1-1):# looping nilai kolom dengan -1
        a1 = baris #buat variabel ai untuk memuat baris matrix
        b1 = kolom # buat b1 untuk memuat kolom matrix
        output1[a1, b1] = copycat[baris, kolom] # simpan nilai ke output 1  
fig, axes = plt.subplots(5, 2, figsize=(20, 20)) # buat figur dengan subplot 5,2 dan size 20 x 20
ax = axes.ravel()# buat perintah ravel untuk memasukan posisi dari tiap plot

ax[0].imshow(cat, cmap=plt.cm.gray)# tampilkan gambar asli yang diubah ke grayscale pada posisi ax 0
ax[0].set_title("Citra Input")# buat title untuk plot ax 0
ax[1].hist(cat.ravel(), bins=256)# buat histogram pada ax 1
ax[1].set_title('Histogram Input')# buat tittle histogram gambar asli grayscale ax 1

ax[2].imshow(cat_equalized, cmap=plt.cm.gray)# tampilkan gambar equalized (HE)ax 2
ax[2].set_title("Citra Output HE")# title untuk HE ax2
ax[3].hist(cat_equalized.ravel(), bins=256)# buat histogram equalized pada ax 3
ax[3].set_title('Histogram Output HE Method')# buat title histogram  HE ax  3

ax[4].imshow(cat_cs, cmap=plt.cm.gray)# tampilkan gambar CSax 4
ax[4].set_title("Citra Output CS")# title gambar cs ax 4
ax[5].hist(cat_cs.ravel(), bins=256)# buat histogram CS ax 5
ax[5].set_title('Histogram Output CS Method')# buat title histogram CSax 5

ax[6].imshow(cat_clahe, cmap=plt.cm.gray)# tampilkan gambar clahe pada ax 6
ax[6].set_title("Citra Grayscale CLAHE")# title gambar clahe ax 6
ax[7].hist(cat_clahe.ravel(), bins=256)# tampilkan histogram clahe ax  7
ax[7].set_title('Histogram Output CLAHE Method')# ax buat title histogram clahe 7

ax[8].imshow(output1, cmap=plt.cm.gray)# tampilkan gambar hasil output 1ax 8
ax[8].set_title("Citra Grayscale Perkalian Konstanta")# ax buat title grayscale perkalian konstanta8
ax[9].hist(output1.ravel(), bins=256)#buat histogram untuk konstanta perkalian ax 9
ax[9].set_title('Histogram Output Perkalian Konstanta Method')# buat title histogram konstanta perkalian ax 9

fig.tight_layout()# ketebalan laout
plt.show()# tampilkan
