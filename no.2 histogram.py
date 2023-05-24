# memanggil modul yang diperlukan
import cv2 # import library cv2
import numpy as np # import library numpy
from matplotlib import pyplot as plt # import library matplotlib
#jika menggunakan google colab jgn lupa load code di bawah ini
#bgr
nisan= plt.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\R34.jpg") # import gambar dari file direktori
# membuat filter: matriks berukuran 5 x 5 
kernel = np.ones((5,5),np.float32)/25
print(kernel)# print hasil kernel
# lakukan filtering

nissan_Averaging = cv2.filter2D(nisan,-1,kernel) # nissan averaging filtering
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) # bbuat subplot pada figur dengan ukuran 12x 12 1 baris 3 kolom
ax = axes.ravel()# buat fungsi ax untuk kordinat plot
ax[0].imshow(nisan)# tampilkan citra asli
ax[0].set_title("Citra nissan") # buat tittle untuk gambar  kucing raksasa
ax[1].hist(nisan.ravel(), bins=256) # buat histogramnya
ax[1].set_title('Histogram nissan') # buat histogram nissan
ax[2].imshow(nissan_Averaging)# tampilkan gambar Citra Kucing Raksasa filter
ax[2].set_title("Citra nissan Averaging") # buat tittle Citra Kucing Raksasa Averaging
ax[3].hist(nissan_Averaging.ravel(), bins=256) # buat histogramnya
ax[3].set_title('Histogram nissan Averaging') # buat histogram nissan
kernel = np.matrix([ #
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]         
          ])/40
print(kernel)

# buat lagi filteringnya
nissan_filter2 = cv2.filter2D(nisan,-1,kernel)
nissan_Averaging = cv2.filter2D(nisan,-1,kernel)
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) # bbuat subplot pada figur dengan ukuran 12x 12 1 baris 3 kolom
ax = axes.ravel()# buat fungsi ax untuk kordinat plot
ax[0].imshow(nisan)# tampilkan citra asli
ax[0].set_title("Citra nissan") # buat tittle untuk gambar  nissann
ax[1].hist(nisan.ravel(), bins=256) # buat histogramnya
ax[1].set_title('Histogram nissan') # buat histogram nissan


plt.show()# tampilkan

#========================================================================================================================

# memanggil citra sebagai grayscale (argument 0)
nissan = plt.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\Bubble cat.jpg") # import gambar dari file direktori
giantcat = cv2.cvtColor(nissan, cv2.COLOR_BGR2RGB)# ubah citra menjadi rgb

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(nissan,cv2.CV_64F)

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(nissan,cv2.CV_64F,1,0,ksize=5)# sobel untuk sumbu x
sobely = cv2.Sobel(nissan,cv2.CV_64F,0,1,ksize=5)# sobel untuk sumbu y

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra 
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting 
plt.rcParams["figure.figsize"] = (20,20)# 


# menampilkan hasil filter
plt.subplot(2,2,1),plt.imshow(nissan,cmap = 'gray')#tampilkan gambar citra asli 
plt.title('Original'), plt.xticks([]), plt.yticks([])# buat tittle untuk gambar original
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')# buat subplot ubtuk gambar laplacian
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])# buat tittle untuk laplacian
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')# buat subplot untuk gambar soble x
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])# buat tittle untuk sobelx
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')# buat subplot untuk menampilkan gambar sobel y
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])# buat tittle untuk sobel  y
# Plot!import cv2

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(nissan,45,80)
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) # bbuat subplot pada figur dengan ukuran 12x 12 1 baris 3 kolom
ax = axes.ravel()# buat fungsi ax untuk kordinat plot

ax[0].imshow(nissan,cmap = 'gray')# subplot image asli
ax[0].set_title('Original Image')# tittle original
ax[1].hist(nissan.ravel(), bins=256) # buat histogramnya
ax[2].imshow(edges,cmap = 'gray')# subplot image asli
ax[2].set_title('Edge Image')# tittle edge image
ax[3].hist(nissan.ravel(), bins=256) # buat histogramnya

