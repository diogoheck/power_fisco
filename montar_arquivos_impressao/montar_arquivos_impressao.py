from dicionarios_nf import dicionario_nf as dic


def impressao_cte_sefaz(tupla, cte_entradas, competencia):
    lista_notas = []
    lista_notas.append(['data_emissao', 'CNPJ', 'IE', 'numero', 'valor'])
    notas_sefaz = dic.dict_notas_sefaz_cte(cte_entradas)
    for t in tupla:
        notas = notas_sefaz.get(t, 'nao encontrado')
        if notas == 'nao encontrado':
            print(f'o cte não encontrado e {t}')
        if notas != 'nao encontrado':
            # compet_sefaz = notas[8].split('/')[1] if notas[8] else ''
            compet_sefaz = notas[8].split('/')[1] + notas[8].split('/')[2][2:4]

            if compet_sefaz == competencia:

                valor = float(notas[9].replace('.', '').replace(
                    ',', '.')) if notas[9] else 0.0
                data_emissao = notas[8][0:10] if notas[8] else ''
                CNPJ = notas[3] if notas[3] else ''
                IE = notas[2] if notas[2] else ''
                num = notas[0] if notas[0] else ''

                lista_notas.append([data_emissao, CNPJ, IE, num, valor])
    return lista_notas


def impressao_cte_sped(tupla, sped, eous):
    lista_notas = []
    lista_notas.append(['data_emissao', 'data_entrada', 'CNPJ',
                       'CPF', 'IE', 'Fornecedor', 'numero', 'valor', 'chave'])
    notas_sped = dic.dict_notas_sped_cte(sped, eous)
    fornecedor = dic.dict_cadastro_fornecedores(sped)
    for t in tupla:
        notas = notas_sped.get(t, 'nao encontrado')
        if notas != 'nao encontrado':
            participante = fornecedor.get(notas[4], 'nao encontrado')
            CNPJ = participante[5] if participante else ''
            CPF = participante[6] if participante else ''
            IE = participante[7] if participante else ''
            NOME = participante[3] if participante else ''
            data_emissao = notas[11] if notas[11] else ''
            data_entrada = notas[12] if notas[12] else ''
            numero = notas[9] if notas[9] else ''
            valor = notas[15] if notas[15] else 0
            chave = notas[10] if notas[10] else ''
            lista_notas.append([data_emissao, data_entrada,
                               CNPJ, CPF, IE, NOME, numero, valor, chave])
    return lista_notas

# STEP 4.1.3


