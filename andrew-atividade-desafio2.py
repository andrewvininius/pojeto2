tupla1 = (1, 2, 3) #tupla de inteiros

print(2 in tupla1)
print(22 in tupla1)

tupla2 = (1, 2, 3) #tupla de inteiros

print(tupla2.count(1))
tupla2 = (1, 1, 2, 3)
print(tupla2.count(1))

alunos = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(alunos) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

alunos[1] = 'Carolina'
print(alunos) # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana']

notas = []
notas.append(float(input('Digite a nota do primeiro aluno: ')))
notas.append(float(input('Digite a nota do segundo aluno: ')))
notas.append(float(input('Digite a nota do terceiro aluno: ')))
print(notas)
media = (notas[0] + notas[1] + notas[2]) / 3

dados_cliente = {
    'Nome': 'Renan',
    'Endereco': 'Rua Cruzeiro do Sul',
    'Telefone': '982503645'
}

print(dados_cliente['Nome']) # Renan

dic = {"joao":100,"maria":150}
dic["joao"]
100
dic["maria"]
150
dic["pedro"] = 10
dic
{'pedro': 10, 'joao': 100, 'maria': 150}
dic = {'joao': 100, 'maria': 150, 'pedro':
10}
dic
{'pedro': 10, 'joao': 100, 'maria': 150}
