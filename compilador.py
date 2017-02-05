import sys
from sets import Set
import csv
matriz = []
intermediaria = []
tokens = []
estados = Set([])
indice = []
contEstado = 1#contador de estados
estadosFinais = []
#fita = []
lalr = []
lista = []

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
	
class Tab_simbolos_60():
	rotulo = "variavel"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_16():
	rotulo = "numero"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_15():
	rotulo = "op_aritmetica"
	nome = "nome"
	linha = 0	

class Tab_simbolos_19():
	rotulo = "op_relacionais"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_21():
	rotulo = "reservado"
	nome = "main"
	linha = 0
	
class Tab_simbolos_29():
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

class Tab_simbolos_48():
	rotulo = "reservado"
	nome = "sizeof"
	linha = 0

class Tab_simbolos_47():
	rotulo = "op_relacionais"
	nome = "igual"
	linha = 0

#Nome fita saida
nome_fita = "fita_saida.txt"
arq_GP = "/home/casa/Downloads/GR-gold-parser2.txt"

estado0 = Tab_simbolos_nula#apenas para as posicoes vazias
estado1 = Tab_simbolos_erro
estado3 = Tab_simbolos_3
estado7 = Tab_simbolos_7
estado12 = Tab_simbolos_12
estado16 = Tab_simbolos_16
estado15 = Tab_simbolos_15
estado19 = Tab_simbolos_19
estado21 = Tab_simbolos_21
estado29 = Tab_simbolos_29
estado32 = Tab_simbolos_32
estado40 = Tab_simbolos_40
estado47 = Tab_simbolos_47
estado48 = Tab_simbolos_48
estado60 = Tab_simbolos_60

lista.append(estado0)#posicao 0
lista.append(estado1)#posicao 1 ERRO
lista.append(estado0)#posicao 0
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
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado15)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado19)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado21)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado29)#estado correto com suas informacoes
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
lista.append(estado0)#estado correto com suas informacoes
lista.append(estado47)#estado correto com suas informacoes
lista.append(estado48)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado60)#estado correto com suas informacoes
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
				#print("PRODUCOES IF", producoes[k]);
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
                                if contEstado not in estadosFinais:
				    estadosFinais.append(contEstado)
				criou = 0
	i = 0
	b = 0
	a = 0

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
                                                                        if matriz[pos][a] not in matriz[contEstado][a]:
									    matriz[contEstado][a] = matriz[contEstado][a] + matriz[pos][a]
                                                                        else:
                                                                            pass
								except:
									matriz[contEstado][a]=[]
									matriz[contEstado][a] = matriz[contEstado][a] + matriz[pos][a]
							
						except:
							pass
						if pos in estadosFinais and contEstado not in estadosFinais:
							estadosFinais.append(contEstado)
					novoEstado=1
			if(novoEstado==1):
                                print "Criou novo estado ", contEstado, "inderteminismo em c: ", c, " com: ", v
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
            #line = line.replace(" \n", "");
            aux_linha = line.split(" ");
            for k in range(0, len(line)):
                cont = 0
                for c in line[k]:
                    if c != " ":
		            try:
                                pos = verificaInt(matriz[pos_aux][c],pos_aux,c);
                                pos_aux = pos[0];
		            except: #erro escrita
                                while c != " ": #le ate terminar a palavra
                                    k+=1;
                                    try: #caso o erro esteja na ultima palavara da linha
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
                                print('Erro ELSE na linha %d' % (cont_linhas) + ' na palavra  %s' % (aux_linha[cont_componentes]));
                            if "\n" in aux_linha[cont_componentes]:
                                aux_linha[cont_componentes] = aux_linha[cont_componentes].replace("\n", "")
                            gravaFita(pos_aux, cont_linhas, aux_linha[cont_componentes]);
                            cont_componentes+=1                       
			    pos_aux = 0;
                            cont_split_linha+=1
                    cont+=1
            if pos_aux not in estadosFinais:
                pos_aux = 1;
                #cont_componentes-=1
                print('Erro na linha %d' % (cont_linhas) + ' na palavra  %s' % (aux_linha[cont_componentes]));
            if aux_linha[cont_componentes] != "" and pos_aux != 0: #espaco fim da linha
                if "\n" in aux_linha[cont_componentes]:
                    aux_linha[cont_componentes] = aux_linha[cont_componentes].replace("\n", "")
                gravaFita(pos_aux, cont_linhas, aux_linha[cont_componentes]);

    arq.close()