def impressao_entradas_sped(tupla, sped, eous):
    notas_sped = dic.dict_notas_sped(sped, eous)
    fornecedor = dic.dict_cadastro_fornecedores(sped)
    lista_notas = []
    msg = ''
    lista_notas.append(['data_doc', 'data_emiss', 'Num', 'CNPJ',
                       'CPF', 'IE', 'NOME', 'chave', 'VLR',
                        'BC_ICMS', 'VL_ICMS', ''])
    CNPJ = ''
    CPF = ''
    IE = ''
    NOME = ''
    DATA_DOC = ''
    DATA_EMISS = ''
    NUM = ''
    CHAVE = ''
    VALOR = ''
    BASE = ''
    ICMS = ''

    for t in tupla:
        msg = ''
        notas = notas_sped.get(t, 'nao encontrado')
        if notas != 'nao encontrado':
            if notas[6] == '00':
                participante = fornecedor.get(notas[4], 'nao encontrado')
                CNPJ = participante[5] if participante else ''
                CPF = participante[6] if participante else ''
                IE = participante[7] if participante else ''
                NOME = participante[3] if participante else ''

                DATA_DOC = notas[10][:2] + '/' + notas[10][2:4] + \
                    '/' + notas[10][4:8] if notas[10] else ''
                DATA_EMISS = notas[11][:2] + '/' + notas[11][2:4] + \
                    '/' + notas[11][4:8] if notas[11] else ''
                NUM = int(notas[8]) if notas[8] else ''
                CHAVE = notas[9] if notas[9] else ''
                VALOR = round(float(notas[12].replace(
                    ',', '.')), 2) if notas[12] else ''
                BASE = round(float(notas[21].replace(
                    ',', '.')), 2) if notas[21] else ''
                ICMS = round(float(notas[22].replace(
                    ',', '.')), 2) if notas[22] else ''
            elif notas[6] == '05':
                msg = 'INUTILIZADA'
                CNPJ = ''
                CPF = ''
                IE = ''
                NOME = ''
                DATA_DOC = notas[10][:2] + '/' + notas[10][2:4] + \
                    '/' + notas[10][4:8] if notas[10] else ''
                DATA_EMISS = notas[11][:2] + '/' + notas[11][2:4] + \
                    '/' + notas[11][4:8] if notas[11] else ''
                NUM = int(notas[8]) if notas[8] else ''
                CHAVE = notas[9] if notas[9] else ''
                VALOR = round(float(notas[12].replace(
                    ',', '.')), 2) if notas[12] else ''
                BASE = round(float(notas[21].replace(
                    ',', '.')), 2) if notas[21] else ''
                ICMS = round(float(notas[22].replace(
                    ',', '.')), 2) if notas[22] else ''
            elif notas[6] == '04':
                msg = 'DENEGADA'
                CNPJ = ''
                CPF = ''
                IE = ''
                NOME = ''
                DATA_DOC = notas[10][:2] + '/' + notas[10][2:4] + \
                    '/' + notas[10][4:8] if notas[10] else ''
                DATA_EMISS = notas[11][:2] + '/' + notas[11][2:4] + \
                    '/' + notas[11][4:8] if notas[11] else ''
                NUM = int(notas[8]) if notas[8] else ''
                CHAVE = notas[9] if notas[9] else ''
                VALOR = round(float(notas[12].replace(
                    ',', '.')), 2) if notas[12] else ''
                BASE = round(float(notas[21].replace(
                    ',', '.')), 2) if notas[21] else ''
                ICMS = round(float(notas[22].replace(
                    ',', '.')), 2) if notas[22] else ''
            elif notas[6] == '08':
                participante = fornecedor.get(notas[4], 'nao encontrado')
                CNPJ = participante[5] if participante else ''
                CPF = participante[6] if participante else ''
                IE = participante[7] if participante else ''
                NOME = participante[3] if participante else ''

                DATA_DOC = notas[10][:2] + '/' + notas[10][2:4] + \
                    '/' + notas[10][4:8] if notas[10] else ''
                DATA_EMISS = notas[11][:2] + '/' + notas[11][2:4] + \
                    '/' + notas[11][4:8] if notas[11] else ''
                NUM = int(notas[8]) if notas[8] else ''
                CHAVE = notas[9] if notas[9] else ''
                VALOR = round(float(notas[12].replace(
                    ',', '.')), 2) if notas[12] else ''
                BASE = round(float(notas[21].replace(
                    ',', '.')), 2) if notas[21] else ''
                ICMS = round(float(notas[22].replace(
                    ',', '.')), 2) if notas[22] else ''

            lista_notas.append(
                [DATA_DOC, DATA_EMISS, NUM, CNPJ, CPF, IE, NOME, CHAVE,
                 VALOR, BASE, ICMS, msg])

    return lista_notas


def impressao_entradas_sefaz(tupla, entradas, competencia):

    notas_sefaz = dic.dict_notas_sefaz(entradas)
    lista_notas = []
    lista_notas.append(['dt_Emit', 'Dt_Ent/Sai', 'IE_Emit', 'UF_Emit',
                        'CNPJ_Emit', 'Razao_Social_Emit', 'IE_Dest/Remet',
                        'UF_Dest/Remet', 'CNPJ_Dest/Remet',
                        'Razao_Social_Dest/Remet',
                        'Mod', 'Serie', 'Numero', 'Total_NF-e',
                        'Total_BC_ICMS', 'Total_ICMS', 'Total_BC_ICMS_ST',
                        'Total_ICMS_ST', 'Sit', 'E/S', 'Chave_NF-e'])
    for t in tupla:
        notas = notas_sefaz.get(t, 'nao encontrado')
        if notas != 'nao encontrado':
            compet_sefaz = notas[0].split('/')[1] + notas[0].split('/')[2]

            if compet_sefaz == competencia:

                lista_notas.append(notas)
    return lista_notas