# Hitungan threshold. 
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi 
# yang diberikan
ret,thresh1 = cv2.threshold(nissan,127,255,cv2.THRESH_BINARY) # buat perintah untuk mengubah gambar menjadi thresh binary
ret,thresh2 = cv2.threshold(nissan,127,255,cv2.THRESH_BINARY_INV) # buat perintah untuk mengubah gambar menjadi thtesh binary inv
ret,thresh3 = cv2.threshold(nissan,127,255,cv2.THRESH_TRUNC) # buat perintah untuk mengubah gambar menjadi thresh trunc
ret,thresh4 = cv2.threshold(nissan,127,255,cv2.THRESH_TOZERO) # buat perintah untuk mengubah gambar menjadi thresh tozero
ret,thresh5 = cv2.threshold(nissan,127,255,cv2.THRESH_TOZERO_INV) # buat perintah untuk mengubah gambar menjadi thresh tozero inv

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'] # buat tittle untuk tiap gambar
images = [nissan, thresh1, thresh2, thresh3, thresh4, thresh5]# masukan seluruh gabar pada 1 variabel
# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(nissan,45,80)
fig, axes = plt.subplots(6, 2, figsize=(12, 12)) # bbuat subplot pada figur dengan ukuran 12x 12 1 baris 3 kolom
ax = axes.ravel()# buat fungsi ax untuk kordinat plot
ax[0].imshow(nissan,cmap = 'gray')# subplot image asli
ax[0].set_title('Original Image')# tittle original
ax[1].hist(nissan.ravel(), bins=256) # buat histogramnya 
ax[2].imshow(thresh1,cmap = 'gray')# subplot thresh1
ax[2].set_title('thresh1 Image')# tittle thresh1 image
ax[3].hist(thresh1.ravel(), bins=256) # buat histogramnya
ax[4].imshow(thresh2,cmap = 'gray')# subplot thresh2
ax[4].set_title('thresh2 Image')# tittle thresh2
ax[5].hist(thresh2.ravel(), bins=256) # buat histogramnya
ax[6].imshow(thresh3,cmap = 'gray')# subplot thresh3
ax[6].set_title('thresh3 Image')# tittle thresh3 image
ax[7].hist(thresh3.ravel(), bins=256) # buat histogramnya
ax[8].imshow(thresh4,cmap = 'gray')# subplot thresh4
ax[8].set_title('thresh4 Image')# tittle thresh4 image
ax[9].hist(thresh4.ravel(), bins=256) # buat histogramnya
ax[10].imshow(thresh5,cmap = 'gray')# subplot thresh5
ax[10].set_title('thresh5 Image')# tittle thresh5 image
ax[11].hist(thresh5.ravel(), bins=256) # buat histogramnya

# digunakan median blur untuk menghaluskan tepi objek pada citra
nisangray= cv2.cvtColor(nisan, cv2.COLOR_BGR2GRAY)# ubah citra menjadi rgb

# ini diperlukan agar thresholding memberikan hasil lebih baik
nisangray = cv2.medianBlur(nisangray,5)

# Lakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(nisangray,127,255,cv2.THRESH_BINARY)# Binary Threshold

th2 = cv2.adaptiveThreshold(nisangray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)# Adaptive Threshold dengan Mean


th3 = cv2.adaptiveThreshold(nisangray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)# Adaptive Threshold dengan Gaussian

# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [nisangray, th1, th2, th3]

fig, axes = plt.subplots(4, 2, figsize=(12, 12)) # bbuat subplot pada figur dengan ukuran 12x 12 1 baris 3 kolom
ax = axes.ravel()# buat fungsi ax untuk kordinat plot
ax[0].imshow(nisangray,cmap = 'gray')# subplot image asli
ax[0].set_title('Original Image')# tittle original
ax[1].hist(nisangray.ravel(), bins=256) # buat histogramnya 

ax[2].imshow(th1,cmap = 'gray')# subplot thresh1
ax[2].set_title('th1 Image')# tittle thresh1 image
ax[3].hist(th1.ravel(), bins=256) # buat histogramnya

ax[4].imshow(th2,cmap = 'gray')# subplot thresh2
ax[4].set_title('thresh2 Image')# tittle thresh2
ax[5].hist(th2.ravel(), bins=256) # buat histogramnya

ax[6].imshow(th3,cmap = 'gray')# subplot thresh3
ax[6].set_title('thresh3 Image')# tittle thresh3 image
ax[7].hist(th3.ravel(), bins=256) # buat histogramnya
plt.show()# tampilkan
