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
lalr = []
lista = []
regras = []

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
	
class Tab_simbolos_14():
	rotulo = "variavel"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_16():
	rotulo = "numero"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_17():
	rotulo = "op_aritmetica"
	nome = "nome"
	linha = 0	

class Tab_simbolos_19():
	rotulo = "op_relacionais"
	nome = "nome"
	linha = 0
	
class Tab_simbolos_23():
	rotulo = "reservado"
	nome = "main"
	linha = 0
	
class Tab_simbolos_29():
	rotulo = "reservado"
	nome = "return"
	linha = 0
	
class Tab_simbolos_34():
	rotulo = "reservado"
	nome = "break"
	linha = 0
	
class Tab_simbolos_42():
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

#Pilha
class Pilha:
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def vazia(self):
        return len(self.dados) == 0
        
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def consulta(self):
        print " ", self.dados
  
    def lenPilha(self):
        return len(self.dados)

    def getvalor(self, simbolo):
	return legenda(simbolo)

    def getTopo(self):
	return self.dados[(len(self.dados))-1]
  

p = Pilha() #Pilha para analisador semantico
#Nome fita saida
nome_fita = "fita_saida.txt"
arq_GP = "GR-gold-parser2.txt"

estado0 = Tab_simbolos_nula#apenas para as posicoes vazias
estado1 = Tab_simbolos_erro
estado3 = Tab_simbolos_3
estado7 = Tab_simbolos_7
estado12 = Tab_simbolos_12
estado14 = Tab_simbolos_14
estado16 = Tab_simbolos_16
estado17 = Tab_simbolos_17
estado19 = Tab_simbolos_19
estado23 = Tab_simbolos_23
estado29 = Tab_simbolos_29
estado34 = Tab_simbolos_34
estado42 = Tab_simbolos_42
estado47 = Tab_simbolos_47
estado48 = Tab_simbolos_48

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
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado17)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado19)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado23)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado29)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado34)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado42)#estado correto com suas informacoes
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#posicao 0
lista.append(estado0)#estado correto com suas informacoes
lista.append(estado47)#estado correto com suas informacoes
lista.append(estado48)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes #53
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado16)#estado correto com suas informacoes
lista.append(estado17)#estado correto com suas informacoes
lista.append(estado17)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes		#64
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes
lista.append(estado14)#estado correto com suas informacoes

