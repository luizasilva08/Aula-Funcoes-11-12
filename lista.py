''' Uma lista é uma estrutura de dados que permite armazenar vários valores dentro de uma única variável.'''

'''Tipos: numeros, nomes, dados; pode combinar vários tipos, como string, int, float, etc...'''

'''determina um espaço na memória para lista, e cada valor é dividido em índices [0,1,2,3...]'''

'''tamanho da lista - len()'''

notas = [7,8,6]
print(len(notas))

''' inserindo dados na lista - append()'''

nomes = []

nomes.append("Ana")
nomes.append("Carlos")

'''removendo dados da lista - remove()'''

nomes.remove("Carlos")

'''se eu não sei o valor exato, posso remover pelo índice'''

nomes.remove([1])

'''quando você remove um valor, a lista vai se reorganizando automaticamente (os índices)'''
'''trabalhar com caracteres dinamicos'''