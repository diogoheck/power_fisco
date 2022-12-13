

def lista_numeros_notas_sped(arquivo, operacao):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = set()
        for registro in arquivo:
            notas = registro.strip().split('|')

            if notas[1] == 'C100' and notas[2] == operacao and \
                    notas[6] != '02' and notas[9] != '':
                nf.add(notas[9])
            elif notas[1] == 'C100' and notas[2] == operacao and \
                    notas[6] != '02' and notas[6] != '05' \
                    and notas[6] != '04' and notas[9] == '':
                nf.add(notas[8])
            elif notas[1] == 'C100' and notas[2] == operacao and \
                    notas[6] != '02':
                nf.add(notas[8])
    return nf


def lista_numeros_notas_sefaz(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = set()
        entrou1vez = True
        for registro in arquivo:
            notas = registro.strip().split(';')
            if not entrou1vez and notas[12] != 'Numero':
                nf.add(notas[20])
            entrou1vez = False
    return nf


def lista_numeros_cte_sefaz(arquivo):
    with open(arquivo,  encoding='UTF-8') as arquivo:
        nf = set()
        entrou1vez = True
        for registro in arquivo:
            notas = registro.strip().split(';')
            if not entrou1vez and notas[0].split('/')[0] != 'Ano ':
                nf.add(int(notas[0].split('/')[2]))
            entrou1vez = False
    return nf


def lista_numeros_cte_sped(arquivo, operacao):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = set()
        for registro in arquivo:
            notas = registro.strip().split('|')
            if notas[1] == 'D100' and notas[2] == operacao \
                    and notas[6] != '02':
                nf.add(int(notas[9]))
    return nf
