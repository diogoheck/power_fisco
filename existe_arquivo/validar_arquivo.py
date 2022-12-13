# -*- coding: utf-8 -*-
from pathlib import Path
import os


def converte_utf8(file, file_1):
    with open(file, encoding='ansi') as arquivo:
        with open(file_1, 'w', encoding='utf-8') as saida:
            for registro in arquivo:
                print(registro.strip(), file=saida)


def existe_arquivo_sped(sped, sped_1):
    arq1 = Path(sped)
    if arq1.is_file():
        converte_utf8(sped, sped_1)
        return True
    return False


def retorna_competencia_arquivo(sped):
    with open(sped, encoding='ansi') as f:
        firstline = f.readline().rstrip()
    return firstline


def existe_sefaz_entradas(entradas, entradas_1):
    arq1 = Path(entradas)
    if arq1.is_file():
        converte_utf8(entradas, entradas_1)
        return True
    return False


def existe_sefaz_saidas(sa, sa_1):
    arq1 = Path(sa)
    if arq1.is_file():
        converte_utf8(sa, sa_1)
        return True
    return False


def existe_sefaz_cte_saidas(cte_saidas, cte_saidas_1):
    arq1 = Path(cte_saidas)
    if arq1.is_file():
        converte_utf8(cte_saidas, cte_saidas_1)
        return True
    return False


def existe_sefaz_cte_entradas(cte_entradas, cte_entradas_1):
    arq1 = Path(cte_entradas)
    if arq1.is_file():
        converte_utf8(cte_entradas, cte_entradas_1)
        return True
    return False


def remover_arquivos(arquivo):
    if arquivo:
        os.remove(arquivo)
