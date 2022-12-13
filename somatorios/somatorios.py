from dicionarios_nf import dicionario_nf as dicionario
from salvar_arquivos_excel import arquivos_excel as excel

def soma_sefaz(saidas):
    dic = dicionario.dict_notas_sefaz(saidas)
    total_nfe = 0
    total_bc_icms = 0
    total_icms = 0
    total_bc_icms_st = 0
    total_icms_st = 0
    lista_saidas = []

    for k, v in dic.items():
        total_nfe = total_nfe + float(v[13].replace(',', '.'))   
        total_bc_icms = total_bc_icms + float(v[14].replace(',','.'))
        total_icms = total_icms + float(v[15].replace(',', '.'))
        total_bc_icms_st = total_bc_icms_st + float(v[16].replace(',', '.'))
        total_icms_st = total_icms_st + float(v[17].replace(',', '.'))
  

    lista_saidas.append(['SEFAZ', round(total_nfe, 2), round(total_bc_icms, 2)
                        , round(total_icms, 2), round(total_bc_icms_st, 2), 
                         round(total_icms_st, 2)])

    
    return lista_saidas


def soma_sped(sped):
    dic = dicionario.dict_notas_sped(sped, '1')
    total_nfe = 0
    total_bc_icms = 0
    total_icms = 0
    total_bc_icms_st = 0
    total_icms_st = 0
    lista_saidas = []
  
    for k, v in dic.items():
        if v[6] != '02' and v[6] != '05':
            if v[12] != '': 
                total_nfe = total_nfe + float(v[12].replace(',', '.'))   
            if v[21] != '': 
                total_bc_icms = total_bc_icms + float(v[21].replace(',','.'))
            if v[22] != '': 
                total_icms = total_icms + float(v[22].replace(',', '.'))
            if v[23] != '': 
                total_bc_icms_st = total_bc_icms_st + float(v[23].replace(',', '.'))
            if v[24] != '': 
                total_icms_st = total_icms_st + float(v[24].replace(',', '.'))
  

    lista_saidas.append(['SPED', round(total_nfe, 2), round(total_bc_icms, 2), round(total_icms, 2), round(total_bc_icms_st, 2), 
                         round(total_icms_st, 2)])

    
    return lista_saidas

def soma_sped_cte(sped, eous):
    dic = dicionario.dict_notas_sped_cte(sped, eous)
    total_nfe = 0
    total_bc_icms = 0
    total_icms = 0
    lista_saidas = []
  
    for k, v in dic.items():
        if v[6] != '02' and v[6] != '05':
            if v[15] != '': 
                total_nfe = total_nfe + float(v[15].replace(',', '.'))   
            if v[19] != '': 
                total_bc_icms = total_bc_icms + float(v[19].replace(',','.'))
            if v[20] != '': 
                total_icms = total_icms + float(v[20].replace(',', '.'))
  

    lista_saidas.append(['SPED', round(total_nfe, 2), round(total_bc_icms, 2), round(total_icms, 2)])

    return lista_saidas

def soma_total_cte (arquivo, sped, eous):
    total_nfe = 0
    total_bc_icms = 0
    total_icms = 0
    msg = False
    total_sefaz = soma_sefaz_cte(arquivo)
    total_sped = soma_sped_cte(sped, eous)
    lista_total = []
    lista_total.append(['', 'Total CTe', 'Total BC ICMS', 'Total ICMS'])
    lista_total.append(*total_sefaz)
    lista_total.append(*total_sped)
    total_nfe = total_sefaz[0][1] - total_sped[0][1]
    total_bc_icms = total_sefaz[0][2] - total_sped[0][2]
    total_icms = total_sefaz[0][3] - total_sped[0][3]

    if total_nfe or total_bc_icms or total_icms:
        msg = True


    lista_total.append(['dif',total_nfe, total_bc_icms, total_icms])

    excel.salvar_fechamento_saidas(lista_total, msg, True)

def soma_sefaz_cte(saidas):
    dic = dicionario.dict_notas_sefaz_cte(saidas)
    total_nfe = 0
    total_bc_icms = 0
    total_icms = 0
    lista_saidas = []

    for k, v in dic.items():
        valor = float(v[9].replace('.', '').replace(',', '.')) if v[9] else 0.0
        base_icms = float(v[10].replace('.', '').replace(',', '.')) if v[10] else 0.0
        icms = float(v[11].replace('.', '').replace(',', '.')) if v[11] else 0.0
        total_nfe = total_nfe + valor   
        total_bc_icms = total_bc_icms + base_icms
        total_icms = total_icms + icms
  
    lista_saidas.append(['SEFAZ', round(total_nfe, 2), round(total_bc_icms, 2), round(total_icms, 2)])

    return lista_saidas

def soma_total (saidas, sped):
    total_nfe = 0
    total_bc_icms = 0
    total_icms = 0
    total_bc_icms_st = 0
    total_icms_st = 0
    msg = False
    total_sefaz = soma_sefaz(saidas)
    total_sped = soma_sped(sped)
    lista_total = []
    lista_total.append(['', 'Total NF-e', 'Total BC ICMS', 'Total ICMS', 
                         'Total BC ICMS ST', 'Total ICMS ST'])
    lista_total.append(*total_sefaz)
    lista_total.append(*total_sped)
    total_nfe = total_sefaz[0][1] - total_sped[0][1]
    total_bc_icms = total_sefaz[0][2] - total_sped[0][2]
    total_icms = total_sefaz[0][3] - total_sped[0][3]
    total_bc_icms_st = total_sefaz[0][4] - total_sped[0][4]
    total_icms_st = total_sefaz[0][5] - total_sped[0][5]

    if total_nfe or total_bc_icms or total_icms or total_bc_icms_st or total_icms_st:
        msg = True


    lista_total.append(['dif',total_nfe, total_bc_icms, total_icms, total_bc_icms_st, total_icms_st])

    excel.salvar_fechamento_saidas(lista_total, msg)




    