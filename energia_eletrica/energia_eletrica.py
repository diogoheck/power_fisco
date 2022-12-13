def lista_notas_energia_eletrica(arquivo):
    with open(arquivo, encoding='UTF-8') as arquivo:
        nf = []
        nf.append([['', 'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART',
                   'COD_MOD', 'COD_SIT', 'SER', 'SUB', 'COD_CONS',
                    'NUM_DOC', 'DT_DOC', 'DT_E_S', 'VL_DOC', 'VL_DESC',
                    'VL_FORN', 'VL_SERV_NT', 'VL_TERC', 'VL_DA', 'VL_BC_ICMS',
                    'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'COD_INF',
                    'VL_PIS', 'VL_COFINS', 'TP_LIGACAO', 'COD_GRUPO_TENSAO',
                    'CHV_DOCe', 'FIN_DOCe', 'CHV_DOCe_REF', 'IND_DEST',
                    'COD_MUN_DEST', 'COD_CTA', 'COD_MOD_DOC_REF',
                    'HASH_DOC_REF', 'SER_DOC_REF', 'NUM_DOC_REF',
                    'MES_DOC_REF', 'ENER_INJET', 'OUTRAS_DED']])
        for registro in arquivo:
            notas = registro.strip().split('|')
            if notas[1] == 'C500':
                nf.append([notas])
    return nf
