from sys import argv
from sets import Set
import csv
matriz = []
intermediaria = []
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
			if "'" in producoes[k]:
				tokens = producoes[k].replace("'", "")
				tokens = tokens.replace(" ", "")
				tokens = tokens.replace("\n", "")
				for c in tokens:
					if c != "\n" and c != "\r":
						try:
							if matriz[0][c] is None:
								pass
						except:
							matriz[0][c] = []
							indice.append(c)
			else:
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
        teste_estado = 0;
	lines = arq.readlines()#le tds as linhas da gramatica
	matriz.append({})
	for line in lines:
		cont = 0
                teste_estado = 0
		partes = line.split("::=")#separamos a linha em duas partes
		producoes = partes[1].split("|")#separando as producoes na quantidade de procucoes
		for k in range(0,len(producoes)):#separando tokens
			estado = None
			tokens = producoes[k][producoes[k].find(" ")+1:(producoes[k].find("<"))]
			if "<" in producoes[k] and ">" in producoes[k]:
				estado = producoes[k][producoes[k].find("<")+1:producoes[k].find(">")]
			partes[0] = partes[0].replace("<", "")
			partes[0] = partes[0].replace(">", "")
			cont = 0
			criou = 0
			if "'" in producoes[k]:
				print("PRODUCOES IF", producoes[k]);
				tokens = producoes[k].replace("'", "")
				tokens = tokens.replace(" ", "")
				for c in tokens:
					if c != "\n" and c != "\r":
						if teste_estado == 0 :
				        		contEstado+=1;                                    
				    			aux = contEstado;
                                        		teste_estado = 1;
						try:
							matriz[cont][c].append(contEstado)
							if estado == None:
								cont=contEstado
								criou = 1
						except:
							#matriz.append({}) #talvez retirar
							cont-=1
							contEstado+=1
							matriz[cont][c] = []
							matriz[cont][c].append(contEstado)
							cont=contEstado-1
							#criou = 1
				if producoes[k] == "''\n":
				    cont=contEstado;
				    criou = 1;
			else:
                                tokens = tokens.replace("'", "")
				tokens = tokens.replace(" ", "")
				if len(tokens) == 1:
				    if teste_estado == 0 :
				        contEstado+=1;                                    
				    	aux = contEstado;
                                        teste_estado = 1;
				    try:
					matriz[cont][tokens].append(aux)
					if partes[0] != estado:
					    cont=aux
				            criou = 1;
				    except:
					#matriz.append({}) #talvez retirar
					if partes[0] != estado:
					    cont=aux
				            criou=1
					matriz[cont][c] = []
					matriz[cont][c].append(aux)
		    	         	cont=aux;
					#criou = 1
				else: 
					tokens = tokens.replace("'", "")
					tokens = tokens.replace(" ", "")
					for c in tokens:
						if c != "\n" and c != "\r":
							try:
								matriz[cont][c].append(contEstado+1)
								if partes[0] != estado:
									cont=contEstado
									contEstado+=1
									criou = 1
								#criou = 1;
							except:
								matriz.append({})
								if partes[0] != estado:
									cont=contEstado
									contEstado+=1
									criou=1
								matriz[cont][c] = []
								matriz[cont][c].append(contEstado)
								cont=contEstado-1
								#criou = 1
					if estado == partes[0]:
						criou = 0			
			if criou:
                                print(producoes[k]);
				print("TAM ", len(matriz));
				matriz.append({})
				estadosFinais.append(contEstado)
				criou = 0
		print
	i = 0
	b = 0
	a = 0
	for a in range(0, len(matriz)):
		i = 0
		for k in range(0, len(indice)):
			try:
				print matriz[b][indice[i]], "AUX " + indice[i], "B ", b
			except:
				pass			
			i = i + 1
			#print
		b = b + 1
	print estadosFinais

def detMat():
	global contEstado
	global matriz
	global estadosFinais
	global simbolos
	global estadosAutomato
	cont=0
	existeInd=1
	novoEstado = 0
	while(existeInd):
		if(cont > 100):
			existeInd = 0
		for c, v in matriz[cont].iteritems():
			if len(v) > 1:
				contEstado+=1
				matriz.append({})
				for i in range(0,len(v)):
					pos=int(v[i])
					for a in indice:
						try:
							if matriz[pos][a] is not None:
								try:
									matriz[contEstado][a] = matriz[contEstado][a] + matriz[pos][a]
								except:
									matriz[contEstado][a]=[]
									matriz[contEstado][a] = matriz[contEstado][a] + matriz[pos][a]
							
						except:
							pass
						if pos in estadosFinais and contEstado not in estadosFinais:  
							estadosFinais.append(contEstado)
					novoEstado=1
			if(novoEstado==1):
				matriz[cont][c] = []
				matriz[cont][c].append(contEstado)
				print "Criou novo estado", contEstado, "indeterminismo em ", c, "com", v
				novoEstado+=1
				estados.add(contEstado)
                print("CONT ", cont)
		novoEstado=0		
		cont+=1
		if cont > 46:
			existeInd=0
		
