

def dict_notas_sefaz(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = {}
        entrou1vez = True
        for registro in arquivo:
            notas = registro.strip().split(';')
            if not entrou1vez and notas[12] != 'Numero':
                nf[notas[20]] = notas
            entrou1vez = False
    return nf


def dict_notas_sefaz_cte(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = {}
        entrou1vez = True
        for registro in arquivo:
            notas = registro.strip().split(';')
            if not entrou1vez and notas[0].split('/')[0] != 'Ano ':
                notas[0] = int(notas[0].split('/')[2])
                nf[notas[0]] = notas
            entrou1vez = False
    return nf


def dic_itens_movimentados_sped_so_entradas(arquivo, itens):
    with open(arquivo, encoding='UTF-8') as arquivo:

        c100 = False
        c170 = False
        entrada = False
        lista_itens_totais = []
        lista_itens_totais.append(['num', 'Emitente', 'chave', 'cod_item',
                                  'descr', 'Valor',
                                   'Base ICMS', 'Valor ICMS',
                                   'Base ICMS ST', 'Vlr ICMS ST', 'Vlr IPI', 'aliq 0200',
                                   'aliq c170', 'un', 'NCM', 'CFOP', 'CST'])
        for registro in arquivo:
            notas = registro.strip().split('|')

            if notas[1] == 'C100':
                if notas[2] == '0':
                    entrada = True
                else:
                    entrada = False

            if notas[1] == 'C100' and notas[6] != '02' \
                    and notas[6] != '05' and entrada:
                c100 = True
                c170 = False
                num_nota = int(notas[8])  # add numero nota
                chave_nota = notas[9]  # add chave nota
                emitente = 'Emissão Própria' if notas[3] == '0' else 'Teceiros'
            if notas[1] == 'C170' and c100 and entrada:
                c170 = True
                lista_itens = []
                lista_itens.append(num_nota)
                lista_itens.append(emitente)

                lista_itens.append(chave_nota)

                # add codigo item
                lista_itens.append(notas[3])

                # add descrição item
                if itens.get(notas[3]) is not None:
                    lista_itens.append(itens.get(notas[3])[3])

                    valor = round(float(notas[7].replace(
                        ',', '.')), 2) if notas[7] else 0.0
                    base = round(float(notas[13].replace(
                        ',', '.')), 2) if notas[13] else 0.0
                    icms = round(float(notas[15].replace(
                        ',', '.')), 2) if notas[15] else 0.0
                    base_icms_st = round(float(notas[16].replace(
                        ',', '.')), 2) if notas[16] else 0.0
                    vl_icms_st = round(float(notas[18].replace(
                        ',', '.')), 2) if notas[18] else 0.0
                    vlr_IPI = round(float(notas[24].replace(
                        ',', '.')), 2) if notas[24] else 0.0
                    lista_itens.append(valor)
                    lista_itens.append(base)
                    lista_itens.append(icms)
                    lista_itens.append(base_icms_st)
                    lista_itens.append(vl_icms_st)
                    lista_itens.append(vlr_IPI)

                    # add alíquota item
                    lista_itens.append(itens.get(notas[3])[12])
                    lista_itens.append(notas[14])
                    # add alíquota c190
                    # aliq_c190 = ''
                    # lista_itens.append(aliq_c190)
                    # print(aliq_c190)
                    # add unidade item
                    lista_itens.append(itens.get(notas[3])[6])
                    # add NCM item
                    lista_itens.append(itens.get(notas[3])[8])
                    # add CFOP item
                    lista_itens.append(notas[11])
                    # add cst item
                    lista_itens.append(notas[10])
                    lista_itens_totais.append(lista_itens)
            if notas[1] == 'C190' and not c170 and entrada:
                lista_itens = []
                lista_itens.append(num_nota)
                lista_itens.append(emitente)

                lista_itens.append(chave_nota)

                # add codigo item
                lista_itens.append('')

                # add descrição item
                lista_itens.append('')

                valor = round(float(notas[5].replace(
                    ',', '.')), 2) if notas[5] else 0.0
                base = round(float(notas[6].replace(
                    ',', '.')), 2) if notas[6] else 0.0
                icms = round(float(notas[7].replace(
                    ',', '.')), 2) if notas[7] else 0.0
                base_icms_st = round(float(notas[8].replace(
                    ',', '.')), 2) if notas[8] else 0.0
                vl_icms_st = round(float(notas[9].replace(
                    ',', '.')), 2) if notas[9] else 0.0
                vlr_IPI = round(float(notas[11].replace(
                    ',', '.')), 2) if notas[11] else 0.0
                lista_itens.append(valor)
                lista_itens.append(base)
                lista_itens.append(icms)
                lista_itens.append(base_icms_st)
                lista_itens.append(vl_icms_st)
                lista_itens.append(vlr_IPI)

                # aliq 0200
                lista_itens.append('')

                # aliq c170/c190
                lista_itens.append(
                    round(float(notas[4].replace(',', '.')), 2)
                    if notas[4] else 0.0)

                # add unidade item
                lista_itens.append('')
                # add NCM item
                lista_itens.append('')
                # add CFOP item
                lista_itens.append(notas[3])
                # add cst item
                lista_itens.append(notas[2])
                lista_itens_totais.append(lista_itens)

    return lista_itens_totais


def dic_itens_movimentados_sped(arquivo, itens):
    with open(arquivo, encoding='UTF-8') as arquivo:

        c100 = False
        c170 = False
        lista_itens_totais = []
        lista_itens_totais.append(['num', 'Emitente', 'chave', 'cod_item',
                                  'descr', 'Valor',
                                   'Base ICMS', 'Valor ICMS',
                                   'Base ICMS ST', 'Vlr ICMS ST', 'Vlr IPI', 'aliq 0200',
                                   'aliq c170', 'un', 'NCM', 'CFOP', 'CST'])
        for registro in arquivo:
            notas = registro.strip().split('|')
            if notas[1] == 'C100' and notas[6] != '02' and notas[6] != '05':
                c100 = True
                c170 = False
                num_nota = int(notas[8])  # add numero nota
                chave_nota = notas[9]  # add chave nota
                emitente = 'Emissão Própria' if notas[3] == '0' else 'Teceiros'
            if notas[1] == 'C170' and c100:
                c170 = True
                lista_itens = []
                lista_itens.append(num_nota)
                lista_itens.append(emitente)

                lista_itens.append(chave_nota)

                # add codigo item
                lista_itens.append(notas[3])

                # add descrição item
                if itens.get(notas[3]) is not None:
                    lista_itens.append(itens.get(notas[3])[3])

                    valor = round(float(notas[7].replace(
                        ',', '.')), 2) if notas[7] else 0.0
                    base = round(float(notas[13].replace(
                        ',', '.')), 2) if notas[13] else 0.0
                    icms = round(float(notas[15].replace(
                        ',', '.')), 2) if notas[15] else 0.0
                    base_icms_st = round(float(notas[16].replace(
                        ',', '.')), 2) if notas[16] else 0.0
                    vl_icms_st = round(float(notas[18].replace(
                        ',', '.')), 2) if notas[18] else 0.0
                    vlr_IPI = round(float(notas[24].replace(
                        ',', '.')), 2) if notas[24] else 0.0
                    lista_itens.append(valor)
                    lista_itens.append(base)
                    lista_itens.append(icms)
                    lista_itens.append(base_icms_st)
                    lista_itens.append(vl_icms_st)
                    lista_itens.append(vlr_IPI)

                    # add alíquota item
                    lista_itens.append(itens.get(notas[3])[12])
                    lista_itens.append(notas[14])
                    # add unidade item
                    lista_itens.append(itens.get(notas[3])[6])
                    # add NCM item
                    lista_itens.append(itens.get(notas[3])[8])
                    # add CFOP item
                    lista_itens.append(notas[11])
                    # add cst item
                    lista_itens.append(notas[10])
                    lista_itens_totais.append(lista_itens)
            if notas[1] == 'C190' and not c170:
                lista_itens = []
                lista_itens.append(num_nota)
                lista_itens.append(emitente)

                lista_itens.append(chave_nota)

                # add codigo item
                lista_itens.append('')

                # add descrição item
                lista_itens.append('')

                valor = round(float(notas[5].replace(
                    ',', '.')), 2) if notas[5] else 0.0
                base = round(float(notas[6].replace(
                    ',', '.')), 2) if notas[6] else 0.0
                icms = round(float(notas[7].replace(
                    ',', '.')), 2) if notas[7] else 0.0
                base_icms_st = round(float(notas[8].replace(
                    ',', '.')), 2) if notas[8] else 0.0
                vl_icms_st = round(float(notas[9].replace(
                    ',', '.')), 2) if notas[9] else 0.0
                vlr_IPI = round(float(notas[11].replace(
                    ',', '.')), 2) if notas[11] else 0.0
                lista_itens.append(valor)
                lista_itens.append(base)
                lista_itens.append(icms)
                lista_itens.append(base_icms_st)
                lista_itens.append(vl_icms_st)
                lista_itens.append(vlr_IPI)

                # aliq 0200
                lista_itens.append('')

                # aliq c170/c190
                lista_itens.append(
                    round(float(notas[4].replace(',', '.')), 2)
                    if notas[4] else 0.0)

                # add unidade item
                lista_itens.append('')
                # add NCM item
                lista_itens.append('')
                # add CFOP item
                lista_itens.append(notas[3])
                # add cst item
                lista_itens.append(notas[2])
                lista_itens_totais.append(lista_itens)

    return lista_itens_totais


def dict_cadastro_itens_sped(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        itens = {}
        for registro in arquivo:
            iten = registro.strip().split('|')
            if iten[1] == '0200':
                itens[iten[2]] = iten
    return itens


def dict_cadastro_fornecedores(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        participantes = {}
        for registro in arquivo:
            participante = registro.strip().split('|')
            if participante[1] == '0150':
                participantes[participante[2]] = participante
    return participantes


def dict_notas_sped(arquivo, operacao):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = {}
        for registro in arquivo:
            notas = registro.strip().split('|')
            if notas[1] == 'C100' and notas[2] == operacao:
                if notas[9] != '':
                    nf[notas[9]] = notas
                else:
                    nf[notas[8]] = notas
    return nf


def dict_notas_sped_c190(arquivo, operacao):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = {}
        num_nota = ''
        lista_cfops = []
        tipo = operacao
        first = False
        achou_nota = False
        achou_c190 = False
        for registro in arquivo:
            notas = registro.strip().split('|')

            if notas[1] == 'C100' and notas[2] == operacao:
                if achou_c190:
                    nf[num_nota] = lista_cfops
                    lista_cfops = []
                    achou_c190 = False
                tipo = notas[2]
                num_nota = int(notas[8])
                achou_nota = True
                first = True

            if notas[1] == 'C100':
                tipo = notas[2]

            if achou_nota and notas[1] == 'C190' and operacao == tipo:
                if first:
                    lista_cfops = []
                    lista_cfops.append(notas[3])
                    achou_c190 = True
                    first = False
                else:
                    lista_cfops.append(notas[3])
                    achou_c190 = True
        if lista_cfops:
            nf[num_nota] = lista_cfops

    return nf


def dict_notas_sped_cte(arquivo, operacao):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = {}
        for registro in arquivo:
            notas = registro.strip().split('|')

            if notas[1] == 'D100' and notas[2] == operacao:
                notas[9] = int(notas[9])
                nf[notas[9]] = notas
    return nf


def lista_numeros_notas_sefaz(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = set()
        entrou1vez = True
        for registro in arquivo:
            notas = registro.strip().split(';')
            if not entrou1vez and notas[12] != 'Numero':
                nf.add(int(notas[12]))
            entrou1vez = False
    return nf
