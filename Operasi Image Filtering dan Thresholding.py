# LOW PASS FILTER
# memanggil modul yang diperlukan
import cv2 # import library open cv
import numpy as np # 
from matplotlib import pyplot as plt
#jika menggunakan google colab jgn lupa load code di bawah ini
#bgr
bigcat = plt.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\supergiantcutie cat.jpg") # import gambar dari file direktori
giantcat = cv2.cvtColor(bigcat, cv2.COLOR_BGR2RGB)# ubah citra menjadi rgb
# membuat filter: matriks berukuran 5 x 5 
kernel = np.ones((5,5),np.float32)/25
print(kernel)# print hasil kernel
# lakukan filtering
kucing_Averaging = cv2.filter2D(giantcat,-1,kernel)
fig, axes = plt.subplots(1, 2, figsize=(12, 12)) # bbuat subplot pada figur dengan ukuran 12x 12 1 baris 3 kolom
ax = axes.ravel()# buat fungsi ax untuk kordinat plot
ax[0].imshow(giantcat)# tampilkan citra asli
ax[0].set_title("Citra kucing raksasa") # buat tittle untuk gambar  kucing raksasa
ax[1].imshow(kucing_Averaging)# tampilkan gambar Citra Kucing Raksasa filter
ax[1].set_title("Citra Kucing Raksasa Averaging") # buat tittle Citra Kucing Raksasa Averaging
kernel = np.matrix([ # kernel matrix
          [2, 2, 2],# baris pertama matrix
          [2, 5, 2],# baris kedua matrix
          [2, 2, 2]  # baris kedua matrix       
          ])/30 # matriks di rata ratakan dan dibagi
print(kernel)# print nilai kernel

# buat lagi filteringnya
bigcat_filter2 = cv2.filter2D(bigcat,-1,kernel)
plt.imshow(bigcat_filter2)# tampilkan citra asli
plt.set_title("Citra bigcat") # buat tittle untuk gambar  bigcat

plt.show()# tampilkan


#===================================================================================================================
# Highpass Filter

import cv2# input library cv2
import numpy as np # import library numpy
from matplotlib import pyplot as plt # inport library matplotlib


# memanggil citra sebagai grayscale (argument 0)
bubblecat = plt.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\Bubble cat.jpg") # import gambar dari file direktori
giantcat = cv2.cvtColor(bubblecat, cv2.COLOR_BGR2RGB)# ubah citra menjadi rgb

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(bubblecat,cv2.CV_64F)

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(bubblecat,cv2.CV_64F,1,0,ksize=5)# sobel untuk sumbu x
sobely = cv2.Sobel(bubblecat,cv2.CV_64F,0,1,ksize=5)# sobel untuk sumbu y

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra 
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting 
plt.rcParams["figure.figsize"] = (20,20)# 


# menampilkan hasil filter
plt.subplot(2,2,1),plt.imshow(bubblecat,cmap = 'gray')#tampilkan gambar citra asli 
plt.title('Original'), plt.xticks([]), plt.yticks([])# buat tittle untuk gambar original
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')# buat subplot ubtuk gambar laplacian
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])# buat tittle untuk laplacian
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')# buat subplot untuk gambar soble x
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])# buat tittle untuk sobelx
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')# buat subplot untuk menampilkan gambar sobel y
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])# buat tittle untuk sobel  y
# Plot!import cv2
# memanggil citra sebagai grayscale (argument 0)
morning = plt.imread('D:\SEMESTER 6\Pengolahan Citra Digital\image\morning cat.jpg')
bubblecatgray = cv2.cvtColor(bubblecat, cv2.COLOR_BGR2GRAY)# ubah citra bgr ke rgbb

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(morning,100,200)

plt.subplot(121),plt.imshow(morning,cmap = 'gray') # tampilkan gambar morning cat
plt.title('Original Image'), plt.xticks([]), plt.yticks([])# buat title sabagai original image
plt.subplot(122),plt.imshow(edges,cmap = 'gray')#  tampilkan gambar edges 
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])#tampilkan titte edge image

# Hitungan threshold. 
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi 
# yang diberikan
ret,thresh1 = cv2.threshold(bubblecatgray,127,255,cv2.THRESH_BINARY) # buat perintah untuk mengubah gambar menjadi thresh binary
ret,thresh2 = cv2.threshold(bubblecatgray,127,255,cv2.THRESH_BINARY_INV) # buat perintah untuk mengubah gambar menjadi thtesh binary inv
ret,thresh3 = cv2.threshold(bubblecatgray,127,255,cv2.THRESH_TRUNC) # buat perintah untuk mengubah gambar menjadi thresh trunc
ret,thresh4 = cv2.threshold(bubblecatgray,127,255,cv2.THRESH_TOZERO) # buat perintah untuk mengubah gambar menjadi thresh tozero
ret,thresh5 = cv2.threshold(bubblecatgray,127,255,cv2.THRESH_TOZERO_INV) # buat perintah untuk mengubah gambar menjadi thresh tozero inv

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV'] # buat tittle untuk tiap gambar
images = [bubblecatgray, thresh1, thresh2, thresh3, thresh4, thresh5]# masukan seluruh gabar pada 1 variabel

# menampilkan beberapa gambar sekaligus
for i in range(6): # untuk 1 pada range 6
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray') # sublot untuk gambar 3 baris dan 2 kolom
    plt.title(titles[i]) # tampilkan tittle untuk plot
    plt.xticks([]),plt.yticks([]) # plot

# digunakan median blur untuk menghaluskan tepi objek pada citra
# ini diperlukan agar thresholding memberikan hasil lebih baik
bubblecatgray = cv2.medianBlur(bubblecatgray,5)

# Lakukan Thresholding

ret,th1 = cv2.threshold(bubblecatgray,127,255,cv2.THRESH_BINARY)# Binary Threshold

th2 = cv2.adaptiveThreshold(bubblecatgray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)# Adaptive Threshold dengan Mean


th3 = cv2.adaptiveThreshold(bubblecatgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)# Adaptive Threshold dengan Gaussian


# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding'] #dibuat tittle variabel
images = [bubblecatgray, th1, th2, th3] # buat variabel untuk gambar

# menampilkan hasil
for i in range(4):# untuk range foto 4
    plt.subplot(2,2,i+1)# plot dimensi 2x2 
    plt.imshow(images[i],'gray') # tampilkan gambar
    plt.title(titles[i])# tampilkan gambar
    plt.xticks([]),plt.yticks([]) # non aktifkan sumbu

plt.show()# tampilkan
