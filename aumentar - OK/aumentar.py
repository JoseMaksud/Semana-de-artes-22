import cv2
image=cv2.imread('Ronald.jpg')
grande=cv2.pyrUp(image)
cv2.imwrite('grande.png', grande)