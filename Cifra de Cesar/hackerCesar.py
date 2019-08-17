alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,"

#Funcao para buscar posicao do caracter no alfabeto definido O(n)
def searchPosition(ch):
	for i in range(0,len(alphabet)-1):
		if alphabet[i] == ch:
			return i
	return -1



#Funcao de escrita em arquivo
def createFile(number, string):
	file_open = open(str(number)+".txt",'w+')
	file_open.close()
	return str(number)+".txt"


#Funcao que cria novos arquivos com o nome da chave.txt, esse arquivo com o texto descifrado utilizando a chave
def writeInFile(tentativa, file):
	file_to_write = open(file, "w")
	file_cifrado = open("textCesar.txt","r")

	for line in file_cifrado:
		for i in line:
			if i == "\n":
				file_to_write.write(i)
			else:
				file_to_write.write(alphabet[(searchPosition(i) + tentativa) % (len(alphabet))])


	file_to_write.close()
	file_cifrado.close()



for i in range(1, len(alphabet)):
	nameFile = createFile(i, alphabet)
	writeInFile(i, nameFile)



