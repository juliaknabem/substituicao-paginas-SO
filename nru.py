class Pagina:
    def __init__(self, id_pagina):
        self.id_pagina = id_pagina
        self.bit_referencia = False
        self.bit_modificado = False

def substituicao_paginas_NRU(qtd_quadros, qtd_paginas, arquivo_referencia):
    quadros = []
    contador_falta_pagina = 0

    with open(arquivo_referencia, 'r') as file:
        referencia_paginas = [int(line) for line in file]

    for referencia in referencia_paginas:
        pagina_encontrada = False

        for quadro in quadros:
            if quadro.id_pagina == referencia:
                pagina_encontrada = True
                quadro.bit_referencia = True
                break

        if not pagina_encontrada:
            contador_falta_pagina += 1
            if len(quadros) < qtd_quadros:
                quadros.append(Pagina(referencia))
            else:
                quadros_nru = [quadro for quadro in quadros if quadro.bit_referencia == False and quadro.bit_modificado == False]
                if len(quadros_nru) > 0:
                    quadros.remove(quadros_nru[0])
                    quadros.append(Pagina(referencia))
                else:
                    quadros_nru = [quadro for quadro in quadros if quadro.bit_referencia == False and quadro.bit_modificado == True]
                    if len(quadros_nru) > 0:
                        quadros.remove(quadros_nru[0])
                        quadros.append(Pagina(referencia))
                    else:
                        quadros_nru = [quadro for quadro in quadros if quadro.bit_referencia == True and quadro.bit_modificado == False]
                        if len(quadros_nru) > 0:
                            quadros.remove(quadros_nru[0])
                            quadros.append(Pagina(referencia))
                        else:
                            quadros.remove(quadros[0])
                            quadros.append(Pagina(referencia))

    return contador_falta_pagina

# Exemplo de uso
qtd_quadros = int(input("Digite o número de quadros endereçáveis na memória: "))
qtd_paginas = int(input("Digite o total de páginas distintas endereçáveis: "))
arquivo_referencia = input("Digite o nome do arquivo contendo a lista de páginas referenciadas: ")
faltas_pagina = substituicao_paginas_NRU(qtd_quadros, qtd_paginas, arquivo_referencia)
print("Total de faltas de página:", faltas_pagina)