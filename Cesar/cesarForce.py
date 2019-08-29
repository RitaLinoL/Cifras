alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,"

def searchPosition(ch):
	'''
	Funcao para buscar posicao do caracter no alfabeto definido O(n), onde n e a posicao de ch no alfabeto
	:param char ch - caracter a ser procurado no alfabeto
	'''
	for i in range(0,len(alphabet)):
		if alphabet[i] == ch:
			return i
	return -1


def createFile(name):
	'''
	Funcao de escrita em arquivo usando o numero da tentativa
	:param str name - nome do arquivo a ser criado
	:return o nome do arquivo.txt
	'''
	file_open = open("tentativas/"+str(name)+".txt",'w+')
	file_open.close()
	return "tentativas/"+str(name)+".txt"



def writeInFile(chave, file_cifrado):
	'''
	Funcao que cria novos arquivos com o nome da chave.txt, esse arquivo com o texto descifrado utilizando a chave
	:param int chave - numero da chave tentada
	:param str file_cifrado - nome do arquivo a ser lido  
	'''
	file_to_write = open(createFile(chave), "w")
	file_cifrado = open(file_cifrado,"r")

	for line in file_cifrado:
		for i in line:
			if (searchPosition(i) == -1):
				file_to_write.write(i)
			else:
				indice = (searchPosition(i) - chave) % (len(alphabet))
				file_to_write.write(alphabet[indice])
	file_to_write.close()
	file_cifrado.close()


'''Tentativas de chaves iguais a quantidade de letras do alfabeto'''
for i in range(1, len(alphabet)):
	writeInFile(i, "textCesar.txt")


