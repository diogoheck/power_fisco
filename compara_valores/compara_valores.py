from dicionarios_nf import dicionario_nf as dicionario
from salvar_arquivos_excel import arquivos_excel as excel


def compara_valores(sped, notas_sefaz, eous):

    lista_notas = []
    lista_cfops = ''
    lista_notas.append(['Chave', 'Data_doc', 'CNPJ', 'CPF', 'IE', 'NOME',
                        'Num', 'CFOP', 'Total_Sefaz', 'Total_SPEd', 'Difer',
                        'Base_ICMS_Sefaz', 'Base_ICMS_SPED', 'Difer',
                        'ICMS_sefaz', 'ICMS_SPED', 'Difer',
                        'Base_ICMS_ST_Sefaz', 'Base_ICMS_ST_SPED', 'Difer',
                        'ICMS_ST_sefaz', 'ICMS_ST_SPED', 'difer'])

    dic_sped = dicionario.dict_notas_sped(sped, eous)
    dic_sefaz = dicionario.dict_notas_sefaz(notas_sefaz)
    fornecedor = dicionario.dict_cadastro_fornecedores(sped)
    dic_c190 = dicionario.dict_notas_sped_c190(sped, eous)

    for k, v in dic_sefaz.items():
        if dic_sped.get(k):
            participante = fornecedor.get(dic_sped.get(k)[4], 'nao encontrado')
            CNPJ = participante[5] if participante else ''
            CPF = participante[6] if participante else ''
            IE = participante[7] if participante else ''
            NOME = participante[3] if participante else ''

            chave = dic_sped.get(k)[9] if dic_sped.get(k)[9] else ''
            data_doc = dic_sped.get(k)[10] if dic_sped.get(k)[10] else ''

            num = int(dic_sped.get(k)[8]) if dic_sped.get(k)[8] else ''

            vlr_sped = round(float(dic_sped.get(k)[12].replace(
                ',', '.')), 2) if dic_sped.get(k)[12] else 0.0
            base_icms_sped = round(float(dic_sped.get(k)[21].replace(
                ',', '.')), 2) if dic_sped.get(k)[21] else 0.0
            icms_sped = round(float(dic_sped.get(k)[22].replace(
                ',', '.')), 2) if dic_sped.get(k)[22] else 0.0
            base_icms_st_sped = round(float(dic_sped.get(k)[23].replace(
                ',', '.')), 2) if dic_sped.get(k)[23] else 0.0
            icms_st_sped = round(float(dic_sped.get(k)[24].replace(
                ',', '.')), 2) if dic_sped.get(k)[24] else 0.0

            vlr_sefaz = round(
                float(v[13].replace(',', '.')), 2) if v[14] else 0.0
            base_icms_sefaz = round(
                float(v[14].replace(',', '.')), 2) if v[15] else 0.0
            icms_sefaz = round(
                float(v[15].replace(',', '.')), 2) if v[16] else 0.0
            base_icms_st_sefaz = round(
                float(v[16].replace(',', '.')), 2) if v[17] else 0.0
            icms_st_sefaz = round(
                float(v[17].replace(',', '.')), 2) if v[18] else 0.0

            dif_opera = vlr_sefaz - vlr_sped
            dif_base_icms = base_icms_sefaz - base_icms_sped
            dif_icms = icms_sefaz - icms_sped
            dif_base_icms_st = base_icms_st_sefaz - base_icms_st_sped
            dif_icms_st = icms_st_sefaz - icms_st_sped

            if dif_opera or dif_base_icms or dif_icms or \
                    dif_icms_st or dif_base_icms_st:

                extrair_num = int(k[25:34])
                lista_cfops = dic_c190.get(
                    extrair_num) if dic_c190.get(extrair_num) else ''
                lista_cfops = '|'.join(lista_cfops)

                lista_notas.append([chave, data_doc, CNPJ, CPF, IE, NOME, num,
                                    lista_cfops, vlr_sefaz, vlr_sped,
                                    dif_opera,
                                    base_icms_sefaz, base_icms_sped,
                                    dif_base_icms,
                                    icms_sefaz, icms_sped, dif_icms,
                                    base_icms_st_sefaz, base_icms_st_sped,
                                    dif_base_icms_st,
                                    icms_st_sefaz, icms_st_sped, dif_icms_st])
    # print(lista_notas)
    excel.salvar_compara_entradas(lista_notas, eous)


def compara_valores_cte(sped, notas_sefaz, eous):

    lista_notas = []
    lista_notas.append(['Chave', 'Num', 'Total_Sefaz', 'Total_SPEd', 'Difer',
                        'Base_ICMS_Sefaz', 'Base_ICMS_SPED', 'Difer',
                        'ICMS_sefaz', 'ICMS_SPED', 'Difer'])

    dic_sped = dicionario.dict_notas_sped_cte(sped, eous)
    dic_sefaz = dicionario.dict_notas_sefaz_cte(notas_sefaz)

    for k, v in dic_sefaz.items():
        if dic_sped.get(k):
            chave = dic_sped.get(k)[10]
            num = dic_sped.get(k)[9]
            vlr_sped = round(float(dic_sped.get(k)[15].replace(
                ',', '.')), 2) if dic_sped.get(k)[15] else 0.0
            base_icms_sped = round(float(dic_sped.get(k)[19].replace(
                ',', '.')), 2) if dic_sped.get(k)[19] else 0.0
            icms_sped = round(float(dic_sped.get(k)[20].replace(
                ',', '.')), 2) if dic_sped.get(k)[20] else 0.0

            vlr_sefaz = round(
                float(v[9].replace('.', '').replace(',', '.')), 2) \
                if v[9] else 0.0
            base_icms_sefaz = round(
                float(v[10].replace('.', '').replace(',', '.')), 2) \
                if v[10] else 0.0
            icms_sefaz = round(
                float(v[11].replace('.', '').replace(',', '.')), 2) \
                if v[11] else 0.0

            dif_opera = vlr_sefaz - vlr_sped
            dif_base_icms = base_icms_sefaz - base_icms_sped
            dif_icms = icms_sefaz - icms_sped

            if dif_opera or dif_base_icms or dif_icms:

                lista_notas.append([chave, num, vlr_sefaz, vlr_sped, dif_opera,
                                   base_icms_sefaz, base_icms_sped,
                                   dif_base_icms, icms_sefaz, icms_sped,
                                   dif_icms])
    excel.salvar_compara_entradas(lista_notas, eous, True)


