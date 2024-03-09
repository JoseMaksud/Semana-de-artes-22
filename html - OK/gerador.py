import cv2

im = cv2.imread('estudante.jpg')
altura = im.shape[0]
largura = im.shape[1]
pixels = largura * altura

print('Altura:', altura)
print('Largura:', largura)
print('Total de Pixels:', pixels)

contador = 1
#Gerador do CSS
with open('scarlett.css', 'w', encoding='utf-8') as f:
    for i in range(altura):
        for j in range(largura):
            pixel = im[i,j]
            rgb = 'rgb('+ str(+pixel[2]) + ',' + str(pixel[1]) + ',' + str(pixel[0]) + ')'
            linha = ('.p' + str(contador) + '{position:absolute;width:1px;height:1px;background-color:'+ rgb + ';top:'+ str(i) + 'px;left:'+ str(j) +'px;}')
            contador = contador + 1
            f.write(linha)
            f.write('\n')

#Gerador do HTML
contador = 1
with open('scarlett.html', 'w', encoding='utf-8') as f:
    for i in range(altura):
        for j in range(largura):
            linha = '<div class="p'+ str(contador) +'"></div>'
            contador = contador + 1
            f.write(linha)
            f.write('\n')
