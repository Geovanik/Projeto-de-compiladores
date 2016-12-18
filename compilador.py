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
fita = []

class Tab_simbolos_nula():
	rotulo = "nula"
	nome = "nula"
	linha = "nula"

class Tab_simbolos_erro():
	rotulo = "erro"
	nome = "erro"
	linha = "erro"
	
class Tab_simbolos_3():
	rotulo = "condicao"
	nome = "if"
	linha = 0 #sera preenchida quando for lido no codigo fonte do programa do usuario
	
class Tab_simbolos_7():
	rotulo = "condicao"
	nome = "else"
	linha = 0
	
class Tab_simbolos_12():
	rotulo = "laco"
	nome = "while"
	linha = 0
	
class Tab_simbolos_13():
	rotulo = "variavel"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_14():
	rotulo = "numero"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_15():
	rotulo = "op_aritmetica"
	nome = "nome"
	linha = 0	

class Tab_simbolos_17():
	rotulo = "op_relacionais"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_21():
	rotulo = "reservado"
	nome = "main"
	linha = 0
	
class Tab_simbolos_27():
	rotulo = "reservado"
	nome = "return"
	linha = 0
	
class Tab_simbolos_32():
	rotulo = "reservado"
	nome = "break"
	linha = 0
	
class Tab_simbolos_40():
	rotulo = "reservado"
	nome = "continue"
	linha	= 0

class Tab_simbolos_46():
	rotulo = "reservado"
	nome = "sizeof"
	linha = 0

class Tab_simbolos_47():
	rotulo = "op_relacionais"
	nome = "igual"
	linha = 0

lista = []

estado0 = Tab_simbolos_nula#apenas para as posicoes vazias
estado1 = Tab_simbolos_erro
estado3 = Tab_simbolos_3
estado7 = Tab_simbolos_7
estado12 = Tab_simbolos_12
estado13 = Tab_simbolos_13
estado14 = Tab_simbolos_14
estado15 = Tab_simbolos_15
estado17 = Tab_simbolos_17
estado21 = Tab_simbolos_21
estado27 = Tab_simbolos_27
estado32 = Tab_simbolos_32
estado40 = Tab_simbolos_40
estado46 = Tab_simbolos_46
estado47 = Tab_simbolos_47

lista.append(estado0)#posicao 0
lista.append(estado1)#posicao 1 ERRO
lista.append(estado0)#posicao 2
lista.append(estado3)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado7)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado12)#estado correto com suas informacoes
lista.append(estado13)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado15)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado17)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado21)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado27)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado32)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado40)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado46)#estado correto com suas informacoes
lista.append(estado47)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0


print (lista[0].rotulo)
print (lista[7].rotulo)
print (lista[12].rotulo)
print (lista[17].rotulo)
print (lista[46].rotulo)
#print (lista[46].linha)
# estado - posicao na lista
# 3 - 0

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
							matriz.append({}) #talvez retirar
							cont-=1
							contEstado+=1
							matriz[cont][c] = []
							matriz[cont][c].append(contEstado)
							cont=contEstado-1
							criou = 1
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
				    if partes[0] == estado:
                                        for j in range(0,len(producoes)):#separando tokens
					    #estado = None
					    tokens = producoes[j][producoes[j].find(" ")+1:(producoes[j].find("<"))]
                                            tokens = tokens.replace(" ", "");
                                            try:
                                                if contEstado not in matriz[contEstado][tokens]:
				                    matriz[contEstado][tokens].append(contEstado)
					        if partes[0] != estado:
					            cont=aux
				                    criou = 1;
				            except:
					        #matriz.append({}) #talvez retirar
                                                matriz.append({})
					        if partes[0] != estado:
					            cont=aux
				                    criou=1
					        matriz[contEstado][tokens] = []
					        matriz[contEstado][tokens].append(contEstado);
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
								criou = 1;
							except:
								matriz.append({})
								if partes[0] != estado:
									cont=contEstado
									contEstado+=1
									criou=1
								matriz[cont][c] = []
								matriz[cont][c].append(contEstado)
								cont=contEstado-1
								criou = 1
					if estado == partes[0]:
						criou = 0			
			if criou:
				matriz.append({})
				estadosFinais.append(contEstado)
				criou = 0
		print
	i = 0
	b = 0
	a = 0
	#for a in range(0, len(matriz)):
	#	i = 0
	#	for k in range(0, len(indice)):
	#		try:
	#			print matriz[b][indice[i]], "AUX " + indice[i], "B ", b
	#		except:
	#			pass			
	#		i = i + 1
	#		#print
	#	b = b + 1
	#print estadosFinais

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
				novoEstado+=1
				estados.add(contEstado)
		novoEstado=0		
		cont+=1
		if cont > 46:
			existeInd=0

def verificaInt(lista,num,char):
    pos = []
    for aux in lista:
        try:
            pos.append(int(aux));
        except:
            pass
    return pos

def leituraFonte():
    global matriz
    pos = 0
    pos_aux = 0
    cont_linhas = 0
    b = '';
    arq = open("exprog","r")
    lines = arq.readlines()#le tds as linhas da gramatica
    for line in lines:
        pos_aux = 0
        cont_linhas = cont_linhas + 1
        cont_split_linha = 0
        aux_linha = None;
        if line != "\n":
            cont_componentes = 0 #contador para auxiliar navegacao nos componentes da linha atual
            cont_split_linha = 0
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            line = line.replace("\t", "")
            aux_linha = line.split(" ");
            for k in range(0, len(line)):
                cont = 0
                for c in line[k]:
                    if c != " ":
		            try:
                                pos = verificaInt(matriz[pos_aux][c],pos_aux,c);
                                pos_aux = pos[0];
		            except: #erro escrita
                                while c != " ":
                                    k+=1;
                                    try:
                                        c = line[k];
                                    except:
                                        break;
                                k+=1;
                                pos_aux = 1;
	            else: #chamar a funcao que grava na fita
                        #estado 1 de erro
                        if aux_linha[cont_componentes] != "": #espaco fim da linha
                            if pos_aux not in estadosFinais:
                                pos_aux = 1;
                            gravaFita(pos_aux, cont_linhas, aux_linha[cont_componentes]);
                            cont_componentes+=1                     
			    pos_aux = 0;
                            cont_split_linha+=1
                    cont+=1
            if pos_aux not in estadosFinais:
                pos_aux = 1;
            if aux_linha[cont_componentes] != "" and pos_aux != 0: #espaco fim da linha
                gravaFita(pos_aux, cont_linhas, aux_linha[cont_componentes]); 
    arq.close()

def gravaFita(num_estado, linha, palavra):
    global lista
    with open("fita_saida.txt", "a") as arq:
    	aux = lista[num_estado];
        str_fita = str(num_estado) + ";" + palavra + ";" + aux.rotulo + ";" + str(linha) + ";\n"
        arq.write(str_fita);
    arq.close();
    
		
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
            if "X" not in intermediaria[i][j]:
	        intermediaria[i][j] = intermediaria[i][j];
	except:
	    intermediaria[i][j] = []
	    intermediaria[i][j].append("X")
    i+=1;

detMat()

arq = open("fita_saida.txt","w")
arq.close
intermediaria = matriz

i = 0;

while i < contEstado:
    for j in indice:
        try:
            if "X" not in intermediaria[i][j]:
	        intermediaria[i][j] = intermediaria[i][j];
	except:
	    intermediaria[i][j] = []
	    intermediaria[i][j].append("X")
    i+=1;

leituraFonte()
print("ESTADO FINAIS ", estadosFinais);
