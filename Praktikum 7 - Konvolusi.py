import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np

import cv2

gate = plt.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\gate keeper kitsune.jpg") # import gambar dari file direktori
gategrayscale = cv2.cvtColor(gate, cv2.COLOR_BGR2GRAY) # ubah gambar ke dalam bentuk grayscale
print(gate.shape) # print dimnesi dari citra

kernel = np.array([[-1, 0, -1], # baris pertama matrix
                   [0, 4, 0],   # baris ke 2 matrix
                   [-1, 0, -1]])# baris ke 3 matrix
# Kernel ini memiliki efek memperkuat tepi pada citra, di mana nilai positif di tengah kernel akan meningkatkan intensitas tepi dan nilai negatif di sekitar kernel akan melemahkan intensitas tepi.
citraOutput = cv2.filter2D(gate, -1, kernel)# untuk menerapkan operasi konvolusi pada citra gate menggunakan kernel

fig, axes = plt.subplots(1, 3, figsize=(12, 12)) # bbuat subplot pada figur dengan ukuran 12x 12 1 baris 3 kolom
ax = axes.ravel()# buat fungsi ax untuk kordinat plot

ax[0].imshow(gate)# tampilkan citra asli
ax[0].set_title("Citra Input") # buat tittle untuk gambar asli
ax[1].imshow(gategrayscale, cmap = 'gray')# tampilkan gambar grayscale
ax[1].set_title("Citra grayscale") # buat tittle graycale
ax[2].imshow(citraOutput, cmap = 'gray')# tampilkan hasil konvolusi citra atau output
ax[2].set_title("Citra Output")# buat tittle untuk citra output

# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('baymax.jpg',0)

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

plt.show() # tampilkan citra