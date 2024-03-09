import cv2

def sepia(r, g, b):
    tr = 0.393 * r + 0.769 * g + 0.189 * b
    tg = 0.349 * r + 0.686 * g + 0.168 * b
    tb = 0.272 * r + 0.534 * g + 0.131 * b

    if tr > 255:
        r = 255
    else:
        r = tr

    if tg > 255:
        g = 255
    else:
        g = tg

    if tb > 255:
        b = 255
    else:
        b = tb
    
    y = [r,g,b]
    return y

im = cv2.imread('ventania.jpg')
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
        nova_cor = sepia(vermelho, verde, azul)
        im[i,j] = (nova_cor[2], nova_cor[1], nova_cor[0])

cv2.imwrite('ventania.png', im)