def imprime():
	global matriz
	a = ""#usado na impressao de valores 
	print (' '*9+'|'),
	for simbolo in indice:#mostrou as ligacoes
		print '%8s' % (simbolo),"|",
		
	print
	print ('_ _'*(len(indice)*3))
	#verifique se o estado e final e imprima o *
	for i in range(0,len(matriz)):
		#if i not in inalcancaveis and i not in mortos:
		if i in estadosFinais:
			print "*",
		else:
			print " ",
		print '%6s' % (i),"|",
		#imprime os simbilos que sao nomes das regras
			
		for simbolo in indice:
			try:
				print '%8s' % (matriz[i][simbolo]),
			except:
				print '%6s' % (a),"X",
				
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

intermediaria = matriz;

i = 0;

while i < contEstado:
    for j in indice:
        try:
	    intermediaria[i][j] = intermediaria[i][j];
	except:
	    intermediaria[i][j] = []
	    intermediaria[i][j].append("X")
    i+=1;

imprime()

csvfile = "arq.csv"

with open(csvfile, 'w') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(indice)
    for i in range(0, len(intermediaria)):
        if i < 46:
		j = i;
		char_i = intermediaria[j]['i'];
		char_f = intermediaria[j]['f'];
		char_e = intermediaria[j]['e'];
		char_l = intermediaria[j]['l'];
		char_s = intermediaria[j]['s'];
		char_w = intermediaria[j]['w'];
		char_h = intermediaria[j]['h'];
		char_a = intermediaria[j]['a'];
		char_o = intermediaria[j]['o'];
		char_u = intermediaria[j]['u'];
		char_1 = intermediaria[j]['1'];
		char_2 = intermediaria[j]['2'];
		char_3 = intermediaria[j]['3'];
		char_4 = intermediaria[j]['4'];
		char_5 = intermediaria[j]['5'];
		char_6 = intermediaria[j]['6'];
		char_7 = intermediaria[j]['7'];
		char_8 = intermediaria[j]['8'];
		char_9 = intermediaria[j]['9'];
		char_0 = intermediaria[j]['0'];
		char_ma = intermediaria[j]['+'];
		char_me = intermediaria[j]['-'];
		char_di = intermediaria[j]['/'];
		char_di = intermediaria[j]['/'];
		char_ve = intermediaria[j]['*'];
		char_ig = intermediaria[j]['='];
		char_mm = intermediaria[j]['>'];
		char_mn = intermediaria[j]['<'];
		char_m = intermediaria[j]['m'];
		char_n = intermediaria[j]['n'];
		char_r = intermediaria[j]['r'];
		char_t = intermediaria[j]['t'];
		char_b = intermediaria[j]['b'];
		char_k = intermediaria[j]['k'];
		char_c = intermediaria[j]['c'];
		char_z = intermediaria[j]['z'];
		writer.writerow([char_i,char_f,char_e,char_l,char_s,char_w,char_h,char_a,char_o,char_u,char_1,char_2,char_3,char_4,char_5,char_6,char_7,char_8,char_9,char_0,char_ma,char_me,char_di,char_ve,char_ig,char_mm,char_mn,char_m,char_n,char_r,char_t,char_b,char_k,char_c,char_z]);

detMat()

intermediaria = matriz

i = 0;

while i < contEstado:
    for j in indice:
        try:
	    intermediaria[i][j] = intermediaria[i][j];
	except:
	    intermediaria[i][j] = []
	    intermediaria[i][j].append("X")
    i+=1;

csvfile = "arqDet.csv";

with open(csvfile, 'w') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(indice)
    for i in range(0, len(intermediaria)):
        if i < 49:
		j = i;
		char_i = intermediaria[j]['i'];
		char_f = intermediaria[j]['f'];
		char_e = intermediaria[j]['e'];
		char_l = intermediaria[j]['l'];
		char_s = intermediaria[j]['s'];
		char_w = intermediaria[j]['w'];
		char_h = intermediaria[j]['h'];
		char_a = intermediaria[j]['a'];
		char_o = intermediaria[j]['o'];
		char_u = intermediaria[j]['u'];
		char_1 = intermediaria[j]['1'];
		char_2 = intermediaria[j]['2'];
		char_3 = intermediaria[j]['3'];
		char_4 = intermediaria[j]['4'];
		char_5 = intermediaria[j]['5'];
		char_6 = intermediaria[j]['6'];
		char_7 = intermediaria[j]['7'];
		char_8 = intermediaria[j]['8'];
		char_9 = intermediaria[j]['9'];
		char_0 = intermediaria[j]['0'];
		char_ma = intermediaria[j]['+'];
		char_me = intermediaria[j]['-'];
		char_di = intermediaria[j]['/'];
		char_di = intermediaria[j]['/'];
		char_ve = intermediaria[j]['*'];
		char_ig = intermediaria[j]['='];
		char_mm = intermediaria[j]['>'];
		char_mn = intermediaria[j]['<'];
		char_m = intermediaria[j]['m'];
		char_n = intermediaria[j]['n'];
		char_r = intermediaria[j]['r'];
		char_t = intermediaria[j]['t'];
		char_b = intermediaria[j]['b'];
		char_k = intermediaria[j]['k'];
		char_c = intermediaria[j]['c'];
		char_z = intermediaria[j]['z'];
		writer.writerow([char_i,char_f,char_e,char_l,char_s,char_w,char_h,char_a,char_o,char_u,char_1,char_2,char_3,char_4,char_5,char_6,char_7,char_8,char_9,char_0,char_ma,char_me,char_di,char_ve,char_ig,char_mm,char_mn,char_m,char_n,char_r,char_t,char_b,char_k,char_c,char_z]);

imprime()

print(estadosFinais);
