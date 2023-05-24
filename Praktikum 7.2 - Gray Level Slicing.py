import cv2 # import library cv2 
import numpy as np # import library numpy
from skimage import data# import library skimage
import matplotlib.pyplot as plt# import library matplotlib

catori= cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\hoam.jpg") # import gambar dari file direktori
cat = cv2.cvtColor(catori, cv2.COLOR_BGR2GRAY) # mengubah gambar menjadi grayscale
row, column = cat.shape # Mendapatkan jumlah baris dan kolom pada citra cat
cat1 = np.zeros((row,column),dtype = 'uint8') # Membuat array baru, cat1, dengan bentuk yang sama dengan cat, diisi dengan nol
 

min_range = 10 # Menentukan nilai batas minimum
max_range = 60 # Menentukan nilai batas maximum
 

for i in range(row):# membuat iterasi pada row atau baris matriks
    for j in range(column):# membuat iterasi pada column atau kolom
        if cat[i,j]>min_range and cat[i,j]<max_range: # Jika intensitas piksel berada dalam rentang yang ditentukan
            cat1[i,j] = 255 #atur piksel yang sesuai di cat1 menjadi 255 (putih)
        else:# Jika tidak
            cat1[i,j] = 0 #atur piksel tersebut menjadi 0 (hitam)

fig, axes = plt.subplots(2, 2, figsize=(12, 12)) # buat subplot figure untuk plot 4 buah plot dengan size 12x12
ax = axes.ravel() # perintah untuk memasukan kordinat urutan tiap plot dengan ax 

ax[0].imshow(cat, cmap=plt.cm.gray)# tampilkan gmabar cat grayscale
ax[0].set_title("Citra Input")# buat title bahwa cat adalah citra input atau asli
ax[1].hist(cat.ravel(), bins=256)# buat histogram
ax[1].set_title('Histogram Input')# buat tittle histogram

ax[2].imshow(cat1, cmap=plt.cm.gray)# tampikan hasil dari output grayscale dengan intensitas 0 dan 255
ax[2].set_title("Citra Output")# buat tittle
ax[3].hist(cat1.ravel(), bins=256)# tampilkan histogram
ax[3].set_title('Histogram Output')# buat tittle histogram

plt.show()# tampilkan