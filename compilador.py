from sys import argv
from sets import Set
matriz = []
tokens = []
estados = Set([])
indice = []
contEstado = 1#contador de estados
estadosFinais = []

def leituraGramatica (arq):
	global matriz
	lines = arq.readlines()#le tds as linhas da gramatica
	matriz.append({})
	i=1
	for line in lines:
		k=1
		partes = line.split("::=")#separamos a linha em duas partes
		producoes = partes[1].split("|")#separando as producoes na quantidade de procucoes
		estado = partes[0].replace("<", "")
		estado = estado.replace(">", "")
		estados.add(estado)
		
		for k in range(0,len(producoes)):#separando tokens
			tokens = producoes[k][producoes[k].find(" ")+1:producoes[k].find("<")]
			tokens = tokens.replace("'", "")
			tokens = tokens.replace(" ", "")
			for c in tokens:
				if c != "\n" and c != "\r":
					try:
						if matriz[0][c] is None:
							pass
					except:
						matriz[0][c] = []
						indice.append(c)

def preencheTabela (arq):
	global matriz
	global contEstado
	global estadosFinais
	criou = 0
	lines = arq.readlines()#le tds as linhas da gramatica
	matriz.append({})
	for line in lines:
		cont = 0
		partes = line.split("::=")#separamos a linha em duas partes
		producoes = partes[1].split("|")#separando as producoes na quantidade de procucoes
		for k in range(0,len(producoes)):#separando tokens
			tokens = producoes[k][producoes[k].find(" ")+1:producoes[k].find("<")]
			if "<" in producoes[k] and ">" in producoes[k]:
				estado = producoes[k][producoes[k].find("<")+1:producoes[k].find(">")]
			tokens = tokens.replace("'", "")
			tokens = tokens.replace(" ", "")
			partes[0] = partes[0].replace("<", "")
			partes[0] = partes[0].replace(">", "")
			cont = 1
			for c in tokens:
				if c != "\n" and c != "\r":
					try:
						matriz[cont][c] = contEstado
						if partes[0] != estado:
							contEstado+=1
							criou = 1
							cont=contEstado
					except:
						matriz.append({})
						matriz[cont][c] = contEstado
						contEstado+=1
						cont=contEstado
						criou = 1
			if criou:
				matriz.append({})
				matriz[cont]['*'] = '*'
				estadosFinais.append(contEstado)
				criou = 0
		print
	i = 0
	b = 1
	for a in range(0, len(matriz)):
		for k in range(0, len(indice)):
			try:
				print matriz[b][indice[i]], "AUX " + indice[i]
			except:
				pass			
			i = i + 1
		b = b + 1
	print estadosFinais
		
def imprime():
	global matriz
	a = ""#usado na impressao de valores 
	#print (' '*11+'|'),
	for simbolo in indice:#mostrou as ligacoes
		print '%s' % (simbolo),"|",
		
	print
	print ('_ _'*(len(indice)*5))
	for simbolo in indice:
		try:
			print '%s' % (matriz[0][simbolo]),
		except:
			print '%s' % (a),"X",
	
		print ('|'),
	print
	print


############################################################# MAIN
arq = open("gramatica","r")

leituraGramatica (arq)

arq.close

arq = open("gramatica","r")

preencheTabela (arq)

arq.close

print indice

#imprime()
