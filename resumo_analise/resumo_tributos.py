

def soma_valores_agrupados(lista_final, lista_completa, IND_CFOP_E, IND_CST_E, IND_ALIQ_E, IND_VLR_E, IND_BASE_E, IND_ICMS_E):
    lista_acum = []
    for li in lista_final:
        soma_ctb = 0
        soma_base = 0
        soma_icms = 0
        for lc in lista_completa:

            if li[0] == lc[IND_CFOP_E] and \
                    li[1] == lc[IND_CST_E] and \
                    li[2] == str(lc[IND_ALIQ_E]).replace('.', ','):

                soma_ctb = soma_ctb + lc[IND_VLR_E]
                soma_base = soma_base + lc[IND_BASE_E]
                soma_icms = soma_icms + lc[IND_ICMS_E]
                e115 = soma_ctb - soma_base
        lista_acum.append(
            [li[0], li[1], li[2], soma_ctb, soma_base, soma_icms, e115])
    return lista_acum


def criar_lista_resumida(dic, lista_distinta):
    lista_final = []

    for li in lista_distinta:
        if dic.get(li):
            lista_final.append(dic.get(li))

    lista_final = sorted(lista_final)

    return lista_final


def resumo_tributos(lista_entradas, entrada):
    lista = []
    lista_vlr_acum = []
    dic = {}
    second = False
    lista_final = []
    lista_distinta = set()

    if entrada:
        IND_CST_E = -1
        IND_CFOP_E = -2
        IND_ALIQ_E = -5
        IND_VLR_E = -9
        IND_BASE_E = -8
        IND_ICMS_E = -7
    else:
        IND_CFOP_E = -10
        IND_CST_E = -11
        IND_ALIQ_E = -9
        IND_VLR_E = -8
        IND_BASE_E = -7
        IND_ICMS_E = -6

    for l in lista_entradas:
        if second:
            if l[IND_ALIQ_E] == 0.0:
                l[IND_ALIQ_E] = '0'
            chave = str(l[IND_CFOP_E]).replace('.', ',') + str(l[IND_CST_E]
                                                               ).replace('.', ',') + \
                str(l[IND_ALIQ_E]).replace('.', ',') + ''

            lista_distinta.add(chave)
            lista.append(
                {chave: [l[IND_CFOP_E], l[IND_CST_E], str(l[IND_ALIQ_E]).replace('.', ',')]})
            dic[chave] = [l[IND_CFOP_E], l[IND_CST_E],
                          str(l[IND_ALIQ_E]).replace('.', ',')]
        second = True

    lista_final = criar_lista_resumida(dic, lista_distinta)

    lista_vlr_acum = soma_valores_agrupados(
        lista_final, lista_entradas, IND_CFOP_E, IND_CST_E, IND_ALIQ_E, IND_VLR_E, IND_BASE_E, IND_ICMS_E)

    return lista_vlr_acum


# def resumo_tributos_saidas(lista_entradas):
#     lista = []
#     dic = {}
#     second = False
#     lista_final = []
#     lista_distinta = set()
#     for l in lista_entradas:
#         if second:

#             chave = str(l[-10]).replace('.', ',') + str(l[-11]
#                                                         ).replace('.', ',') + \
#                 str(l[-9]).replace('.', ',') + ''

#             lista_distinta.add(chave)
#             lista.append(
#                 {chave: [l[-10], l[-11], str(l[-9]).replace('.', ',')]})
#             dic[chave] = [l[-10], l[-11], str(l[-9]).replace('.', ',')]
#         second = True

#     lista_final = criar_lista_resumida(dic, lista_distinta)
#     return lista_final
