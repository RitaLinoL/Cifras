from PIL import Image

def strToBin(message):
	'''strToBin e uma funcao que converte string em um vetor de binarios
	:param str message - messagem a ser passada para vetor de binarios
	:return list() msg_bin - retorna um vetor com binarios correspondendo as letras da messagem'''
	msg_bin = list()
	for x in range(0,len(message)):
		msg_bin.append(bin(ord(message[x]))[2:].zfill(8))
	return msg_bin



def imageToBin(image):
	'''imageToBin e uma funcao que converte pixeis de uma imagem para binario
	:param File(bmp) image - imagem a ser convertida
	:return list() img_bin retorna uma lista dos rgbs em binarios correspondente a imagem'''
	img_bin = list()

	for i in list(image.getdata()):
		r =  (bin(i[0])[2:].zfill(8)) 
		img_bin.append(r)
		g = (bin(i[1])[2:].zfill(8))
		img_bin.append(g)
		b = (bin(i[2])[2:].zfill(8))
		img_bin.append(b)
	return img_bin

def binToImage(img_bin):
	'''binToImage retorna uma imagem .bmp a partir da imagem em binario enviada
	:param binary img_bin - lista com as cores de cada pixel em binario e o texto oculto ]
	:return list img - lista de pixeis em decimal'''
	img = list() #lista com todos os pixeis
	pxl = list()
	color = 0 #0 = r, 1 = g, 2 = b
	for i in range(0,len(img_bin)):
		pxl.insert(color, int(img_bin[i], 2)) #converter algo em base 2 para inteiro
		color += 1 % 3
		if (i+1)%3 == 0 and i!=0:# a cada 3 cores (r,g,b) insere uma tupla na imagem
			img.insert(i,pxl)
			pxl = list()
			color = 0

	return img


def verifyLength(message, img):
	fit = (len(message)*9) < (len(list(img.getdata())) * 3)
	return fit

def createImg(img_bin, length):
	'''cria um arquivo .bmp com o texto oculto em seus bits
	:param File img_bin - imagem em binario com o texto oculto
	'''
	img = binToImage(img_bin)
	data = list()
	j=0
	for i in img:
		data.append(tuple(i))
	newImage = Image.new('RGB', length)
	newImage.putdata(data)
	newImage.save('img_com_messagem_oculta.bmp')



def hide(msg, img, length):
	''' hide e a funcao responsavel por ocultar a messagem na imagem
	:param str msg  - messagem em texto a sem ocultada
	:param File imd - imagem que recebera o texto
	:return 
	'''
	msg_bin = strToBin(msg)
	img_bin = imageToBin(img)
	letter_list= list()
	i = -1
	for letter in msg_bin: #caminha nas letras do texto
		letter_list = list(letter)
		letter_list.reverse()
		for bit_letter in letter_list: # caminha nos bits das letras
			i += 1
			if (i+1)%8 == 0: #se o proximo byte for o nono da seq RGBRGBRGB pula-se para a proxima sequencia 
				img_bin[i] = str(img_bin[i])[:-1]+bit_letter
				i+=1
				continue
			img_bin[i] = str(img_bin[i])[:-1]+bit_letter

	for b_terminador in '11000000': #inserindo byte de terminacao 3, endoftext na tabela ascii
		i += 1
		if (i+1)%8 == 0:
			img_bin[i] = str(img_bin[i])[:-1]+b_terminador
			i+=1
			continue
		img_bin[i] = str(img_bin[i])[:-1]+b_terminador
	
	createImg(img_bin, length)


def show(img):
	'''show() tira o texto escondido na imagem
	:param File bmp img - imagem com texto oculto
	:return str text - retorna o texto oculto na imagem'''
	img_bin = imageToBin(img)
	x = 0
	byte = str()
	message = str()
	for i in range(len(img_bin)):
		byte = list()
		for b in range(8):#caminha 8 bits em busca do terminador e da letra
			if(x % 8 == 0) and (x!= 0):
				x += 1
			byte.append(str(img_bin[x])[-1])
			x += 1


		byte.reverse()
		byte_str = ''.join(byte)

		if byte_str == "00000011": 
			break
		else:
			letter = chr(int(byte_str,2))
			message+=letter
			byte = ""
	return message