def legenda (string):

	if string == 'if':
		return 22
		
	elif string == 'else':
		return 7

        elif string == 'main':
		return 5
		
	elif string == 'var':# se for com mais de uma letra -erro
		return 14
		
	elif string == 'num':# mais de um digito
		return 16
		
	elif string == 'op':# operador aritmetico
		return 17

	elif string == 'laco':# operador aritmetico
		return 200

        elif string == 'while':# operador aritmetico
		return 12
		
	elif string == 'op2': #operador logico
		return 19
		
	elif string == 'return':
		return 29
		
	elif string == 'continue':
		return 13
		
	elif string == 'sizeof':
		return 19

	elif string == 'var2':# para apenas uma letra
		return 300
		
	elif string == 'condicao':
		return 100

	elif string == 70:
		return 'operando'

        elif string == 'break':
		return 27

	elif string == 'operando':
		return 'operando'

	elif string == 'num2':# para apenas um digito
		return 52

	elif string == 'reservadas':# para apenas uma letra
		return 110

        elif string == 'S':
		return 61
 
        elif string == '(EOF)':
		return 70

	elif string == '16':
		return 'num'

	elif string == '$':
		return 70

	elif string == '0':
                return 49
    
        elif string == '1':
		return 50

	elif string == '2':
		return 58

        elif string == '3':
		return 57

	elif string == '4':
		return 60

	elif string == '5':
		return 59

	elif string == '6':
		return 62

	elif string == '7':
		return 61

	elif string == '8':
		return 64
	
	elif string == '9':
		return 63

	elif string == '=':
		return 65

	elif string == "'4'":
		return 'exp1'

	elif string == '14':
		return 'var'

	elif string == '16':
		return 'num'

	elif string == '60':
		return 'op'

	elif string == 'op':
		return 60

	elif string == '17':
		return 'op'

	elif string == 'a':
		return 66

	elif string == 'e':
		return 67

	elif string == 'i':
		return 68

	elif string == 'o':
		return 69

	elif string == 'u':
		return 46

	elif string == '':
		return 50
	
	elif string =='<':
		return 54

	elif string == '50':
		return '+'

	elif string == '+':
		return 50

	elif string == '/' or string == '-':
                return 51

	elif string == '*':
		return 52

	elif string == '<' or string == '>' or string == '==':
                return 19

        elif string == 'e' or string == 'i' or string == 'o' or string == 'u' or 'a' in string or 'e' in string or 'i' in string or 'o' in string or 'u' in string:
                return 60

	elif '1' in string or '2' in string or '3' in string or '4' in string or '5' in string or '6' in string or '7' in string or '8' in string or '9' in string or '0' in string:
		return 16

        elif string == '1':
            	print("ERRO")

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
			tokens = producoes[k] = producoes[k].split(" ")
			for a in range(0,len(tokens)):#separando tokens
				if "'" in tokens[a]:
					if "'<'" not in tokens[a]:
						aux = tokens[a].split("<")
						try:
							if matriz[0]["<"] is None:
								pass
						except:
							matriz[0]["<"] = []
							indice.append("<")
					else:
						aux = tokens[a].split(" ")
					aux[0] = aux[0].replace("'","")
					aux[0] = aux[0].replace("\n","")
					for c in aux[0]:
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
	a = ""
	contAux = 0
	auxContAux = 0
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
			if contAux == 1:
				producoes[k] = "'='"
			if "'" in producoes[k]:
				if "<'" in producoes[k]: #caso seja o simbolo <
					c = '<'
					try:
						matriz[cont][tokens].append(contEstado)
						if partes[0] != estado:
						    criou = 1;
					except:
						matriz[cont][c] = []
						matriz[cont][c].append(contEstado)
				else:
					if len(producoes[k]) == 3:
					    producoes[k] = producoes[k].replace("'","")
					    if teste_estado == 0 :
						contEstado+=1;                                    
					    	aux = contEstado;
		                                teste_estado = 1;
					    try:
						matriz[cont][producoes[k]].append(aux)
						if partes[0] != estado:
						    cont=aux
						    criou = 1;
					    except:
						if partes[0] != estado:
						    cont=aux
						    criou=1
						matriz[cont][producoes[k]] = []
						matriz[cont][producoes[k]].append(aux)
			    	         	cont=aux;
					    if partes[0] == estado:
		                                for j in range(0,len(producoes)):#separando tokens
						    tokens = producoes[j][producoes[j].find(" ")+1:(producoes[j].find("<"))]
		                                    tokens = tokens.replace(" ", "");
		                                    try:
		                                        if contEstado not in matriz[contEstado][tokens]:
						            matriz[contEstado][tokens].append(contEstado)
							if partes[0] != estado:
							    cont=aux
						            criou = 1;
						    except:
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
				if contAux == 3 and auxContAux == 0:
					cont = 0
					tokens = "break"
					auxContAux+=1
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
				if contAux == 3 and auxContAux == 1:
					tokens = "'else'"
					cont = 0
					auxContAux+=1
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
				if contAux == 4 and auxContAux == 2:
					cont = 0
					tokens = "return"
					auxContAux+=1
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
		contAux+=1
		try:
			line = lines[contAux]
		except:
			pass

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

def leituraFonte(): #leitura do arquivo codigo (cria a fita de saida)
    global matriz
    pos = 0
    pos_aux = 0
    cont_linhas = 0
    b = '';
    flag_erro = 0
    arq = open("exprog","r")
    lines = arq.readlines()#le tds as linhas do arquivo
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
                                while c != " ": #le ate terminar a palavra
                                    k+=1;
                                    try: #caso o erro esteja na ultima palavara da linha
                                     	 c = line[k];
                                    except:
                                        break;
                                k+=1;
                                pos_aux = 1;
	            else: #chamar a funcao que grava na fita
                        if aux_linha[cont_componentes] != "": #espaco fim da linha
                            if pos_aux not in estadosFinais:
                                pos_aux = 1;
                                print('    Erro encontrado na linha %d' % (cont_linhas) + ' na palavra  %s' % (aux_linha[cont_componentes]));
                                flag_erro = 1
                            if "\n" in aux_linha[cont_componentes]:
                                aux_linha[cont_componentes] = aux_linha[cont_componentes].replace("\n", "")
                            gravaFita(pos_aux, cont_linhas, aux_linha[cont_componentes]);
                            cont_componentes+=1                       
			    pos_aux = 0;
                            cont_split_linha+=1
                    cont+=1
            if pos_aux not in estadosFinais:
                pos_aux = 1;
                print('    Erro encontrado na linha %d' % (cont_linhas) + ' na palavra  %s' % (aux_linha[cont_componentes]));
                flag_erro = 1
            if aux_linha[cont_componentes] != "" and pos_aux != 0: #espaco fim da linha
                if "\n" in aux_linha[cont_componentes]:
                    aux_linha[cont_componentes] = aux_linha[cont_componentes].replace("\n", "")
                gravaFita(pos_aux, cont_linhas, aux_linha[cont_componentes]);
    if flag_erro == 0:
        print "  Sucesso! Nao foram encontrados erros na analise lexica"
    else:
        print "  Foram encontrados erros na analise lexica"
    print
    arq.close()

