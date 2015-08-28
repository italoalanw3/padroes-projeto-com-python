# lib padrão do Python para definir classes abstratas
import abc

""" Interface/Abstrata Componente """
class LinguagemProgramacao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def executar(self):
        return

""" Classe Componente DECORATOR """
class Interpretador(LinguagemProgramacao):
    """ construtor que recebe a interface que sera decorada """
    def __init__(self, linguagemProgramacao):
        self.linguagemProgramacao = linguagemProgramacao
        
    def executar(self):
        print('Interpretando...')
        self.linguagemProgramacao.executar()
        

""" Classe Componente Concreta """
class Python(LinguagemProgramacao):
    def __init__(self, versao):
        self.versao = versao
    def executar(self):
        print ('Executado Python %.2f' % self.versao)


# EXEMPLO DE EXECUCAO:
"""
python = Interpretador(Python(3.4))
python.executar()

#saída:
Interpretando...
Executado Python 3.40
"""
