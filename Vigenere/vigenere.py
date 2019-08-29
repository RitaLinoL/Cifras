alphabet = "abcdefghijklmnopqrstuvwxyz"
chave = "ipanema"


def searchPosition(ch):
	'''
	Funcao para buscar posicao do caracter no alfabeto definido O(n), onde n e a posicao de ch no alfabeto
	:param char ch - caracter a ser procurado no alfabeto
	'''
	for i in range(0,len(alphabet)):
		if alphabet[i] == ch:
			return i
	return -1



def readFile(file):
	file_open = open(file, "r")
	file_to_write = open("texto_claro.txt","w")
	msg = str()
	aux = 0

	for line in file_open:
		for letter in line:

			pos = searchPosition(letter)

			pos_chave = aux % len(chave) 

			if (pos == -1):
				file_to_write.write(letter)
				msg+= letter
			else:
				aux += 1
				p = (pos - searchPosition(chave[pos_chave]) + 26 ) % 26 #uso de expressao algebrica
				file_to_write.write(alphabet[p])
				msg += alphabet[p]
	
	return msg

				
		
print(readFile("mensagem.txt"))
