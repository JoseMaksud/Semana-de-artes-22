import cv2
import numpy as np

vermelho = 0
verde = 0
azul = 0

path = r'pierrette.jpg'
img = cv2.imread(path)
tamanho = img.shape
linhas = tamanho[0]
colunas = tamanho[1]
print('Tamanho da Imagem: Largura(%dpx) - Altura(%dpx)' % (linhas,colunas))

img_vermelho = np.zeros((linhas, colunas,3), np.uint8)
img_verde = np.zeros((linhas, colunas,3), np.uint8)
img_azul = np.zeros((linhas, colunas,3), np.uint8)

for l in range(linhas):
    for c in range(colunas):
        pixel_atual = img[l,c]

        vermelho = pixel_atual[2]
        img_vermelho[l,c] = (0, 0, vermelho)

        verde = pixel_atual[1]
        img_verde[l,c] = (0, verde, 0)

        azul = pixel_atual[0]
        img_azul[l,c] = (azul, 0, 0)

arquivo = 'vermelho.png'
cv2.imwrite(arquivo, img_vermelho)

arquivo = 'verde.png'
cv2.imwrite(arquivo, img_verde)

arquivo = 'azul.png'
cv2.imwrite(arquivo, img_azul)