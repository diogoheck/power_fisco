# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import os
from cruzamentos_analises import analise_c170 as analise_entradas
from cruzamentos_analises import analise_c190 as analise_saidas

from salvar_arquivos_excel import arquivos_excel as excel
from existe_arquivo import validar_arquivo as validar
from identifica_itens_saida import identifica_itens as tem_itens
from numeracao_notas import confere_numeracao
from cruzamento_num_nf import cruzamento_num_nf as cruzar
from somatorios import somatorios as soma_saidas
from compara_valores import compara_valores as compara
from openpyxl import Workbook
from resumo_analise import resumo_tributos as resumo
from energia_eletrica import energia_eletrica as cta_energia
from salvar_arquivos_excel import arquivos_excel as gera_excel

sa = 'ExtratoNFe_saidas.txt'
sped = 'sped.txt'
entradas = 'entradas.txt'
cte_saidas = 'ExtratoCte_saidas.txt'
cte_entradas = 'ExtratoCte_entradas.txt'

sped_1 = 'sped1.txt'
entradas_1 = 'entradas1.txt'
sa_1 = 'ExtratoNFe_saidas1.txt'
cte_saidas_1 = 'ExtratoCte_saidas1.txt'
cte_entradas_1 = 'ExtratoCte_entradas1.txt'


if __name__ == '__main__':

    print('executando........')

    if validar.existe_arquivo_sped(sped, sped_1):
        wb = Workbook()
        wb.save('power_fisco.xlsx')
        competencia = validar.retorna_competencia_arquivo(sped_1)

        compet = competencia.split(
            '|')[4][2:4] + competencia.split('|')[4][6::]

        print('conferindo numeracao de notas.....')
        # NUMERAÇÃO DE EMISSÃO PROPRIA NF-E
        confere_numeracao.conferir_numeracao_notas(sped_1)

        # CRUZAMENTOS NOTAS FISCAIS SAIDAS
        if validar.existe_sefaz_saidas(sa, sa_1):
            print('cruzando as notas de saídas.....')
            cruzar.cruzamento_entradas_saidas(sped_1, sa_1, '1', compet)
            compara.compara_valores(sped_1, sa_1, '1')
            compara.compara_valores_c100xc190(sped_1, '1')
            soma_saidas.soma_total(sa_1, sped_1)
            validar.remover_arquivos(sa_1)

        # CRUZAMENTOS DE CTEs DE SAIDAS
        if validar.existe_sefaz_cte_saidas(cte_saidas, cte_saidas_1):
            print('cruzando os CTEs de saídas.....')
            confere_numeracao.conferir_numeracao_notas(sped_1, True)
            cruzar.cruzamento_entradas_saidas_cte(
                sped_1, cte_saidas_1, '1', compet)
            compara.compara_valores_cte(sped_1, cte_saidas_1, '1')
            soma_saidas.soma_total_cte(cte_saidas_1, sped_1, '1')
            validar.remover_arquivos(cte_saidas_1)

        # CRUZAMENTOS NOTAS FISCAIS ENTRADAS
        if validar.existe_sefaz_entradas(entradas, entradas_1):
            print('cruzando as notas de entradas.....')
            cruzar.cruzamento_entradas_saidas(sped_1, entradas_1, '0', compet)
            compara.compara_valores(sped_1, entradas_1, '0')
            compara.compara_valores_c100xc190(sped_1, '0')
            validar.remover_arquivos(entradas_1)

        lista = cta_energia.lista_notas_energia_eletrica(sped_1)
        gera_excel.salvar_energia_eletrica(lista)

        # CRUZAMENTOS DE CTEs DE ENTRADAS
        if validar.existe_sefaz_cte_entradas(cte_entradas, cte_entradas_1):
            print('cruzando os CTEs de entradas.....')
            cruzar.cruzamento_entradas_saidas_cte(
                sped_1, cte_entradas_1, '0', compet)
            compara.compara_valores_cte(sped_1, cte_entradas_1, '0')
            validar.remover_arquivos(cte_entradas_1)

        # GERAÇÃO DAS ANALISES FISCAIS
        if tem_itens.identicar_itens_saidas(sped_1):
            print('montando as análises fiscais.....')
            lista_entradas = analise_entradas.analise_c170(sped_1)
            lista_resumo = resumo.resumo_tributos(lista_entradas, entrada=True)
            excel.salvar_analise_Full(lista_entradas, lista_resumo)
        else:
            print('montando as análises fiscais.....')
            lista_entradas = analise_entradas.analise_c170(sped_1, True)
            lista_resumo = resumo.resumo_tributos(lista_entradas, entrada=True)
            excel.salvar_analise_c170(lista_entradas, lista_resumo)
            lista_saidas = analise_saidas.analise_c190(sped_1)
            lista_resumo = resumo.resumo_tributos(lista_saidas, entrada=False)
            excel.salvar_analise_c190(lista_saidas, lista_resumo)

        validar.remover_arquivos(sped_1)
        print('\nfinalizado com sucesso....\o/\o/\o/\n')
        os.system("pause")
