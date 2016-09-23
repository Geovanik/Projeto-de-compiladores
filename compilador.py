
from sys import argv
matriz = []
tokens = []

def leituraGramatica (arq):
	lines = arq.readlines()#le tds as linhas da gramatica
	
	#for line in lines:
		#print line

	for line in lines:
		k=1
		partes = line.split("=")#separamos a linha em duas partes
		producoes = partes[1].split("|")#separando as producoes na quantidade de procucoes
		#print producoes
		
		for k in range(0,len(producoes)):
			tokens = producoes[k][producoes[k].find(" ")+1:producoes[k].find("<")]
			#k = k+1
			print tokens
		#tokens = producoes[0][producoes[0].find("<")+1:partes[0].find(">")]
		
		#quantidade = len(producoes)
		#aux = 0
		#for aux in range(0,len(producoes)):
		#	tokens[aux] = producoes[aux].split("<")
		#	aux = aux + 1
			
		#print ("\n")
		




############################################################# MAIN
arq = open ("gramatica.txt","r")

leituraGramatica (arq)

arq.close


