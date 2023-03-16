import cv2


imagem = cv2.imread("imagens/images.jpg")
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv2.imshow("Imagem", imagemCinza)
cv2.waitKey()