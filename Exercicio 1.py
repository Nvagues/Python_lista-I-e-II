# Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma
# classe onde teremos o retorno do documento, o retorno do nome e
# verificação de tipo de pessoa, onde um método irá receber como
# parâmetro “F” ou “N” para trazer fumante ou não fumante.
# Feito isso, crie uma instância e retorne esses valores.


class Pessoa ():
    
    def__init__(self, cpf,nome,idade,fumante):
    self.cpf = cpf 
    self.nome = nome
    self.idade = idade 
    self.fumante = fumante
        
       
    def get_fumante(self, sim_ou_não):
        if sim_ou_não == "F":
            return f'{self.name} é fumante'
        elif sim_ou_não =="N":
            return f'{self.name} não é fumante'
        else:
            return "Não Informar"
        
pessoa1 = Pessoa ("Natalia Vagues","34","36180307890","N")        
            
          
    