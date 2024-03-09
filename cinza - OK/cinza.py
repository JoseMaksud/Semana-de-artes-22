from tkinter import Y
import cv2

def cinza(r, g, b):
    y = round(r * 0.299 + g * 0.587 + b * 0.114)
    return y

im = cv2.imread('Ronald.jpg')
altura = im.shape[0]
largura = im.shape[1]
pixels = largura * altura

print('Altura:', altura)
print('Largura:', largura)
print('Total de Pixels:', pixels)

for i in range(altura):
    for j in range(largura):
        cor = im[i,j]
        azul = cor[0]
        verde = cor[1]
        vermelho = cor[2]
        cor_cinza = cinza(vermelho, verde, azul)
        im[i,j] = (cor_cinza, cor_cinza, cor_cinza)

cv2.imwrite('cinza.png', im)













