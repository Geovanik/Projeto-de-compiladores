class Pilha(object):
    def __init__(self):
        self.dados = []
 
    def empilha(self, elemento):
        self.dados.append(elemento)
 
    def vazia(self):
        return len(self.dados) == 0
        
    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)
            
  
p = Pilha()
p.empilha('0;8')
p.empilha('7;30')
p.empilha('11;20')
p.empilha('10')
print p.desempilha(),
print p.desempilha(),
print p.desempilha(),
print p.desempilha(), 

def shift():
	
	#pega o elemento da primeira linha mais o estado para onde vai. Ex foto
	#p.empilha(#elemento lido)
	
	#retira da lista a elemento empilhado
