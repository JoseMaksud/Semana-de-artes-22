import cv2
import numpy as np

contador = 0

pixel = 20  #Alterar o valor do tamanho do 'pixel'
vermelho = 0
verde = 0
azul = 0

path = r'Gabriel.jpg'
img = cv2.imread(path)
tamanho = img.shape
altura = tamanho[0]
largura = tamanho[1]
print('Tamanho da Imagem: Largura(%dpx) - Altura(%dpx)' % (altura,largura))

linhas = int(altura / pixel)
colunas = int(largura / pixel)
print('Tamanho da Nova Imagem: Largura(%dpx) - Altura(%dpx)' % (linhas*pixel,colunas*pixel))

imgpx = np.zeros((linhas * pixel,colunas * pixel,3), np.uint8)

linhas_pixel = 0
lpx = 0
colunas_pixel = 0
cpx= 0

for l in range(linhas):

    for c in range(colunas):

        for i in range(pixel):

            for j in range(pixel):
                pixel_atual = img[(lpx) + i, (cpx) + j]
                vermelho = vermelho + pixel_atual[2]
                verde = verde + pixel_atual[1]
                azul = azul + pixel_atual[0]
                contador = contador + 1

        vermelho = int(vermelho/(pixel*pixel))
        if vermelho > 255:
            vermelho = 255
        verde = int(verde/(pixel*pixel))
        if verde > 255:
            verde = 255
        azul = int(azul/(pixel*pixel))
        if azul > 255:
            azul = 255

        for i in range(pixel):
            for j in range(pixel):
                imgpx[lpx + i][cpx + j] = (azul, verde, vermelho)
        
        vermelho = 0
        verde = 0
        azul = 0

        if colunas_pixel + 1 < colunas:
            colunas_pixel = colunas_pixel + 1
            cpx = cpx + pixel
        
    if linhas_pixel + 1 < linhas:
        linhas_pixel = linhas_pixel + 1 
        lpx = lpx + pixel
        colunas_pixel = 0
        cpx = 0

arquivo = 'gabriel.png'
cv2.imwrite(arquivo, imgpx)