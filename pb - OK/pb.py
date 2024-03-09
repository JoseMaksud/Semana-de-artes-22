import cv2
import numpy as np

vermelho = 0
verde = 0
azul = 0
soma = 0
media = 0

path = r'amigos.jpg'
img = cv2.imread(path)
tamanho = img.shape
linhas = tamanho[0]
colunas = tamanho[1]

img_pb = np.zeros((linhas, colunas,3), np.uint8)
img_bp = np.zeros((linhas, colunas,3), np.uint8)

for l in range(linhas):
    for c in range(colunas):
        pixel_atual = img[l,c]

        soma = int(pixel_atual[0]) + int(pixel_atual[1]) + int(pixel_atual[2])
        media = soma / 3
        if media > 127:
            img_pb[l,c] = (255,255,255)
            img_bp[l,c] = (0,0,0)
        else:
            img_pb[l,c] = (0,0,0)
            img_bp[l,c] = (255,255,255)

arquivo_pb = 'pb.png'
arquivo_bp = 'bp.png'
cv2.imwrite(arquivo_pb, img_pb )
cv2.imwrite(arquivo_bp, img_bp )