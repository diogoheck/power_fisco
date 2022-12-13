

def analise_c190(sped):
    with open(sped, encoding='UTF-8') as sped:

        lista_itens = []
        lista_itens.append(['Num', 'Chave', 'CST', 'CFOP', 'ALIQ', 'VLR_OP',
                            'VL_BC_ICMS', 'VL_ICMS',
                            'BC_ICMS_ST', 'VL_ICMS_ST', 'VLR_RED_BC',
                            'VLR_IPI', 'COD_OBS'])

        for registro in sped:
            notas = registro.strip().split('|')

            if notas[1] == 'C100':
                if notas[2] == '1':
                    saida = True
                else:
                    saida = False

            if notas[1] == 'C100' and notas[2] == '1' and \
                    notas[6] != '02' and notas[6] != '05' and saida:
                num_nota = int(notas[8]) if notas[8] else ''  # add numero nota
                chave_nota = notas[9] if notas[9] else ''  # add chave nota

            if notas[1] == 'C190' and saida:
                cst = notas[2] if notas[2] else ''
                cfop = notas[3] if notas[3] else ''
                aliq = notas[4] if notas[4] else ''
                valor_op = round(float(notas[5].replace(
                    ',', '.')), 2) if notas[5] else 0.0
                base_icms = round(float(notas[6].replace(
                    ',', '.')), 2) if notas[6] else 0.0
                icms = round(float(notas[7].replace(
                    ',', '.')), 2) if notas[7] else 0.0
                base_st = round(float(notas[8].replace(
                    ',', '.')), 2) if notas[8] else 0.0
                icms_st = round(float(notas[9].replace(
                    ',', '.')), 2) if notas[9] else 0.0
                base_red = round(float(notas[10].replace(
                    ',', '.')), 2) if notas[10] else 0.0
                IPI = round(float(notas[11].replace(
                    ',', '.')), 2) if notas[11] else 0.0
                obs = notas[12] if notas[12] else ''

                lista_itens.append(
                    [num_nota, chave_nota, cst, cfop, aliq,
                        valor_op, base_icms, icms, base_st,
                        icms_st, base_red, IPI, obs])

    return lista_itens
