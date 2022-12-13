
from salvar_arquivos_excel import arquivos_excel as excel


def lista_numeros_notas_sped_emissao_propria(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = []
        for registro in arquivo:
            notas = registro.strip().split('|')

            if notas[1] == 'C100' and notas[3] == '0':
                nf.append([int(notas[8]), notas[7], notas[5]])
        nf = sorted(nf)
    return nf


def lista_numeros_notas_sped_emissao_propria_cte(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = []
        for registro in arquivo:
            notas = registro.strip().split('|')
            if notas[1] == 'D100' and notas[3] == '0':
                nf.append([int(notas[9]), notas[7], notas[5]])
        nf = sorted(nf)
    return nf


def conferir_numeracao_notas(arquivo, CTE=False):
    entrou1vez = True
    lista_faltas = []

    if not CTE:
        lista_notas_proprias_ordenadas = \
            lista_numeros_notas_sped_emissao_propria(
                arquivo)
    else:
        lista_notas_proprias_ordenadas = \
            lista_numeros_notas_sped_emissao_propria_cte(
                arquivo)
    for l in lista_notas_proprias_ordenadas:
        if entrou1vez:
            num_anterior = l[0]
            serie_anterior = l[1]
            modelo = l[2]
            entrou1vez = False
        elif l[1] == serie_anterior and \
                l[2] == modelo and l[0] - num_anterior < 1000:
            if l[0] - num_anterior == 1:
                num_anterior = l[0]
                serie_anterior = l[1]
                modelo = l[2]
            else:
                while (l[0] - num_anterior > 1):
                    num_anterior = num_anterior + 1
                    lista_faltas.append([num_anterior, modelo, serie_anterior])
                num_anterior = l[0]
        else:
            num_anterior = l[0]
            serie_anterior = l[1]
            modelo = l[2]

    excel.salvar_pulou_nf(lista_faltas, CTE)
