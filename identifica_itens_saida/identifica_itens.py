def identicar_itens_saidas(sped):
    achou_nota_propria = False
    with open(sped, encoding='UTF-8') as sped:
        for registro in sped:
            notas = registro.strip().split('|')
            if notas[1] == 'C100' and notas[2] == '1' \
                    and notas[9] != '' and notas[6] != '02':
                achou_nota_propria = True
            if notas[1] == 'C170' and achou_nota_propria:
                return True
            if notas[1] == 'C190' and achou_nota_propria:
                return False
    return True