def gravaFita(num_estado, linha, palavra):
    global lista
    with open("fita_saida.txt", "a") as arq:
    	aux = lista[num_estado];
        str_fita = str(num_estado) + ";" + palavra + ";" + aux.rotulo + ";" + str(linha) + ";\n"
        arq.write(str_fita);
    arq.close();

def leRegras():
    global arq_GP
    cont = 0
    cont_tam_linha = 0
    line = ""
    aux = ""
    arq = open(arq_GP, "r");
    while "Rules" not in line: #ira ler o arquivo ate encontrar o bloco Rules
        line = arq.readline()
    line = arq.readline()
    line = arq.readline()
    while 1: #leitura do arquivo ate acabar as informacoes bloco Nonterminals
        line = arq.readline()
        if line.startswith("\r"):
            break
 	regras.append({})
        line = line.replace("\r\n", "")
        line = line.split(" ")
        if int(line[0]) < 10:
            cont_tam_linha = len(line)
            regras[cont] = []
            line[7] = line[7].replace("<","")
            line[7] = line[7].replace(">","")
            line[7] = line[7].replace("'","")
            regras[cont] = str(legenda(line[7]))
            cont_tam_linha = 9
            while cont_tam_linha < len(line):
		aux = line[cont_tam_linha]
                line[cont_tam_linha] = line[cont_tam_linha].replace("<","")
            	line[cont_tam_linha] = line[cont_tam_linha].replace(">","")
            	line[cont_tam_linha] = line[cont_tam_linha].replace("'","")
                line[cont_tam_linha] = str(legenda(line[cont_tam_linha]))
                line[cont_tam_linha] = "'.'" + line[cont_tam_linha]
                regras[cont] = regras[cont] + line[cont_tam_linha]
                cont_tam_linha+=1
        else:
            cont_tam_linha = len(line)
            regras[cont] = []
            line[6] = line[6].replace("<","")
            line[6] = line[6].replace(">","")
            line[6] = line[6].replace("'","")
            regras[cont] = str(legenda(line[6]))
            cont_tam_linha = 8
            while cont_tam_linha < len(line):
		aux = line[cont_tam_linha]
                line[cont_tam_linha] = line[cont_tam_linha].replace("<","")
            	line[cont_tam_linha] = line[cont_tam_linha].replace(">","")
            	line[cont_tam_linha] = line[cont_tam_linha].replace("'","")
                line[cont_tam_linha] = str(legenda(line[cont_tam_linha]))
                line[cont_tam_linha] =  "'.'" + line[cont_tam_linha]
                regras[cont] = regras[cont] + line[cont_tam_linha]
                cont_tam_linha+=1
        cont+=1
    arq.close()

def contaEstadosCriaMatriz(): #conta a quantidade de estados do arquivo do gold parser e a matriz para shift/reduce
    global arq_GP
    cont_estado = 0
    cont = 0
    line = ""
    arq = open(arq_GP, "r");
    while "Nonterminals" not in line: #ira ler o arquivo ate encontrar a palavra Nonterminals para completar a linha 0 da lalr
        line = arq.readline()
    line = arq.readline()
    line = arq.readline()
    while 1: #leitura do arquivo ate acabar as informacoes bloco Nonterminals
        line = arq.readline()
        if line.startswith("\r"):
            break
    while "LALR States" not in line: #ira ler ate encontrar os estados LALR
        line = arq.readline()
    line = arq.readline()
    line = arq.readline()
    while 1: #leitura do arquivo ate acabar os estados
        line = arq.readline()
        if "State " in line: #ira ler ate encontrar o inicio das informacoes do estado
            cont_estado += 1
        if line.startswith("=="):
            break
    arq.close()
    while cont < cont_estado:
        lalr.append({})
        cont+=1

