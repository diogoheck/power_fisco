from dicionarios_nf import dicionario_nf as dic


def analise_c170(sped, apenas_entradas=False):

    # STEP 5.1
    itens = dic.dict_cadastro_itens_sped(sped)
    # STEP 5.2
    if apenas_entradas:
        c170 = dic.dic_itens_movimentados_sped_so_entradas(sped, itens)
    else:
        c170 = dic.dic_itens_movimentados_sped(sped, itens)
    return c170
