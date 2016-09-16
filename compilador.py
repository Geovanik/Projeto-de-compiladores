
from sys import argv
matriz = []
tokens = []

def leituraGramatica (arq):
	lines = arq.readlines()#le tds as linhas da gramatica
	
	for line in lines:
		print line

	for line in lines:
		partes = line.split("=")#separamos a linha em duas partes
		
		producoes = partes[1].split("|")
		
		quantidade = len(producoes)
		aux = 0
		for aux in range(0,len(producoes)):
			tokens[aux] = producoes[aux].split("<")
			aux = aux + 1
			
		print producoes




############################################################# MAIN
arq = open ("gramatica.txt","r")

leituraGramatica (arq)

arq.close


