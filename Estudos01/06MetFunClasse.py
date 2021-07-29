#Principal diferença entre método e função: função retorna valor e método não.

def multiplica(a,b): #declara um método
    return a * b

print(multiplica(5,6))


class Calculadoradefinida: #deve começar com letra maiúscula o nome de classe
    def __init__(self, num1, num2):
        pass #obrigatoriamente passa por esse método inicial cada chamada dessa classe
    #obriga a fornecer o parâmetro num1 e num2
        self.a = num1
        self.b = num2
    
    def soma(self):
        return self.a + self.b
    def subt(self):
        return self.a - self.b 

teste1 = Calculadoradefinida(5,30) #instancia a classe, chama init, mas para eu usar os outros métodos de uma classe preciso chamá-los
print(teste1.a)
print(teste1.subt()) #chama o método subt dentro da classe Calculadora


class Calculadoraindefinida: 
    
        def soma(self, numa, numb):
            return numa + numb
        def subt(self, numa, numb):
            return numa - numb 

teste2 = Calculadoraindefinida() 
print(teste2.soma(20,30)) 