def gravaFita(num_estado, linha, palavra):
    global lista
    with open("fita_saida.txt", "a") as arq:
    	aux = lista[num_estado];
        str_fita = str(num_estado) + ";" + palavra + ";" + aux.rotulo + ";" + str(linha) + ";\n"
        arq.write(str_fita);
    arq.close();

#Leitura arquivo Gold Parser
def leituraArquivoGP():
    global arq_GP
    global lalr
    line = ""
    #u = 0
    arq = open(arq_GP,"r")
    while "Nonterminals" not in line: #ira ler o arquivo ate encontrar a palavra Nonterminals para completar a linha 0 da lalr
        line = arq.readline()
    line = arq.readline() #Provisorio
    line = arq.readline() #Provisorio
    #line = arq.readline() #Provisorio
    while 1: #leitura do arquivo ate acabar as informacoes bloco Nonterminals
        line = arq.readline()
        if line.startswith("\r"):
            break
        else:
            line = line.replace("\n", "")
            line = line.replace("\r", "")
            line_split = line.split(" ")
            for k in range(1, len(line_split)):
                aux = line_split[k][line_split[k].find("<")+1:line_split[k].find(">")] #procura ate encontrar o nome da regra
            lalr[0][aux] = []
    while "LALR States" not in line: #ira ler ate encontrar os estados LALR
        line = arq.readline()
    line = arq.readline() #Provisorio
    line = arq.readline() #Provisorio
    while 1: #leitura do arquivo ate acabar os estados
        while "State" not in line and '==' not in line: #ira ler ate encontrar o inicio das informacoes do estado
            line = arq.readline()
        if line.startswith("="): #testa se terminou os estados
            break
        while "<" not in line: #ira ler ate encontrar o inicio das regras
            line = arq.readline()
        while "<" in line: #ira ler ate terminarem as regras do estado
            line = arq.readline()
        while 1: #ira ler ate acabar informacoes do estado
            line = arq.readline()
            if line.startswith("\r"):
                break
            inf = line.split(" ")
            #print inf
            if "'" in inf[8]:
                print "ASPA"
            elif "<" in inf[8]:
                print "<"
            else: #palavra/char da linguagem
                print "PALAVRA"
    arq.close()
    
        

#LALR
def leituraFitaSaidaLalr():
    global lalr
    global nome_fita
    lalr.append({})
    arq = open(nome_fita,"r");
    lines = arq.readlines() #le tds as linhas da gramatica
    arq.close();
    for line in lines: #preenche a linha 0 da matriz
        partes = line.split(";") #separando as producoes na quantidade de procucoes
        try:
            if lalr[0][partes[0]] is None: #posicao na matriz ja foi criada e esta vaziz
                pass
        except:
             lalr[0][partes[0]] = []
    lalr[0]['$'] = []
    leituraArquivoGP()
    
		
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

#print("ESTADO FINAIS ", estadosFinais);
#arq = open("fita_saida.txt","w")
#arq.close
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

csvfile = "arqDet.csv"

with open(csvfile, 'w') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(indice)
    for i in range(0, len(intermediaria)):
        if i < 62:
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

#Tenta criar fita de saida. Se nao conseguir sera finalizado o programa
try:
    arq = open(nome_fita,"w")
except:
    print "Erro criacao fita saida. O programa sera abortado!"
    sys.exit(0)

#print lista
leituraFonte()
print "ESTADOS FINAIS ", estadosFinais;

#Leitura fita saida e criacao LALR
leituraFitaSaidaLalr()