#Leitura arquivo Gold Parser
def leituraArquivoGP(): #le o arquivo do Gold Parser e preenche a tabela lalr
    global arq_GP
    global lalr
    line = ""
    num_estado = 1 #armazena o numero do estado atual
    num_est = 0 #armazena o estado shift/reduce
    u = 0
    arq = open(arq_GP,"r")
    while "Nonterminals" not in line: #ira ler o arquivo ate encontrar a palavra Nonterminals para completar a linha 0 da lalr
        line = arq.readline()
    line = arq.readline()
    line = arq.readline()
    while 1: #leitura do arquivo ate acabar as informacoes bloco Nonterminals e armazena do nome da regras lidas
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
    line = arq.readline()
    line = arq.readline()
    contaEstadosCriaMatriz();
    while 1: #leitura do arquivo ate acabar os estados
        if "State" not in line and '==' not in line: #ira ler ate encontrar o inicio das informacoes do estado
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
            if "'" in inf[8]:
                partes = line.split(" ") #separamos a linha em partes
                partes[8] = partes[8].replace("'", "")
                partes[10] = partes[10].replace("\r\n", "")
                num_est = legenda(partes[8])
		lalr[int(num_estado)][num_est] = []
		lalr[int(num_estado)][num_est].append(partes[9])
                lalr[int(num_estado)][num_est].append(partes[10])
            elif "<" in inf[8]:
                partes = line.split(" ") #separamos a linha em partes
                partes[8] = partes[8].replace("<", "")
                partes[8] = partes[8].replace(">", "")
                partes[10] = partes[10].replace("\r\n", "")
                lalr[int(num_estado)][partes[8]] = []
                lalr[int(num_estado)][partes[8]].append(partes[9])
                lalr[int(num_estado)][partes[8]].append(partes[10])
            elif "(" in inf[8]:
                partes = line.split(" ") #separamos a linha em partes
                num_est = legenda(partes[8])
                lalr[int(num_estado)][str(num_est)] = []
		partes[9] = partes[9].replace("\r\n", "")
                lalr[int(num_estado)][str(num_est)].append(partes[9])
                try: #pode ter (EOF) com ou sem estado
                    partes[10] = partes[10].replace("\r\n", "")
                    lalr[int(num_estado)][str(num_est)].append(partes[10])
                except:
                    pass
            else: #palavra/char da linguagem
                partes = line.split(" ") #separamos a linha em partes
                num_est = legenda(partes[8])
                lalr[int(num_estado)][num_est] = []
                partes[10] = partes[10].replace("\r\n", "")
                lalr[int(num_estado)][num_est].append(partes[9])
                lalr[int(num_estado)][num_est].append(partes[10])
        line = arq.readline() #ajustar leitor
        line = arq.readline() #ajustar leitor
        partes = line.split(" ")
        try:
            num_estado = int(partes[1])
        except:
            pass
        line = arq.readline() #ajustar leitor
    arq.close()

#LALR
def leituraFitaSaidaLalr(): #leitura da fita de saida e cria o cabecalho da matriz lalr
    global lalr
    global nome_fita
    lalr.append({})
    arq = open(nome_fita,"r");
    lines = arq.readlines() #le tds as linhas da gramatica
    arq.close();
    for line in lines: #preenche a linha 0 da matriz com os dados da fita de saida
        partes = line.split(";") #separando as producoes na quantidade de procucoes
        try:
            if lalr[0][partes[0]] is None: #posicao na matriz ja foi criada e esta vazia
                pass
        except:
             lalr[0][partes[0]] = []
    lalr[0]['70'] = []
    lalr[0]['61'] = []
    leituraArquivoGP()

def cargaFita(): #le a fita de saida e monta um vetor com a os dados da fita
    global nome_fita
    fita = []
    arq = open(nome_fita,"r");
    lines = arq.readlines() #le todas as linhas da fita de saida
    arq.close();
    for line in lines:
        line= line.split(";")
        fita.append(line[0])
    fita.append('$') #adiciona o simbolo $ no fim do vetor da fita
    return fita

def mostraLinha(cont):
	print lalr[cont], "num estado", cont

def buscaRegra(cod, simbolo):
    global regras
    if cod == 1: #busca nome da regra
        for aux in regras:
            if simbolo in aux:
                return regra
    else: #busca quantidade de itens da regra
        for aux in regras:
            if simbolo in aux:
		if '<' in aux:
			aux = aux.split(" ")
			aux = simbolo.split(".")
                	return (len(aux)-1)
		else:
			aux = simbolo.split(".")
                	return (len(aux)-1)
    