def compara_valores_c100xc190(sped, eous):

    lista_notas = []
    lista_notas.append(['Chave', 'Num', 'Total_C100', 'Total_C190', 'Difer',
                        'Base_ICMS_C100', 'Base_ICMS_C190', 'Difer',
                        'ICMS_C100', 'ICMS_C190', 'Difer',
                        'Base_ICMS_ST_C100', 'Base_ICMS_ST_C190', 'difer',
                        'ICMS_ST_C100', 'ICMS_ST_C190', 'difer'])

    with open(sped, encoding='UTF-8') as arquivo:
        first = True
        vlr_sped_C190 = 0.0
        base_icms_sped_C190 = 0.0
        icms_sped_C190 = 0.0
        base_icms_st_sped_C190 = 0.0
        icms_st_sped_C190 = 0.0

        for registro in arquivo:
            notas = registro.strip().split('|')
            if notas[1] == 'C100' and notas[2] == eous and notas[6] != '02' \
                    and notas[6] != '05':
                if first:
                    chave = notas[9]
                    num = notas[8]
                    vlr_sped_C100 = round(
                        float(notas[12].replace(',', '.')), 2) \
                        if notas[12] else 0.0
                    base_icms_sped_C100 = round(
                        float(notas[21].replace(',', '.')), 2) \
                        if notas[21] else 0.0
                    icms_sped_C100 = round(
                        float(notas[22].replace(',', '.')), 2) \
                        if notas[22] else 0.0
                    base_icms_st_sped_C100 = round(
                        float(notas[23].replace(',', '.')), 2) \
                        if notas[23] else 0.0
                    icms_st_sped_C100 = round(
                        float(notas[24].replace(',', '.')), 2) \
                        if notas[24] else 0.0
                    first = False
                else:
                    dif_opera = vlr_sped_C100 - round(vlr_sped_C190, 2)
                    dif_base_icms = base_icms_sped_C100 - \
                        round(base_icms_sped_C190, 2)
                    dif_icms = icms_sped_C100 - round(icms_sped_C190, 2)
                    dif_base_icms_st = base_icms_st_sped_C100 - \
                        round(base_icms_st_sped_C190, 2)
                    dif_icms_st = icms_st_sped_C100 - \
                        round(icms_st_sped_C190, 2)

                    if dif_opera or dif_base_icms or dif_icms or dif_icms_st:

                        lista_notas.append([chave, num, vlr_sped_C100,
                                            vlr_sped_C190, dif_opera,
                                            base_icms_sped_C100,
                                            base_icms_sped_C190, dif_base_icms,
                                            icms_sped_C100, icms_sped_C190,
                                            dif_icms,
                                            base_icms_st_sped_C100,
                                            base_icms_st_sped_C190,
                                            dif_base_icms_st,
                                            icms_st_sped_C100,
                                            icms_st_sped_C190, dif_icms_st])

                    chave = notas[9]
                    num = notas[8]
                    vlr_sped_C100 = round(
                        float(notas[12].replace(',', '.')), 2) \
                        if notas[12] else 0.0
                    base_icms_sped_C100 = round(
                        float(notas[21].replace(',', '.')), 2) \
                        if notas[21] else 0.0
                    icms_sped_C100 = round(
                        float(notas[22].replace(',', '.')), 2) \
                        if notas[22] else 0.0
                    base_icms_st_sped_C100 = round(
                        float(notas[23].replace(',', '.')), 2) \
                        if notas[23] else 0.0
                    icms_st_sped_C100 = round(
                        float(notas[24].replace(',', '.')), 2) \
                        if notas[24] else 0.0
                    vlr_sped_C190 = 0.0
                    base_icms_sped_C190 = 0.0
                    icms_sped_C190 = 0.0
                    base_icms_st_sped_C190 = 0.0
                    icms_st_sped_C190 = 0.0

            if notas[1] == 'C100':
                nota_valida = False if notas[2] != eous else True

            if notas[1] == 'C190' and nota_valida:

                vlr_sped_C190 = vlr_sped_C190 + \
                    round(float(notas[5].replace(',', '.')),
                          2) if notas[5] else 0.0
                base_icms_sped_C190 = base_icms_sped_C190 + \
                    round(float(notas[6].replace(',', '.')),
                          2) if notas[6] else 0.0
                icms_sped_C190 = icms_sped_C190 + \
                    round(float(notas[7].replace(',', '.')),
                          2) if notas[7] else 0.0
                base_icms_st_sped_C190 = base_icms_st_sped_C190 + \
                    round(float(notas[8].replace(',', '.')),
                          2) if notas[8] else 0.0
                icms_st_sped_C190 = icms_st_sped_C190 + \
                    round(float(notas[9].replace(',', '.')),
                          2) if notas[9] else 0.0

    excel.salvar_compara_c100xc190(lista_notas, eous)
