from listar_numero_notas import listar_numero_nf as listar
from salvar_arquivos_excel import arquivos_excel as excel
from montar_arquivos_impressao import montar_arquivos_impressao as impressao


def cruzamento_entradas_saidas(sped, arquivo, eous, competencia):
    sped_entradas = listar.lista_numeros_notas_sped(sped, eous)
    sefaz_entradas = listar.lista_numeros_notas_sefaz(arquivo)
    spedxsefaz = sped_entradas - sefaz_entradas
    sefazxsped = sefaz_entradas - sped_entradas
    lista_notas_1 = impressao.impressao_entradas_sped(spedxsefaz, sped, eous)
    listar_notas_2 = impressao.impressao_entradas_sefaz(
        sefazxsped, arquivo, competencia)
    excel.salvar_spedxsefaz(lista_notas_1, eous)
    excel.salvar_sefazxsped(listar_notas_2, eous)


def cruzamento_entradas_saidas_cte(sped, arquivo, eous, competencia):
    sped_saidas = listar.lista_numeros_cte_sped(sped, eous)
    sefaz_saidas = listar.lista_numeros_cte_sefaz(arquivo)
    spedxsefaz = sped_saidas - sefaz_saidas
    sefazxsped = sefaz_saidas - sped_saidas
    lista_notas_1 = impressao.impressao_cte_sped(spedxsefaz, sped, eous)
    listar_notas_2 = impressao.impressao_cte_sefaz(
        sefazxsped, arquivo, competencia)
    excel.salvar_spedxsefaz(lista_notas_1, eous, True)
    excel.salvar_sefazxsped(listar_notas_2, eous, True)