#analisador semantico
def analisadorSintatico():
    global lalr
    global p
    global nome_fita
    global regras
    num_estado = 1
    cont = 0
    fita = cargaFita()
    linha = fita[cont]
    while cont < len(fita) and p.lenPilha() > 0:
	print
	print "  Pilha:"
        p.consulta()
	print
	print "  Fita:", fita
        print
	if fita[cont] == '$': #terminou o conteudo da fita
		break
	if lalr[num_estado][int(linha)][0] == 'r': #reduce
	    quant = 0
	    aux = 0
	    val_regra = num_estado
	    regra = regras[int(lalr[num_estado][int(linha)][1])] #busca o nome da regra
	    quant =  buscaRegra(2,regra)#busca quantidade de elementos da regra
	    regra = regra.split("'.'")
	    while aux <= quant:
		print "  Desempilhou:", p.getTopo()
	        p.desempilha()
		aux+=1
	    aux_nome = legenda(regra[0])
	    aux_nome =aux_nome.replace("'","")
	    num_estado = int(lalr[int(p.getTopo())][str(aux_nome)][1])
	    p.empilha(aux_nome)
	    print "  Empilhou:", p.getTopo()
	    p.empilha(num_estado)
	    print "  Empilhou:", p.getTopo()
            linha = fita[cont]
	elif lalr[num_estado][int(linha)][0] == 's': #shift
	    p.empilha(fita[cont])#empilha o simbolo da acao do shift/reduce
	    print "  Empilhou:", p.getTopo()
	    p.empilha(lalr[num_estado][int(linha)][1]) #empilha o estado do shift/reduce
	    print "  Empilhou:", p.getTopo()
	    num_estado = (int(lalr[num_estado][int(linha)][1]))# - 1
	    print "  Retirou da fita:", fita[cont]
	    fita.pop(cont)
	    linha = fita[cont]
	elif lalr[num_estado][int(linha)][0] == 'g': #Goto
	    num_estado = (int(lalr[num_estado][int(linha)][1]))#-1
	else:
	    pass
    	print
    while 1: #termina reducao da pilha
	print "  Pilha:"
        p.consulta()
	print
	print "  Fita:", fita
        print
	if lalr[num_estado][str(legenda(fita[cont]))][0] == 'r': #reduce
	    quant = 0
	    aux = 0
	    if p.getTopo() == 23:
	        while aux <= 2:
			print "  Desempilhou:", p.getTopo()
			p.desempilha()
			aux+=1
                print "  Empilhou:", aux_nome,
		p.empilha(aux_nome)
	    val_regra = num_estado
	    regra = regras[int(lalr[num_estado][str(legenda(fita[cont]))][1])] #busca o nome da regra
	    quant =  buscaRegra(2,regra)#busca quantidade de elementos da regra
	    regra = regra.split("'.'")
	    if p.getTopo() == 23:
		quant = 2
	    aux = 0
	    while aux <= quant:
		print "  Desempilhou", p.getTopo()#, "da pilha REDUCE FIM FITA"
	        p.desempilha()
		aux+=1
            aux_nome = p.getTopo()
	    p.empilha(legenda(regra[0]))
	    print "  Empilhou:", p.getTopo()
	    p.empilha(lalr[aux_nome][str(legenda(regra[0]))][1])
	    print "  Empilhou:", p.getTopo()
	    aux_nome = legenda(regra[0])
	    aux_nome =aux_nome.replace("'","")
	    num_estado = int(lalr[int(p.getTopo())][str(legenda(aux_nome))][1])
            linha = fita[cont]
	else:
	    print "Erro! Problema na transicao"
	    break


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

detMat()

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

#Tenta criar fita de saida. Se nao conseguir sera finalizado o programa
try:
    arq = open(nome_fita,"w")
except:
    print "Erro criacao fita saida. O programa sera abortado!"
    sys.exit(0)

print
print
print "  Inicio da analise lexica"
leituraFonte()

leituraFitaSaidaLalr()

def imprimeLaLr():
    cont = 1
    c = lalr[0]
    while(cont <= 101):
        for a in lalr[1]:
            try:
                if lalr[cont][a] and cont == 1:
                    print a, ":", lalr[cont][a]
            except:
                pass
        cont+=1

leRegras()

p.empilha('0') #empilha o simbolo inicial
print "  Inicio do processo de analise sintatica:"
analisadorSintatico()
