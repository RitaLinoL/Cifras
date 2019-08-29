import sys #padrao de entrada : python esteganografia.py imagem modo(codificar ou decodificar) "mensagem"(se for modo ocultar)
from functions import hide, verifyLength, show
from PIL import Image


mode = sys.argv[2]#leitura do modo

pathImg = sys.argv[1]#caminho da imagem

#pega a mensagem oculta no arquivo messagem
file_message = open("messagem.txt", "r")
message = str()
for line in file_message:
	message += line
file_message.close()

if mode == 'ocultar':
	img = Image.open(pathImg)
	length = img.size
	
	if(verifyLength(message, img)):
		hide(message, img, length)

	else:
		print("Imagem com tamanho insufiente!")

elif mode == "mostrar":
	img = Image.open(pathImg)
	text = show(img)
	print(text)
	file_message_show =  open("messagem_revelada.txt", 'w')
	for line in text:
		file_message_show.write(line)
	file_message_show.close()

