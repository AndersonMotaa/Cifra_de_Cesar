mensagem = ''

def cifra_cesar(dado,chave):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    saida = ''
    if dado.isalpha() == False:
        return 'erro'
    for i in dado:
        indice = alfabeto.find(i)
        proximo_indice = indice + chave
        if proximo_indice <= (len(alfabeto) - 1):
            saida += alfabeto[proximo_indice]
        else:
            aux = proximo_indice - len(alfabeto)
            saida = saida + alfabeto[aux]
        
    return saida

try:
    while mensagem != 'SAIR 0':
        mensagem = input ("Digite a mensagem: ")
        mensagem = mensagem.upper()
        if mensagem == 'SAIR 0':
            break
        entrada = mensagem.split(" ")
        chave = int(entrada[1])
        print(cifra_cesar(entrada[0],chave))
        print('Digite "SAIR 0" para encerrar o programa')
except:
    print('erro na entrada da chave ou erro nao encontrado, inicie novamente o aplicativo')
